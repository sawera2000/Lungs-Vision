# main.py
import streamlit as st
from streamlit_option_menu import option_menu
#from PIL import Image
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.inception_v3 import preprocess_input
import numpy as np

# Import your modules
import Home
import Account
import Test
from AdditionalInfo import app as AdditionalInfoApp
import Contact
import AboutUs

# st.set_page_config(page_title="Lung Cancer Detection")

class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({
            "title": title,
            "function": func
        })
        
    def run(self):
        with st.sidebar:
            custom_logo_path = 'lun.png'

            # Display the custom logo
            st.image(custom_logo_path, use_column_width=True, width=20)

            app = option_menu(
                menu_title='LungsVision',
                options=[
                    'Account',  # Change the order of pages
                    'Home', 
                    'Test', 
                    'Additional Info', 
                    'Contact',
                    'About Us', 
                ],
                icons=[
                    'clock',  # Use appropriate icon for history
                    'house-fill', 
                    '', 
                    'eye', 
                    'phone',
                    'info-circle-fill', 
                      # Use 'phone' icon for contact
                ],
                menu_icon='hospital',
                default_index=0,
                styles={
                    "container": {"padding": "5px!important", "background-color": 'black'},
                    "icon": {"color": "white", "font-size": "23px"},
                    "nav-link": {"color": "white", "font-size": "16px", "text-align": "left", "margin": "0px",
                                 "--hover-color": "#46B5C5"},
                    "nav-link-selected": {"background-color": "#BC62C3"},
                    
                }
            )
        
        if app == "Home":
            Home.app()
        elif app == "Account":
            Account.app()
        elif app == "Test":
            
            # Test module
            st.title('Lung Cancer Prediction from CT Scan Images')
            uploaded_file = st.file_uploader("Upload a CT scan image", type=["jpg", "jpeg", "png"])

            if uploaded_file is not None:
                # Display the uploaded image
                img = Image.open(uploaded_file)
                st.image(img, caption='Uploaded Image', use_column_width=True)

                # Preprocess the uploaded image
                img = img.resize((224, 224)).convert('RGB')  # Resize and convert to RGB
                img_array = np.array(img)
                img_array = np.expand_dims(img_array, axis=0)
                img_array = preprocess_input(img_array)

                # Generate prediction
                if st.button("Generate Prediction"):
                    prediction = model.predict(img_array)
                    predicted_class = np.argmax(prediction)
                    st.write(f"Prediction: {classes[predicted_class]}")
        elif app == 'Additional Info':
            AdditionalInfoApp(model, classes)
        elif app == 'Contact':
            Contact.app()
        elif app == 'About Us':
            AboutUs.app()
        
# Check for session state change to initiate navigation
        if "app" in st.session_state:
            app = st.session_state.app
            st.session_state.app = None  # Reset session state after navigation
            if app == "Test":
                Test.app()
# Load the model outside of the run method
model = tf.keras.models.load_model("merged_model.h5", compile=False)
# Mapping class indices to labels
classes = [
    "Adenocarcinoma Chest Lung Cancer",
    "Large cell carcinoma Lung Cancer",
    "NO Lung Cancer/ NORMAL",
    "Squamous cell carcinoma Lung Cancer"
]

  # Add Test page with its app() function

# Create an instance of MultiApp and run it
if __name__ == "__main__":
    
    multi_app = MultiApp()
    multi_app.run()

  # Call the Test app within the MultiApp class
