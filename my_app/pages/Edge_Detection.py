import streamlit as st
import cv2
import numpy as np
from PIL import Image
import os
import base64

def edge_detection(image):
    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Apply Gaussian blur
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    # Apply Canny edge detector
    edges = cv2.Canny(blur, 30, 150)
    return edges

def main():
    st.title("Edge Detection dan HITAMKAN")
    st.write("Cara kerjanya yaitu melakukan generate garis pinggir object yang terdeteksi.")

    # Upload image
    uploaded_file = st.file_uploader("Upload Foto", type=["png", "jpg", "jpeg"], accept_multiple_files=False)

    if uploaded_file is not None:
        # Display uploaded image
        st.image(uploaded_file, caption="Foto yang diupload", use_column_width=True)

        # Convert uploaded image to OpenCV format
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        image = cv2.imdecode(file_bytes, 1)

        # Edge detection
        edges = edge_detection(image)

        # Process image if uploaded
        if uploaded_file:
            # Load uploaded image
            img = Image.open(uploaded_file)

            # Convert PIL Image to numpy array
            img_array = np.array(img)

            # Process image based on selected mode
            processed_img = edge_detection(img_array)

            # Display processed image
            st.image(processed_img, caption=f"Foto dengan mode Edge Detection", use_column_width=True)
            
            # Download processed image
            download_button = st.button("Download Foto")
            if download_button:
                img_filename = f"Edge_Version.jpg"
                save_path = os.path.join("downloaded", img_filename)
                cv2.imwrite(save_path, processed_img)
                st.write(f"Foto telah berhasil diunduh sebagai {img_filename}")
                st.markdown(get_binary_file_downloader_html(save_path, 'Foto'), unsafe_allow_html=True)

# Function to create a download link for files
def get_binary_file_downloader_html(file_path, file_label='File'):
    with open(file_path, 'rb') as f:
        data = f.read()
    b64 = base64.b64encode(data).decode()
    return f'<a href="data:file/jpg;base64,{b64}" download="{os.path.basename(file_path)}">{file_label}</a>'

if __name__ == "__main__":
    main()
