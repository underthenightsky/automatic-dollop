import streamlit as st
import pymongo
from flask import redirect
export_username=''
def Verification(): 
                if "load_state" not in st.session_state:
                                                    
                                st.session_state.load_state = False                                
                if len(export_username)!=0:
                      
                      return  st.warning('You are already registered. ')
                else :
                        pass     
                  
                                                   
                
                def signup(username,name, password, email, age, gender, Weight, Height, History):
                       
                        # Initialize MongoDB client and database
                        client = pymongo.MongoClient("mongodb+srv://Garv:bcss1972@cluster0.wjgguh1.mongodb.net/?retryWrites=true&w=majority")
                        db = client["mydatabase"]
                    # Check if the user already exists
                        existing_user = db.users.find_one({"username": username})
                        if existing_user:
                            st.error("Username already exists.")
                            return "User Alr Exists"
                        username_global=username
                        # Create a new user document
                        user = {"username": username, "password": password, "email": email, "name": name,"age": age,"gender": gender, "Weight": Weight, "Height": Height, "MedicalHistory": History}

                        # Insert the user into the "users" collection
                        db.users.insert_one(user)
                        st.success("Account created successfully!")
                        redirect("https://www.google.com")
                        


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
                        # Username
                        username = st.text_input("Username")
                        # Email
                        email = st.text_input("Email")

                        # Password and Confirm Password
                        password = st.text_input("Password", type="password")
                        confirm_password = st.text_input("Confirm Password", type="password")

                with col2:
                        st.markdown("")
                        # Age
                        age = st.text_input("Age")
                        options = ["Male", "Female"]
                        gender = st.selectbox("Select your gender", options)
                        # Weight
                        Weight = st.text_input("Weight")
                        # Height
                        Height = st.text_input("Height")
                        # options = ["HyperTension", "Hypotension", "High Sugar", "Cancer"]
                        medicalIssues = st.Text_imput("Any Serious Medical Issues or Allergies?")
                st.markdown("")
                
                export_username=username
            
                    # Add validation for form fields
                if st.button("Create Account"):
                        if len(name.strip()) == 0:
                            st.error("Please enter your full name.")
                        if len(username.strip()) == 0:
                            st.error("Please enter your username.")
                        if len(age.strip()) == 0:
                            st.error("Please enter your age.")
                        if len(Weight.strip()) == 0:
                            st.error("Please enter your Weight.")
                        if len(Height.strip()) == 0:
                            st.error("Please enter your Height.")
                        elif ((len(email.strip()) == 0) or not('.com' in email)):
                            st.error("Please enter a vail email address.")
                        elif len(password.strip()) <= 7:
                            st.error("Minimum pass lenght is 8.")
                        elif password != confirm_password:
                            st.error("Passwords do not match.")
                        else:
                            # Process the form data and create a new user account
                            signup(username,name,password, email, age, gender, Weight, Height, medicalIssues)
                        
                if st.button("Already have an account ? Login",key='7') or st.session_state.load_state:                     
                            st.session_state.load_state=True
                           
                            def login(username, password):
                                client = pymongo.MongoClient("mongodb+srv://Garv:bcss1972@cluster0.wjgguh1.mongodb.net/?retryWrites=true&w=majority")
                                db = client["mydatabase"]
                                # Check if the user exists and the password matches
                                user = db.users.find_one({"username": username, "password": password})
                                if user:
                                    st.success("Login successful")
                                else:
                                    st.error("Invalid username or password")
                            # Set page title and favicon
                    #st.set_page_config(page_title="Log In", page_icon=":key:")

                            # Set form title
                            st.title("Log in to your Account")

                            # Create a form layout with 2 columns
                            col1, col2 = st.columns(2)

                            # Add form fields to the first column
                            with col1:
                                st.markdown("")
                                # Full Name
                                name = st.text_input("Username",key='jdj5')

                                # Password and Confirm Password
                                password1 = st.text_input("Password ", type="password",key='7hy')

                            st.markdown("")
                            # global export
                            export_username=username

                            # Add validation for form fields
                            if st.button("Login"):
                                if len(name.strip()) == 0:
                                    st.error("Please enter your username.")
                                elif len(password1.strip()) <= 7:
                                    st.error("Minimum pass lenght is 8.")
                                else:
                                    # Process the form data and create a new user account
                                    login(name,password1)
    
            

def LoginUI():
            
        
                    
                if "load_state" not in st.session_state:
                        st.session_state.load_state = False
                if len(export_username)!=0:
                      
                      return  st.warning('You are already registered. ')
                else :
                      pass       
               
                def login(username, password):
                    client = pymongo.MongoClient("mongodb+srv://Garv:bcss1972@cluster0.wjgguh1.mongodb.net/?retryWrites=true&w=majority")
                    db = client["mydatabase"]
                    # Check if the user exists and the password matches
                    user = db.users.find_one({"username": username, "password": password})
                    if user:
                        # global export
                        export_username=username
                        st.success("Login successful")
                    else:
                        st.error("Invalid username or password")
            


                # Set page title and favicon
                #st.set_page_config(page_title="Log In", page_icon=":key:")

                # Set form title
                st.title("Log in to your Account")

                # Create a form layout with 2 columns
                col1, col2 = st.columns(2)

                # Add form fields to the first column
                with col1:
                    st.markdown("")
                    # Full Name
                    name = st.text_input("Username",key='8djj')

                    # Password and Confirm Password
                    password1 = st.text_input("Password ", type="password",key='9d9jo')

                st.markdown("")

                # Add validation for form fields
                if st.button("Login"):
                    if len(name.strip()) == 0:
                        st.error("Please enter your username.")
                    elif len(password1.strip()) <= 7:
                        st.error("Minimum pass lenght is 8.")
                    else:
                        # Process the form data and create a new user account
                        login(name,password1)

                # Add footer
                st.markdown("---")
                
                if st.button("Want to create a new account ? Click here to Sign Up",key='ap29aq') or st.session_state.load_state:
                    st.session_state.load_state = True
                    def signup(username,name, password, email, age, gender, Weight, Height, History):    
                        client = pymongo.MongoClient("mongodb+srv://Garv:bcss1972@cluster0.wjgguh1.mongodb.net/?retryWrites=true&w=majority")
                        db = client["mydatabase"]
                    # Check if the user already exists
                        existing_user = db.users.find_one({"username": username})
                        if existing_user:
                            st.error("Username already exists.")
                            return "User Alr Exists"

                        # Create a new user document
                        user = {"username": username, "password": password, "email": email, "name": name,"age": age,"gender": gender, "Weight": Weight, "Height": Height, "MedicalHistory": medicalIssues}

                        # Insert the user into the "users" collection
                        db.users.insert_one(user)
                        st.success("Account created successfully!")
                        redirect("https://www.google.com")
                        


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
                            name = st.text_input("Full Name",key='l1')
                            # Username
                            username = st.text_input("Username",key='loo')
                            # Email
                            email = st.text_input("Email")

                            # Password and Confirm Password
                            password = st.text_input("Password", type="password",key='l2')
                            confirm_password = st.text_input("Confirm Password", type="password",key='l3')

                    with col2:
                            st.markdown("")
                            # Age
                            age = st.text_input("Age")
                            options = ["Male", "Female",'Other']
                            gender = st.selectbox("Select your gender", options)
                            # Weight
                            Weight = st.text_input("Weight(in KG)")
                            # Height
                            Height = st.text_input("Height(in cms)")
                            # options = ["HyperTension", "Hypotension", "High Sugar", "Cancer"]
                            medicalIssues = st.text_input("Any Serious Medical Issues?")
                    st.markdown("")
                    # global export
                    export_username=username

                        # Add validation for form fields
                    if st.button("Create Account"):
                            if len(name.strip()) == 0:
                                st.error("Please enter your full name.")
                            if len(username.strip()) == 0:
                                st.error("Please enter your username.")
                            if len(age.strip()) == 0:
                                st.error("Please enter your age.")
                            if len(Weight.strip()) == 0:
                                st.error("Please enter your Weight.")
                            if len(Height.strip()) == 0:
                                st.error("Please enter your Height.")
                            elif ((len(email.strip()) == 0) or not('.com' in email)):
                                st.error("Please enter a vail email address.")
                            elif len(password.strip()) <= 7:
                                st.error("Minimum pass lenght is 8.")
                            elif password != confirm_password:
                                st.error("Passwords do not match.")
                            else:
                                # Process the form data and create a new user account
                                Verification.signup(username,name,password, email, age, gender, Weight, Height, medicalIssues)
                        
                # if st.button("Already have an account ? Login",key='7') or st.session_state.load_state:
                            
                            
                            
                #             st.session_state.load_state=True
                #             def login(username, password):
                #                     client = pymongo.MongoClient("mongodb+srv://Garv:bcss1972@cluster0.wjgguh1.mongodb.net/?retryWrites=true&w=majority")
                #                     db = client["mydatabase"]
                #                     # Check if the user exists and the password matches
                #                     user = db.users.find_one({"username": username, "password": password})
                #                     if user:
                #                         st.success("Login successful")
                #                     else:
                #                         st.error("Invalid username or password")
                #                 # Set page title and favicon
                #         #st.set_page_config(page_title="Log In", page_icon=":key:")

                #                 # Set form title
                #             st.title("Log in to your Account")

                #                 # Create a form layout with 2 columns
                #             col1, col2 = st.columns(2)

                #                 # Add form fields to the first column
                #             with col1:
                #                     st.markdown("")
                #                     # Full Name
                #                     name = st.text_input("Username")

                #                     # Password and Confirm Password
                #                     password1 = st.text_input("Password ", type="password")

                #             st.markdown("")

                #                 # Add validation for form fields
                #             if st.button("Login"):
                #                     if len(name.strip()) == 0:
                #                         st.error("Please enter your username.")
                #                     elif len(password1.strip()) <= 7:
                #                         st.error("Minimum pass lenght is 8.")
                #                     else:
                #                         # Process the form data and create a new user account
                #                         login(name,password1)

                    
if __name__=='__main__':
                Verification   
