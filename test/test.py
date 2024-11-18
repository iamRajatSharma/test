from PIL import Image
from surya_functions import get_image_text
import os

def main():

    folder_path = 'source'  # Replace with your folder path

    # Get a list of all files in the folder
    files = os.listdir(folder_path)

    # Filter out the .png files
    png_files = [f for f in files if f.lower().endswith('.png')]

    # print(png_files)
    for img in png_files:
        split_img = img.split(".")
        text_file = split_img[0]+".txt"
        
        extracted_text = get_image_text("source/"+img)

        f = open("source/"+text_file, "a")
        for text in extracted_text:
            # print(text)
            f.write(text)
            f.write("\n")

if __name__ == "__main__":
    main()