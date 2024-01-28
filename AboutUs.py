# Contact.py
import streamlit as st

def app():
    
    st.write("Feel free to contact us for any queries or feedback.")

    # Contact Form
    name = st.text_input("Your Name:")
    email = st.text_input("Your Email:")
    message = st.text_area("Your Message:", height=150)

    if st.button("Submit"):
        # Process the submitted form (you can add your logic here)
        st.success("Form submitted successfully!")

    st.write("---")
    st.write("Lung Cancer Detection")
    st.write("Address: LungsVision")
    st.write("Email: contact@lungcancerdetection.com")
