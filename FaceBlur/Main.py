import cv2
import os
import tkinter as tk
from tkinter import filedialog
import FaceDetection

# Hide the main Tk window
tk.Tk().withdraw()

# Let the user select a folder
folder_path = filedialog.askdirectory(title="Select Folder with Images")

if not folder_path:
    print("No folder selected.")
    exit()

# Output folder
output_folder = os.path.join(folder_path, "processed")
os.makedirs(output_folder, exist_ok=True)

# Valid image extensions
valid_exts = [".jpg", ".jpeg", ".png", ".bmp"]

# Loop through all images in the folder
for filename in os.listdir(folder_path):
    if any(filename.lower().endswith(ext) for ext in valid_exts):
        image_path = os.path.join(folder_path, filename)
        image = cv2.imread(image_path)

        if image is None:
            print(f"Could not load {filename}")
            continue

        # Resize logic
        max_width = 800
        max_height = 600
        original_height, original_width = image.shape[:2]
        width_scale = max_width / original_width
        height_scale = max_height / original_height
        scale = min(width_scale, height_scale)
        resized_image = cv2.resize(image, None, fx=scale, fy=scale)

        # Apply face detection + pixelation
        FaceDetection.detect_and_draw_faces(resized_image)

        # Save processed image
        output_path = os.path.join(output_folder, f"blurred_{filename}")
        cv2.imwrite(output_path, resized_image)
        print(f"Processed: {filename}")

print("Done.")
