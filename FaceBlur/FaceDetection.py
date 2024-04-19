import cv2


def detect_and_draw_faces(resized_image):

    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray_image,1.1,4,)

    for(x,y,w,h) in faces:
        #cv2.rectangle(resized_image, (x, y), (x+w, y+h), (255, 0, 0), 3)

        # Pixelate the region of interest (ROI) containing the face
        roi = resized_image[y:y + h, x:x + w]
        pixelated_roi = cv2.resize(roi, (w // 10, h // 10), interpolation=cv2.INTER_NEAREST)
        pixelated_roi = cv2.resize(pixelated_roi, (w, h), interpolation=cv2.INTER_NEAREST)
        resized_image[y:y + h, x:x + w] = pixelated_roi

    #cv2.imshow('Gray Image', gray_image)