import streamlit as st
from PIL import Image
import numpy as np

def rotate_image(image, angle):
    return image.rotate(angle)

def flip_image(image, mode):
    if mode == "Vertikal":
        return image.transpose(Image.FLIP_TOP_BOTTOM)
    elif mode == "Horizontal":
        return image.transpose(Image.FLIP_LEFT_RIGHT)

def main():
    st.title("Rotate and Flip Image")
    st.write("Upload foto yang ingin dirotasi atau flip.")

    # Upload image
    uploaded_file = st.file_uploader("Upload Foto", type=["png", "jpg", "jpeg"], accept_multiple_files=False)

    if uploaded_file is not None:
        # Display uploaded image
        st.image(uploaded_file, caption="Foto yang diupload", use_column_width=True)

        # Load uploaded image
        img = Image.open(uploaded_file)

        # Transformation options
        transform_options = ["Rotasi 90 Derajat Kanan", "Rotasi 90 Derajat Kiri", "Rotasi 180 Derajat", "Flip Vertikal", "Flip Horizontal"]
        transform_choice = st.selectbox("Pilih Transformasi", transform_options)

        # Apply selected transformation
        if transform_choice == "Rotasi 90 Derajat Kanan":
            transformed_img = rotate_image(img, -90)
        elif transform_choice == "Rotasi 90 Derajat Kiri":
            transformed_img = rotate_image(img, 90)
        elif transform_choice == "Rotasi 180 Derajat":
            transformed_img = rotate_image(img, 180)
        elif transform_choice == "Flip Vertikal":
            transformed_img = flip_image(img, "Vertikal")
        elif transform_choice == "Flip Horizontal":
            transformed_img = flip_image(img, "Horizontal")

        # Display transformed image
        st.image(transformed_img, caption=f"Hasil {transform_choice}", use_column_width=True)

if __name__ == "__main__":
    main()
