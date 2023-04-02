import streamlit as st
import pymongo

def app():
    if "load_state" not in st.session_state:                    
                                st.session_state.load_state = False 
    def login(username, password):
                                client = pymongo.MongoClient("mongodb+srv://Garv:bcss1972@cluster0.wjgguh1.mongodb.net/?retryWrites=true&w=majority")
                                db = client["mydatabase"]
                                # Check if the user exists and the password matches
                                user = db.Doctors.find_one({"username": username, "password": password})
                                if user:
                                    st.success("Login successful")
                                else:
                                    st.error("Invalid username or password")                            
    with st.form("Login Form"):
            # Set form title
            st.title("Log in to your Account")

             
            st.markdown("")
                                # Full Name
            name = st.text_input("Username",key='fs3e')

                                # Password and Confirm Password
            password1 = st.text_input("Password ", type="password",key='7h91')

            st.markdown("")
                            # global export
                            

            Doc_login=st.form_submit_button("Submit")                # Add validation for form fields
            if Doc_login== True:
                                if len(name.strip()) == 0:
                                    st.error("Please enter your username.")
                                elif len(password1.strip()) <= 7:
                                    st.error("Minimum pass lenght is 8.")
                                else:
                                    
                                    # export_username=username
                                    # Process the form data and create a new user account
                                    login(name,password1)
                                    app.func                        
            

