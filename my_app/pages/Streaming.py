# import streamlit as st
# import cv2
# from PIL import Image
# import numpy as np
# import dlib

# # Function to apply face filter
# def apply_face_filter(frame):
#     # Load face detector model
#     detector = dlib.get_frontal_face_detector()

#     # Load landmarks predictor model
#     predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

#     # Detect faces in the frame
#     faces = detector(frame)

#     # Iterate through each detected face
#     for face in faces:
#         # Get facial landmarks
#         landmarks = predictor(frame, face)

#         # Get coordinates of eyes
#         left_eye = (landmarks.part(36).x, landmarks.part(36).y)
#         right_eye = (landmarks.part(45).x, landmarks.part(45).y)

#         # Calculate distance between eyes
#         eye_distance = np.linalg.norm(np.array(left_eye) - np.array(right_eye))

#         # Calculate scale factor for resizing the filter image
#         scale_factor = eye_distance / 180

#         # Load and resize the filter image
#         filter_img = Image.open("filter.png")
#         filter_img = filter_img.resize((int(filter_img.width * scale_factor), int(filter_img.height * scale_factor)))

#         # Calculate position for placing the filter image
#         filter_pos = (int((landmarks.part(27).x + landmarks.part(30).x) / 2 - filter_img.width / 2),
#                       int((landmarks.part(27).y + landmarks.part(30).y) / 2 - filter_img.height / 2))

#         # Overlay the filter image on the frame
#         frame.paste(filter_img, filter_pos, filter_img)

#     return frame

# # Function to apply face recognition
# def apply_face_recognition(frame):
#     # Load pre-trained face detection model
#     face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

#     # Convert frame to grayscale
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#     # Detect faces in the frame
#     faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

#     # Draw rectangle around each face and label emotion
#     for (x, y, w, h) in faces:
#         cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

#     return frame

# def main():
#     st.title("Streaming Video")
#     st.write("Nyalakan video kameramu untuk streaming videonya bekerja.")

#     # Dropdown for selecting option
#     option = st.selectbox("Pilih Mode", ["Video Biasa", "Filter", "Face Recognition"])

#     # Create OpenCV VideoCapture object
#     cap = cv2.VideoCapture(0)

#     # Set video resolution
#     cap.set(cv2.CAP_PROP_FRAME_WIDTH, 900)
#     cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 600)

#     # Read frames from the webcam
#     while True:
#         ret, frame = cap.read()

#         if ret:
#             # Apply selected option
#             if option == "Filter":
#                 frame = apply_face_filter(frame)
#             elif option == "Face Recognition":
#                 frame = apply_face_recognition(frame)

#             # Display the frame
#             st.image(frame, channels="BGR", caption="Streaming Video", use_column_width=True)

#             # Stop the loop if 'Stop' button is clicked
#             if not st.checkbox("Lanjutkan streaming"):
#                 break
#         else:
#             st.warning("Tidak dapat membaca frame dari kamera.")

#     # Release the VideoCapture object
#     cap.release()

# if __name__ == "__main__":
#     main()
