#!/bin/bash
#export CUDA_VISIBLE_DEVICES=1
python3 run.py --encoder vitl --img-path "/home/nicolas/SynologyDrive/Rota2030 - Scania/cane_field_dataset/results/images_additional_filtered_by_gama/flickr.com/" --outdir "predictions/cane_field_dataset_images_additional_filtered_by_gama/flickr.com" --input-size 1080 --pred-only --save-uint16
python3 run.py --encoder vitl --img-path "/home/nicolas/SynologyDrive/Rota2030 - Scania/cane_field_dataset/results/images_additional_filtered_by_gama/Pexels/" --outdir "predictions/cane_field_dataset_images_additional_filtered_by_gama/Pexels" --input-size 1080 --pred-only --save-uint16
python3 run.py --encoder vitl --img-path "/home/nicolas/SynologyDrive/Rota2030 - Scania/cane_field_dataset/results/images_additional_filtered_by_gama/pixabay/" --outdir "predictions/cane_field_dataset_images_additional_filtered_by_gama/pixabay" --input-size 1080 --pred-only --save-uint16
python3 run.py --encoder vitl --img-path "/home/nicolas/SynologyDrive/Rota2030 - Scania/cane_field_dataset/results/images_additional_filtered_by_gama/rawpixel/" --outdir "predictions/cane_field_dataset_images_additional_filtered_by_gama/rawpixel" --input-size 1080 --pred-only --save-uint16
python3 run.py --encoder vitl --img-path "/home/nicolas/SynologyDrive/Rota2030 - Scania/cane_field_dataset/results/images_additional_filtered_by_gama/Unsplash/" --outdir "predictions/cane_field_dataset_images_additional_filtered_by_gama/Unsplash" --input-size 1080 --pred-only --save-uint16
python3 run.py --encoder vitl --img-path "/home/nicolas/SynologyDrive/Rota2030 - Scania/cane_field_dataset/results/images_additional_filtered_by_gama/Wikimedia Commons/" --outdir "predictions/cane_field_dataset_images_additional_filtered_by_gama/Wikimedia Commons" --input-size 1080 --pred-only --save-uint16
