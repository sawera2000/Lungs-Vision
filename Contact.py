import streamlit as st
import json
from streamlit_lottie import st_lottie

def app():

    # Create container for top row with two columns
    top_row = st.container()
    with top_row:
        col1, col2 = st.columns([1, 1])

        # Container 1 (Left): Display Hospital Information
        with col1.container():
            st.header("Hospital Information")
            st.write("Lung Cancer Hospital")
            st.write("Address: 123 Medical Street, Cityville, Country")
            st.write("Phone: +123 456 7890")
            st.write("Email: info@lungcancerhospital.com")

        # Container 2 (Right): Display Lottie animation
        with col2.container():
            with open("ani.json", "r") as file:
                lottie_coding = json.load(file)
            st_lottie(lottie_coding, speed=1, reverse=False, loop=True, quality="low", height=300, width=300, key=None)

    # Doctors and Consultants
    st.header("Doctors and Consultants")

    # Row 1
    col1, col2 = st.columns(2)

    # Container 1 (Top Left)
    with col1.container():
        st.write("**Asst. Prof. Dr. Mubeen Ahmed Memon**")
        st.write("Specialization: Pulmonology")
        st.write("Contact: +03111222398")
        st.write("Address: Chest Care Centre, Sindh, Hyderabad")

    # Container 2 (Top Right)
    with col2.container():
        st.write("**Dr. Muhammad Aslam Memon**")
        st.write("Specialization: Oncology")
        st.write("Contact: +03111444398")
        st.write("Address: Dr Zia-ud-Din Road, Cantonmant, Hyderabad, Sindh")

    # Row 2
    col3, col4 = st.columns(2)

    # Container 3 (Bottom Left)
    with col3.container():
        st.write("**Dr. Alex Johnson**")
        st.write("Specialization: Radiology")
        st.write("Contact: +111 222 3333")
        st.write("Address: Amar Medical & Diagnostic Center Infront Fatima Heights & Mahesh Pathology Laboratary, Saddar, Hyderabad")

    # Container 4 (Bottom Right)
    with col4.container():
        st.write("**Assoc. Prof. Dr. Afsheen Qazi**")
        st.write("Specialization: Pathology")
        st.write("Contact: +444 555 6666")
        st.write("Address: Noor Pathology Laboratory, Saddar, Hyderabad")

    st.write("---")

    st.write("For Consultations and Appointments, please contact our front desk.")

    st.write("---")

    st.write("Lung Cancer Detection")
    st.write("LungsVision")
    st.write("Email: contact@lungcancerdetection.com")




