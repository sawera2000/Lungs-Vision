import streamlit as st
from streamlit_option_menu import option_menu
#from PIL import Image
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.inception_v3 import preprocess_input
import numpy as np

def app():
    st.title('Lung Cancer Prediction from CT Scan Images')
           
        # Lung Cancer Prediction section
    uploaded_file = st.file_uploader("Upload a CT scan image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        
        # Display the uploaded image
        img = Image.open(uploaded_file)
        st.image(img, caption='Uploaded Image', use_column_width=True)

        # Preprocess the uploaded image
        img = img.resize((224, 224)).convert('RGB')
        img_array = np.array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array = preprocess_input(img_array)

        # Generate prediction
        if st.button("Generate Prediction"):
            prediction = model.predict(img_array)
            predicted_class = np.argmax(prediction)
            st.write(f"Prediction: {classes[predicted_class]}")

    