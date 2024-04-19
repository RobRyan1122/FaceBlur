import cv2
import FaceDetection
import LoadIM
from LoadIM import load_image


face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
# Read a PNG image


image = load_image()


# Define the desired maximum width and height for the window
max_width = 800
max_height = 600

# Get the original image dimensions
original_height, original_width = image.shape[:2]

# Calculate the scaling factor for width and height
width_scale = max_width / original_width
height_scale = max_height / original_height

# Choose the minimum scaling factor to maintain aspect ratio
scale = min(width_scale, height_scale)

# Resize the image with the chosen scale
resized_image = cv2.resize(image, None, fx=scale, fy=scale)

FaceDetection.detect_and_draw_faces(resized_image)

# Convert the image to grayscale
#gray_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)
#faces = face_cascade.detectMultiScale(gray_image,1.1,5,)

#for(x,y,w,h) in faces:
  #  cv2.rectangle(resized_image, (x, y), (x+w, y+h), (255, 0, 0), 3)


# Display the image
# Display the resized image in a window with the original aspect ratio
cv2.imshow('Resized Image', resized_image)

cv2.waitKey(0)
cv2.destroyAllWindows()