#!/usr/bin/python3
from pdf2image import convert_from_path
from PIL import Image
from tkinterdnd2 import DND_FILES, TkinterDnD
import tkinter as tk
import os
import sys
print(sys.path)

# Function to convert an image JPG to WebP
def convert_image_to_webp(input_path, output_path, quality=80):
    with Image.open(input_path) as img:
        img.save(output_path, 'webp', quality=quality)

# Function to convert a PDF to WebP
def convert_pdf_to_webp(input_path, output_path, quality=80):
    images = convert_from_path(input_path)
    images[0].save(output_path, 'webp', quality=quality)

# Function to convert a PNG to WebP
def convert_png_to_webp(input_path, output_path, quality=80):
    with Image.open(input_path) as img:
        img = img.convert("RGB")  # Convert to RGB mode (WebP requires RGB)
        img.save(output_path, 'webp', quality=quality)


def on_drop(output_folder, event):
    try:
        result_label.config(text="")  # Clear the result_label text

        file_paths = root.tk.splitlist(event.data)
        quality = quality_slider.get()

        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        for file_path in file_paths:
            # Check if the file is an image (JPG, PNG) or a PDF
            if file_path.lower().endswith(('.jpg', '.jpeg')):
                convert_image_to_webp(file_path, os.path.join(output_folder, os.path.basename(
                    file_path).replace('.jpg', '.webp')), quality=quality)
            elif file_path.lower().endswith(('.png')):
                convert_png_to_webp(file_path, os.path.join(output_folder, os.path.basename(
                    file_path).replace('.png', '.webp')), quality=quality)
            elif file_path.lower().endswith('.pdf'):
                convert_pdf_to_webp(file_path, os.path.join(output_folder, os.path.basename(
                    file_path).replace('.pdf', '.webp')), quality=quality)

        result_label.config(text="Conversion complete!")
    except Exception as e:
        result_label.config(text=f"Error: {str(e)}")


# Create the main application window
root = TkinterDnD.Tk()
root.title("JPG to WebP Converter")

# Calculate the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate the center coordinates
x_center = (screen_width - 600) // 2
y_center = (screen_height - 400) // 2

# Set the geometry to open in the center of the screen
root.geometry(f"600x400+{x_center}+{y_center}")

# Create and configure the input label
input_label = tk.Label(
    root, text="Drag and drop JPG, PNG, or PDF images here:")
input_label.pack(pady=10)

# Create the drop target
drop_target = tk.Listbox(root, selectmode=tk.SINGLE, width=40, height=10)
drop_target.pack()

drop_target.drop_target_register(DND_FILES)
drop_target.dnd_bind('<<Drop>>', lambda event: on_drop(
    "/Users/1willcobb/desktop", event))

# Create and configure the quality slider
quality_label = tk.Label(root, text="Quality:")
quality_label.pack()

quality_slider = tk.Scale(root, from_=0, to=100, orient="horizontal")
quality_slider.set(80)  # Set the default quality value
quality_slider.pack()

# Create and configure the result label
result_label = tk.Label(root, text="")
result_label.pack()

# Start the tkinter main loop
root.mainloop()
