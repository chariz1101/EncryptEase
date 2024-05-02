import streamlit as st
from cryptography.fernet import Fernet
import pages

st.title("EncryptEase") 
st.subheader("Encryption:") 

def encrypt_file(file_obj, f): #define function to call encryptions
  data = file_obj.read()  # Read the file content as bytes
  encrypted_data = f.encrypt(data)
  return encrypted_data

key = Fernet.generate_key() #key generation for encryption
f = Fernet(key) 
  
uploaded_file = st.file_uploader("Choose a file to encrypt")   

if uploaded_file is not None:
  try:
    encrypted_data = encrypt_file(uploaded_file, f) # for storing or display the encrypted data
    st.success("File encrypted successfully!")
  except Exception as e: #used except to avoid crashes during failed encryption
    st.error(f"Encryption failed: {e}")

if uploaded_file is None:
    disable_button = True  # Button is disabled if no file is uploaded
else:
    disable_button = False  # Button is enabled if file is uploaded

if uploaded_file:
    st.download_button("Download Encrypted File", encrypted_data, file_name="encrypted_file.txt")

st.markdown("---")
st.subheader("Download key here")
st.download_button("Download Key", key, file_name="encryption_key.key")
