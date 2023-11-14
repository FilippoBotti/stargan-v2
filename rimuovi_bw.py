import os
import imageio.v2 as imageio
import numpy as np

# Define the directory containing the processed images
input_directory = "/Users/filippo/Desktop/università/laurea/tesi/datasets/horse2zebra/train/horse"

# List all image files in the input directory
image_files = os.listdir(input_directory)

for img_file in image_files:
    # Construct the full image file path
    img_path = os.path.join(input_directory, img_file)

    # Load the image using imageio
    img = imageio.imread(img_path)
    # Check if the image has the desired shape [3, 256, 256]
    if img.shape == (256, 256, 3):
        # If the shape is correct, you can keep the image
        continue
    else:
        # If the shape is not correct, delete the image
        print(img_path)
        os.remove(img_path)
