#!/bin/bash
RESULTS_DIRPATH="/home/nicolas/SynologyDrive/Rota2030 - Scania/cane_field_dataset/results/"
INV_DEPTH_PREDICTIONS_DIRPATH="predictions/inv_depth/"

python3 run.py --encoder vitl --img-path "${RESULTS_DIRPATH}public_domain/images_additional_uploaded_on_roboflow/flickr.com/" --outdir "${INV_DEPTH_PREDICTIONS_DIRPATH}cane_field_dataset_images_additional_uploaded_on_roboflow/flickr.com/" --input-size 1080 --pred-only --save-uint16
python3 run.py --encoder vitl --img-path "${RESULTS_DIRPATH}public_domain/images_additional_uploaded_on_roboflow/Pexels/" --outdir "${INV_DEPTH_PREDICTIONS_DIRPATH}cane_field_dataset_images_additional_uploaded_on_roboflow/Pexels" --input-size 1080 --pred-only --save-uint16
python3 run.py --encoder vitl --img-path "${RESULTS_DIRPATH}public_domain/images_additional_uploaded_on_roboflow/pixabay/" --outdir "${INV_DEPTH_PREDICTIONS_DIRPATH}cane_field_dataset_images_additional_uploaded_on_roboflow/pixabay" --input-size 1080 --pred-only --save-uint16
python3 run.py --encoder vitl --img-path "${RESULTS_DIRPATH}public_domain/images_additional_uploaded_on_roboflow/rawpixel/" --outdir "${INV_DEPTH_PREDICTIONS_DIRPATH}cane_field_dataset_images_additional_uploaded_on_roboflow/rawpixel" --input-size 1080 --pred-only --save-uint16
python3 run.py --encoder vitl --img-path "${RESULTS_DIRPATH}public_domain/images_additional_uploaded_on_roboflow/Unsplash/" --outdir "${INV_DEPTH_PREDICTIONS_DIRPATH}cane_field_dataset_images_additional_uploaded_on_roboflow/Unsplash" --input-size 1080 --pred-only --save-uint16
python3 run.py --encoder vitl --img-path "${RESULTS_DIRPATH}public_domain/images_additional_uploaded_on_roboflow/Wikimedia Commons/" --outdir "${INV_DEPTH_PREDICTIONS_DIRPATH}cane_field_dataset_images_additional_uploaded_on_roboflow/Wikimedia Commons" --input-size 1080 --pred-only --save-uint16
