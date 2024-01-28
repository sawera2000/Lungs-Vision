# AdditionalInfo.py
import streamlit as st

def app(model, classes):
    st.title(':violet[Lung Cancer] ')
    st.header("**is a type of cancer that begins in the lungs. It is one of the most common cancers worldwide and a leading cause of cancer-related deaths.**")
    
    # Create two columns layout
    col1, col2 = st.columns([2, 1])

    # Description of Cancer Types in the left column
    with col1:
        st.write("## Lung Cancer Types")

        # Define cancer types and their descriptions
        cancer_types = {
            "Adenocarcinoma Chest Lung Cancer": [
                "Most common type of lung cancer.",
                "Often found in the outer regions of the lungs.",
                "Common in non-smokers."
            ],
            "Large Cell Carcinoma Lung Cancer": [
                "Fast-growing type of lung cancer.",
                "Can appear in any part of the lungs.",
                "Tends to grow and spread quickly."
            ],
            "NO Lung Cancer/ NORMAL": [
                "Indicates a normal result.",
                "Suggests the absence of lung cancer in the provided CT scan."
            ],
            "Squamous Cell Carcinoma Lung Cancer": [
                "Usually arises in the central part of the lungs.",
                "Linked to smoking.",
                "May cause symptoms such as cough and chest pain."
            ]
        }

        # Display descriptions for the selected cancer type
        selected_cancer_type = st.selectbox("Select a Lung Cancer Type:", list(cancer_types.keys()))
        st.write(f"### {selected_cancer_type}")
        for point in cancer_types[selected_cancer_type]:
            st.write(f"- {point}")
