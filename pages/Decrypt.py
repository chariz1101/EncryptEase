import streamlit as st
from cryptography.fernet import Fernet

st.title("EncryptEase") 
st.subheader("Decryption:") 

key = st.file_uploader("Upload encryption key (.key file)", type="key")

uploaded_file = st.file_uploader("Choose a file to decrypt")

if key and uploaded_file:
    try:
        f = Fernet(key.read())
        decrypted_data = f.decrypt(uploaded_file.read())  # Decrypt the uploaded file
        st.success("File decrypted successfully!")
    except Exception as e:
        st.error(f"Decryption failed: {e}")

if uploaded_file:
    if 'decrypted_data' in locals():  # Check if decrypted_data is defined
        st.download_button("Download Decrypted File", decrypted_data, file_name="decrypted_file.txt")
