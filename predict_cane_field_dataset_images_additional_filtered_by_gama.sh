#!/bin/bash
RESULTS_DIRPATH="/home/nicolas/SynologyDrive/Rota2030 - Scania/cane_field_dataset/results/"
DEPTH_PREDICTIONS_DIRPATH="predictions/inv_depth/"

python3 run.py --encoder vitl --img-path "${RESULTS_DIRPATH}public_domain/images_additional_filtered_by_gama/flickr.com/" --outdir "${DEPTH_PREDICTIONS_DIRPATH}public_domain/images_additional_filtered_by_gama/flickr.com/" --input-size 1080 --pred-only --save-uint16
python3 run.py --encoder vitl --img-path "${RESULTS_DIRPATH}public_domain/images_additional_filtered_by_gama/Pexels/" --outdir "${DEPTH_PREDICTIONS_DIRPATH}public_domain/images_additional_filtered_by_gama/Pexels" --input-size 1080 --pred-only --save-uint16
python3 run.py --encoder vitl --img-path "${RESULTS_DIRPATH}public_domain/images_additional_filtered_by_gama/pixabay/" --outdir "${DEPTH_PREDICTIONS_DIRPATH}public_domain/images_additional_filtered_by_gama/pixabay" --input-size 1080 --pred-only --save-uint16
python3 run.py --encoder vitl --img-path "${RESULTS_DIRPATH}public_domain/images_additional_filtered_by_gama/rawpixel/" --outdir "${DEPTH_PREDICTIONS_DIRPATH}public_domain/images_additional_filtered_by_gama/rawpixel" --input-size 1080 --pred-only --save-uint16
python3 run.py --encoder vitl --img-path "${RESULTS_DIRPATH}public_domain/images_additional_filtered_by_gama/Unsplash/" --outdir "${DEPTH_PREDICTIONS_DIRPATH}public_domain/images_additional_filtered_by_gama/Unsplash" --input-size 1080 --pred-only --save-uint16
python3 run.py --encoder vitl --img-path "${RESULTS_DIRPATH}public_domain/images_additional_filtered_by_gama/Wikimedia Commons/" --outdir "${DEPTH_PREDICTIONS_DIRPATH}public_domain/images_additional_filtered_by_gama/Wikimedia Commons" --input-size 1080 --pred-only --save-uint16
