import streamlit as st


def app():
    # Create the first set of columns with spacing
    col1, col2 = st.columns([1, 5])
    st.write("")  # Add vertical space between logo/title and other content

    # Display the logo image in the first column
    logo_path = 'lun.png'  # Replace with your logo path
    col1.image(logo_path, use_column_width=True, width=100)

    # Set the title and text in the second column
    with col2:
        st.title("Welcome to Lung Cancer Detector")
    col3, col4 = st.columns([1, 1])
    with col3:
        st.markdown("- Early detection significantly improves survival rates,"
                    " Treatment options are constantly advancing,"
                    " Many people with lung cancer live long and fulfilling lives.")
        st.markdown("- Breath by breath, step by step, we stand united against lung cancer. ")
        st.markdown("- join our community and let's create a world without limits.")          
    # Create a new row for the images and text
    st.write("")  # Add vertical space below the text

    # Display the image in the third column
    image_path = 'pic.png'  # Replace with your image path
    col4.image(image_path, use_column_width=False, width=200)

   
   

