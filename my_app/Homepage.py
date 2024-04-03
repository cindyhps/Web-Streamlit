import streamlit as st

# Set page config
st.set_page_config(
    page_title="Homepage",
    page_icon="🫥",
    layout="centered"
)

# Header
st.image("assets/header_image1.jpg", use_column_width=True)

# Title and sidebar
st.title("Homepage")
st.sidebar.image("assets/logo.jpeg", use_column_width=True)
st.sidebar.success("Cindy - Team2 © 2024")

# Content
st.subheader("Tentang Kami")
st.markdown("""
Merupakan website latihan PCD dan AI. Kami menyediakan berbagai konten hasil dari latihan Studi Independen kami.
""")

# Footer
st.markdown("---")
st.write("Terima kasih telah mengunjungi Homepage kami!")
