import streamlit as st
import firebase_admin
from firebase_admin import auth
from firebase_admin import credentials

cred = credentials.Certificate("lung-cancer-detector-13b7c805766c.json")
#firebase_admin.initialize_app(cred)


def t():
    st.session_state.signout = False
    st.session_state.signedout = False
    st.session_state.username = ''

#st.title('  :violet[Pondering]  :sunglasses:')
def app():
    st.title("Unlocking :violet[Health] Insights")

    if "signedout" not in st.session_state:
        st.session_state.signedout = False

    if "signout" not in st.session_state:
        st.session_state.signout = False

    if not st.session_state["signedout"]:
        choice = st.selectbox('Login/Signup', ['Login', 'Sign up'], key="login_signup_choice")

        if choice == "Login":
            email = st.text_input("Email Address", key="login_email")
            password = st.text_input("Password", type="password", key="login_password")

            def f():
                try:
                    user = auth.get_user_by_email(email)
                    st.success("Login Successful")
                    st.session_state.username = user.uid
                    st.session_state.useremail = user.email
                    st.session_state.signedout = True
                    st.session_state.signout = True

                except:
                    st.warning("Login Failed")

            st.button("Login", on_click=f, key="login_button")

        else:
            email = st.text_input("Email Address", key="signup_email")
            password = st.text_input("Password", type="password", key="signup_password")
            username = st.text_input("Enter your unique username", key="signup_username")

            if st.button("Create My Account", key="create_account_button"):
                user = auth.create_user(email=email, password=password, uid=username)
                st.success("Account created successfully!")
                st.markdown("Please Login with your Email and Password")
                st.balloons()

    if st.session_state.signout:
        st.text('Name ' + st.session_state.username)
        st.text('Email id: ' + st.session_state.useremail)
        if st.button('Sign out', key="signout_button"):
            t()


#app()
