import argparse
import glob
import os

import cv2
import matplotlib
import numpy as np
import torch
from icecream import ic

from depth_anything_v2.dpt import DepthAnythingV2
from modules.utils import read_json

# --- Global variables
json_filepath = "uint16_scale_factor.json"
UINT16_SCALE_FACTOR = read_json(json_filepath)['inv_depth']
# ic(UINT16_SCALE_FACTOR)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Depth Anything V2')

    parser.add_argument('--img-path', type=str)
    parser.add_argument('--input-size', type=int, default=518)
    parser.add_argument('--outdir', type=str, default='./vis_depth')

    parser.add_argument('--encoder', type=str, default='vitl', choices=['vits', 'vitb', 'vitl', 'vitg'])

    parser.add_argument('--save-numpy', dest='save_numpy', action='store_true', help='save the model raw output')
    parser.add_argument('--pred-only', dest='pred_only', action='store_true', help='only display the prediction')
    parser.add_argument('--grayscale', dest='grayscale', action='store_true', help='do not apply colorful palette')
    parser.add_argument('--save-uint16', dest='save_uint16', action='store_true', help='save as 16-bit uint image')

    args = parser.parse_args()

    mps_cond = 'mps' if torch.backends.mps.is_available() else 'cpu'
    DEVICE = 'cuda' if torch.cuda.is_available() else mps_cond

    model_configs = {
        'vits': {'encoder': 'vits', 'features': 64, 'out_channels': [48, 96, 192, 384]},
        'vitb': {'encoder': 'vitb', 'features': 128, 'out_channels': [96, 192, 384, 768]},
        'vitl': {'encoder': 'vitl', 'features': 256, 'out_channels': [256, 512, 1024, 1024]},
        'vitg': {'encoder': 'vitg', 'features': 384, 'out_channels': [1536, 1536, 1536, 1536]}
    }

    depth_anything = DepthAnythingV2(**model_configs[args.encoder])
    depth_anything.load_state_dict(torch.load(f'checkpoints/depth_anything_v2_{args.encoder}.pth', map_location='cpu'))
    depth_anything = depth_anything.to(DEVICE).eval()

    if os.path.isfile(args.img_path):
        if args.img_path.endswith('txt'):
            with open(args.img_path, 'r') as f:
                filenames = f.read().splitlines()
        else:
            filenames = [args.img_path]
    else:
        filenames = glob.glob(os.path.join(args.img_path, '**/*'), recursive=True)

    os.makedirs(args.outdir, exist_ok=True)

    cmap = matplotlib.colormaps.get_cmap('Spectral_r')

    print(f'Processing {len(filenames)} images...')
    for k, filename in enumerate(filenames):
        # Check if the file is a folder
        if os.path.isdir(filename):
            continue

        print(f'Progress {k+1}/{len(filenames)}: {filename}')

        raw_image = cv2.imread(filename)

        depth = depth_anything.infer_image(raw_image, args.input_size)  # affine-invariant inverse depth, float32
        # ic(depth.shape, depth.dtype, depth.min(), depth.max())

        depth_uint16 = (depth * UINT16_SCALE_FACTOR).astype(np.uint16)
        # ic(depth_uint16.shape, depth_uint16.dtype, depth_uint16.min(), depth_uint16.max())

        if args.save_numpy:
            output_path = os.path.join(args.outdir, f'{os.path.splitext(os.path.basename(filename))[0]}_raw_inv_depth.npy')
            np.save(output_path, depth)

        suffix = ''
        if args.save_uint16:
            suffix = '_uint16'
            cv2.imwrite(os.path.join(args.outdir, f'{os.path.splitext(os.path.basename(filename))[0]}{suffix}.png'), depth_uint16)

        depth = (depth - depth.min()) / (depth.max() - depth.min()) * 255.0
        depth = depth.astype(np.uint8)

        if args.grayscale:
            depth = np.repeat(depth[..., np.newaxis], 3, axis=-1)
            suffix = '_gray'
        else:
            depth = (cmap(depth)[:, :, :3] * 255)[:, :, ::-1].astype(np.uint8)
            suffix = '_color'

        output_path = os.path.join(args.outdir, f'{os.path.splitext(os.path.basename(filename))[0]}.png')
        # if args.pred_only:
        cv2.imwrite(output_path.replace(".png", f'{suffix}.png'), depth)
        # else:
        split_region = np.ones((raw_image.shape[0], 50, 3), dtype=np.uint8) * 255
        combined_result = cv2.hconcat([raw_image, split_region, depth])

        cv2.imwrite(output_path.replace('.png',  '_combined.png'), combined_result)
