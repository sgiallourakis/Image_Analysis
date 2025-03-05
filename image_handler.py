# This docoment contains the code associated with uploading large tif files and breaking them
# apart into smaller chucks that are more managable.
import os
import tkinter as tk
from tkinter import simpledialog
import psycopg2
from PIL import Image  # To open image files

def save_image_metadata_to_db(iamge_path, descriptions, file_size, image_width, image_height):


def get_definition(image_path):
    # Create Tkinter window (it will be hidden)
    root = tk.Tk()
    root.withdraw() # Hide the root window

    # Prompt the user to enter a description
    description = simpledialog.askstring("Input", f"Enter description for {os.path.basename(image_path)}", parent=root)

    root.quit() # Close the Tkinter window after input

    return description

# Function to get image file size in bytes
def get_file_size(image_path):
    return os.path.getsize(image_path)

# Function to get image dimensions (width, height)
def get_image_dimensions(image_path):
    with Image.open(image_path) as img:
        return img.size # Return a tuple (widrth, height)

# image_prep will take any images and break it into small pieces (preferably squares)
def image_prep(folder_path):
    # Get the list of image files in the folder
    image_files = [f for f in os.listdir(image_folder) if f.endswith(('.tif', 'png', '.jpg'))]  # Adjust file types as needed

    for image_file in image_files:
        image_path = os.path.join(folder_path, image_file)

        # Get use input for the image description
        description = get_definition(image_path)

        # Get image file size and dimension
        file_size = get_file_size(image_path)
        image_width, image_height = get_image_dimensions(image_path)

        # Process the image (e.g., store the description in the database, or any other operation)
        print(f"Processing image: {image_file}")
        print(f"Description: {description}")
        print(f"File size: {file_size} bytes")
        print(f"Dimensions: {image_width} x {image_height} pixels")

        # Store the metadata in the database
        save_image_metadata_to_db(image_path, description, file_size, image_width, image_height)
