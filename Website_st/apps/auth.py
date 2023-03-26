import streamlit as st
import pymongo
from flask import redirect
def Verification():
    def signup(username, password, email):
        # Initialize MongoDB client and database
        client = pymongo.MongoClient("mongodb+srv://Garv:bcss1972@cluster0.wjgguh1.mongodb.net/?retryWrites=true&w=majority")
        db = client["mydatabase"]
        # Check if the user already exists
        existing_user = db.users.find_one({"username": username})
        if existing_user:
            st.error("Username already exists.")
            return "User Alr Exists"

        # Create a new user document
        user = {"username": username, "password": password, "email": email}

        # Insert the user into the "users" collection
        db.users.insert_one(user)
        st.success("Account created successfully!")
        return redirect("https://www.google.com")
        


        # Set page title and favicon
        # st.set_page_config(page_title="Sign Up", page_icon=":key:")

        # Set form title
        st.title("Create an Account")

        # Create a form layout with 2 columns
        col1, col2 = st.columns(2)

        # Add form fields to the first column
        with col1:
            st.markdown("")
            # Full Name
            name = st.text_input("Full Name")

            # Email
            email = st.text_input("Email")

            # Password and Confirm Password
            password = st.text_input("Password", type="password")
            confirm_password = st.text_input("Confirm Password", type="password")

        st.markdown("")

        # Add validation for form fields
        if st.button("Create Account"):
            if len(name.strip()) == 0:
                st.error("Please enter your full name.")
            elif ((len(email.strip()) == 0) or not('.com' in email)):
                st.error("Please enter a vail email address.")
            elif len(password.strip()) <= 7:
                st.error("Minimum pass lenght is 8.")
            elif password != confirm_password:
                st.error("Passwords do not match.")
            else:
                # Process the form data and create a new user account
                signup(name,password, email)

        # Add footer
        st.markdown("---")
        st.write("Already have an account? [Log in](Login)") 
        def login():
            st.write('')

if __name__=='__main__':
        Verification()    