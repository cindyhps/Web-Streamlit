import streamlit as st
import cv2
import numpy as np
from PIL import Image
import io
import os

def histogram_matching(source, target):
    source = np.array(source)
    target = np.array(target)

    # Convert to grayscale if the image is colored
    if len(source.shape) > 2 and source.shape[2] > 1:
        source = cv2.cvtColor(source, cv2.COLOR_RGB2GRAY)

    if len(target.shape) > 2 and target.shape[2] > 1:
        target = cv2.cvtColor(target, cv2.COLOR_RGB2GRAY)

    # Perform histogram matching
    matched_image = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8)).apply(source)

    return Image.fromarray(matched_image)

def main():
    st.title("Histogram Matching")
    st.write("Upload fotomu dengan mode grayscale atau binary (mode hitam putih)")

    # Upload grayscale or binary image
    grayscale_image = st.file_uploader("Upload Grayscale/Binary Image", type=["png", "jpg", "jpeg"], accept_multiple_files=False)

    if grayscale_image is not None:
        # Convert image to PIL format
        grayscale_img = Image.open(grayscale_image)

        # Display grayscale or binary image
        st.image(grayscale_img, caption="Grayscale/Binary Image", use_column_width=True)

        # Upload color reference image
        color_reference_image = st.file_uploader("Upload Color Reference Image", type=["png", "jpg", "jpeg"], accept_multiple_files=False)

        if color_reference_image is not None:
            # Convert reference image to PIL format
            color_reference_img = Image.open(color_reference_image)

            # Perform histogram matching
            colorized_img = histogram_matching(grayscale_img, color_reference_img)

            # Convert image to CMYK
            colorized_img = colorized_img.convert("CMYK")

            # Convert CMYK to RGB for display
            colorized_img = colorized_img.convert("RGB")

            # Display images side by side for comparison
            col1, col2 = st.columns(2)
            with col1:
                st.subheader("Original Image")
                st.image(grayscale_img, use_column_width=True)

            with col2:
                st.subheader("Colorized Image")
                st.image(colorized_img, use_column_width=True)

            # Download colorized image
            download_button = st.button("Download Colorized Image")
            if download_button:
                # Convert the colorized image to bytes
                image_bytes = io.BytesIO()
                colorized_img.save(image_bytes, format='JPEG')
                image_bytes = image_bytes.getvalue()

                # Create 'downloaded' folder if it doesn't exist
                if not os.path.exists("downloaded"):
                    os.makedirs("downloaded")

                # Save the image to 'downloaded' folder
                with open("downloaded/Colorized_Image.jpg", "wb") as f:
                    f.write(image_bytes)

                # Offer the file download
                st.download_button(
                    label="Download",
                    data=image_bytes,
                    file_name="Colorized_Image.jpg",
                    mime="image/jpeg"
                )

if __name__ == "__main__":
    main()
