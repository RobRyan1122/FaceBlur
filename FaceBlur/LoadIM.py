import tkinter as tk
from tkinter import filedialog
import cv2

def load_image():
    # Create a temporary root widget for file dialog only
    temp_root = tk.Tk()
    temp_root.withdraw()  # Hide the temporary root window

    file_path = filedialog.askopenfilename()
    if file_path:
        image = cv2.imread(file_path)
        temp_root.destroy()  # Close the temp root after loading the file
        return image

    temp_root.destroy()
    return None

