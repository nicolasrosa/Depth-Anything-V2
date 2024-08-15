# --- Libraries
from modules.utils import read_json
import cv2
from matplotlib import pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
from icecream import ic

# --- Global variables
# Select the affine-invariant inverse depth prediction image to display
# IMG_INV_DEPTH_FILEPATH = 'predictions/cane_field_dataset/inv_depth/batch_0/IMG_1229_0011_uint16.png'
# IMG_INV_DEPTH_FILEPATH = 'predictions/lasi_images/inv_depth/carro_5m_uint16.png'
IMG_INV_DEPTH_FILEPATH = 'predictions/lasi_images/inv_depth/placa_5m_uint16.png'

IMG_METRIC_DEPTH_FILEPATH = IMG_INV_DEPTH_FILEPATH.replace('inv_depth', 'metric_depth')

UINT16_SCALE_FACTOR = read_json('uint16_scale_factor.json')

INV_DEPTH_TO_METRIC_DEPTH_SCALE_FACTOR = 1590.  # LASI, Scale factor to convert inverse depth to metric depth
MAX_DEPTH = 40.0  # KITTI dataset maximum depth value
# ---


def show_depth_image(img, title):
    plt.figure()
    ax = plt.gca()
    im = ax.imshow(img, cmap='gray')
    plt.title(title)

    # create an axes on the right side of ax. The width of cax will be 5%
    # of ax and the padding between cax and ax will be fixed at 0.05 inch.
    divider = make_axes_locatable(ax)
    cax = divider.append_axes("right", size="5%", pad=0.05)

    plt.colorbar(im, cax=cax)


def read_depth_image(filepath, type_depth):
    # Read 'affine-invariant inverse' or 'metric' depth image
    print("Reading inverse depth image...")
    img_depth_uint16 = cv2.imread(filepath, cv2.IMREAD_UNCHANGED)
    ic(img_depth_uint16.shape, img_depth_uint16.dtype, img_depth_uint16.min(), img_depth_uint16.max())

    # Use the scale factor to retrieve the original disparity values
    img_depth = img_depth_uint16 / UINT16_SCALE_FACTOR[type_depth]
    ic(img_depth.shape, img_depth.dtype, img_depth.min(), img_depth.max())

    return img_depth


def main():
    """ Notes
    In the context of the "Depth Anything" papers, "affine-invariant inverse depth" is not the same as disparity,
    although they are related concepts.

    Disparity refers to the difference in image location of an object viewed from two different angles (in stereo
    vision). It is a measure used to compute depth from stereo image pairs.

    Affine-invariant inverse depth, on the other hand, is a depth representation that is invariant to affine
    transformations. In simpler terms, it’s a way of encoding depth that remains consistent even if the scene undergoes
    certain transformations, such as scaling or rotation.

    The "inverse depth" itself is a reciprocal of depth, so it represents depth as 1/depth1/depth. The affine-invariance
    aspect ensures that this depth representation is robust to transformations that might otherwise affect the depth
    perception.

    In summary, while disparity is directly related to depth perception in stereo vision, affine-invariant inverse depth
    is a more abstract depth representation designed to be robust under various transformations.
    """

    # Read affine-invariant inverse depth prediction image
    img_pred_inv_depth = read_depth_image(IMG_INV_DEPTH_FILEPATH, 'inv_depth')

    # Read the metric depth image
    img_pred_metric_depth = read_depth_image(IMG_METRIC_DEPTH_FILEPATH, 'metric_depth')
    ic(img_pred_metric_depth.shape, img_pred_metric_depth.dtype, img_pred_metric_depth.min(), img_pred_metric_depth.max())

    # FIXME: Na verdade, o que a rede prediz é relative depth, não necessariamente disparidade.
    # Convert inverse depth to metric depth
    # img_gt_depth = (1./img_pred_inv_depth)*DISP2DEPTH_SCALE_FACTOR
    # img_gt_depth[img_gt_depth > MAX_DEPTH] = MAX_DEPTH
    # ic(img_gt_depth.shape, img_gt_depth.dtype, img_gt_depth.min(), img_gt_depth.max())

    # Display the disparity image
    show_depth_image(img_pred_inv_depth, "Predicted Inverse Depth image")
    show_depth_image(img_pred_metric_depth, "Predicted Metric Depth image")
    # show_depth_image(img_gt_depth, "Ground Truth Depth image (meters)")
    plt.show()

    print("\nDone!")


if __name__ == "__main__":
    main()
