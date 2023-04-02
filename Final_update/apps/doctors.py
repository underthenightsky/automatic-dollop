import streamlit as st
import pandas as pd
import os
import pymongo

import json
import time
import requests
import jwt
export_username_1=''
from apps import auth

import time

def app():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://images.unsplash.com/photo-1585435557343-3b092031a831?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8M3x8bWVkaWNhbCUyMGJhY2tncm91bmR8ZW58MHx8MHx8&auto=format&fit=crop&w=500&q=60");
             background-attachment: fixed;
            #  height: 650px;
            #  width: 1519px;
             background-size: 99% ;
             background-repeat:no-repeat;
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
    # export_username_1=auth.export_username
    if "load_state" not in st.session_state:
          st.session_state.load_state = False 
    auth.export_username=export_username_1                                                   
                                
    # Set page title and favicon
    # st.set_page_config(page_title='Find a Doctor',page_icon=':hospital:')
    new_path="C:/Users/1/Downloads/doctor_app-master/doctor_app-master/Final_update/apps/doctors_names.csv"
    # if os.path.exists(new_path):
    #      os.chdir(new_path)
    doctors_df = pd.read_csv(new_path)
    # else :    
    # # # Load data
    #     doctors_df = pd.read_csv(f'{os.getcwd()}/doctors_names.csv')
    
    # Define page layout
    st.title('Doctor Finder')
    st.write('')
    # Create navigation bar

    # Show appropriate page based on selection
    st.sidebar.title('Filter Doctors')
    Department_1 = st.sidebar.multiselect('Select Department', doctors_df['Department'].explode().unique())

    # Filter data
    filtered_df = doctors_df[doctors_df['Department'].apply(lambda x: any(item for item in Department_1 if item in x))]

    # Display results
    if len(filtered_df) == 0:
        st.warning('Please select a department.')
    else:
        for index, row in filtered_df.iterrows():
            st.image(row['Image'], width=250)
            st.write(f"## {row['Name']} ({row['Specialty']})")
            st.write(f"Address: {row['Address']}")
            st.write(f"Phone: {row['Phone']}")
            st.write(f"Experience: {row['XP']} years")
            st.write('---')
    if len(filtered_df)>1:
          st.error("Please chose only one doctor at a time.")
    auth.export_username=export_username_1  
    # while True :
            
    if len(filtered_df) == 1:
            
            if len(auth.export_username)==0:                 
                   st.error("Please Log in or Sign up to consult a doctor.")
            else:     
                if st.button("Click here to consult") or st.session_state.load_state:
                    st.session_state.load_state=True
                    cluster=pymongo.MongoClient('mongodb+srv://Garv:bcss1972@cluster0.wjgguh1.mongodb.net/?retryWrites=true&w=majority')
                    db=cluster['mydatabase']
                    results=db.users.find_one({"username":auth.export_username})
                    
                    with st.form('Doc_Consult_form'):

                            st.header("Doctors Consultation Form")
                            st.write('Please fill up this form')
                            col1,col2=st.columns(2)
                            with col1:
                                st.markdown('')
                                fullname=st.text_input('Fullname',f"{results['name']}",placeholder='Please fill up this section')
                                age=st.text_input('Age',f"{results['age']}",placeholder='Please fill up this section')
                                weight=st.text_input('Weight (in Kg)',f"{results['Weight']}",placeholder='Please fill up this section')
                            with col2:
                                st.markdown('')
                                gender=st.text_input('Gender',f"{results['gender']}",placeholder='Please fill up this section')
                                height=st.text_input('Height (in cms)',f"{results['Height']}",placeholder='Please fill up this section')
                                medical_issues=st.text_input("Medical Issues or Allergies",f"{results['MedicalHistory']}",placeholder='Please fill up this section')
                            Issue_concise_Description=st.text_input("What is your ailment ?",placeholder='Please fill up this section')
                            Issue_Time=st.text_input("How long ago did you notice this issue ?",placeholder='Please fill up this section')
                            Issue_Description=st.text_area("Please Describe your issue :",placeholder='Please fill up this section')                     
                            # st.success("Form Submitted successfully!")
                            submission=st.form_submit_button("Submit")
                            if submission==True:
                                if (len(fullname)==0 or len(age)==0 or len(weight)==0 or len(gender)==0 or len(height)==0 or len(medical_issues)==0 or len(Issue_concise_Description)==0 or len(Issue_Time)==0 or len(Issue_Description)==0):
                                      st.error('Please fill up all the required sections')
                                else :
                                    # doctors.export_username_1=username      
                                    user = {"username": results['username'], "password": results['password'], "email": results['email'], "name": results['name'],"age": results['age'],"gender": results['gender'], "Weight": results['Weight'], "Height": results['Height'], "MedicalHistory": results['MedicalHistory'],'Issue_concise_Description':Issue_concise_Description,'Issue_Time':Issue_Time,'Issue_Description':Issue_Description}
                                    db.users.delete_many({"username":f"{results['username']}"})
                                    db.users.insert_one(user)
                                    st.write('Form submitted successfully.')
                                    # consult_1(user.values())
                                    cluster.close()
                                    API_Key='0SZo9tEORY6P9YL0OB_Aqw'
                                    API_Secret='EJiUtzqPUW4cJ4t7jT93I92WLoIx31UIVOIx'
                                    def generateToken():
                                        token = jwt.encode(
                                    
                                            # Create a payload of the token containing
                                            # API Key & expiration time
                                            {'iss': API_Key, 'exp': time.time() + 5000},
                                    
                                            # Secret used to generate token signature
                                            API_Secret,
                                    
                                            # Specify the hashing alg
                                            algorithm='HS256'
                                        )
                                        # new_token=jwt.decode(token,key=API_Secret, algorithms=['HS256'])
                                        return token
                                        
                                    
                                    
                                    # create json data for post requests
                                    meetingdetails = {"topic": "Doctors Consultation",
                                                    "type": 2,
                                                    "start_time": "2019-06-14T10: 21: 57",
                                                    "duration": "45",
                                                    "timezone": "Asia",
                                                    "agenda": "test",
                                    
                                                    "recurrence": {"type": 1,
                                                                    "repeat_interval": 1
                                                                    },
                                                    "settings": {"host_video": "true",
                                                                "participant_video": "true",
                                                                "join_before_host": "False",
                                                                "mute_upon_entry": "False",
                                                                "watermark": "true",
                                                                "audio": "voip",
                                                                "auto_recording": "cloud"
                                                                }
                                                    }
                                    
                                    # send a request with headers including
                                    # a token and meeting details
                                    def getUsers():
                                        headers = {'authorization': 'Bearer %s' % generateToken(),
                                                'content-type': 'application/json'}

                                        r = requests.get('https://api.zoom.us/v2/users/', headers=headers)
                                        print("\n fetching zoom meeting info now of the user ... \n")
                                        # print(r.text)
                                    def getMeetingParticipants():
                                        headers = {'authorization': 'Bearer %s' % generateToken(),
                                                'content-type': 'application/json'}
                                        r = requests.get(
                                            f'https://api.zoom.us/v2/metrics/meetings/participants', headers=headers)
                                        print("\n fetching zoom meeting participants of the live meeting ... \n")

                                        # you need zoom premium subscription to get this detail, also it might not work as i haven't checked yet(coz i don't have zoom premium account)

                                        print(r.text)
                                    
                                    def createMeeting():
                                        headers = {'authorization': 'Bearer %s' %generateToken(),
                                                'content-type': 'application/json'}
                                        r = requests.post(
                                            f'https://api.zoom.us/v2/users/me/meetings',
                                            headers=headers, data=json.dumps(meetingdetails))
                                    
                                        st.write("\n creating zoom meeting ... \n")
                                        # (r.text)
                                        # converting the output into json and extracting the details
                                        y = json.loads(r.text)
                                        join_URL = y["join_url"]
                                        meetingPassword = y["password"]
                                    
                                        st.write(
                                            f'\n Here is your zoom meeting link {join_URL} and your \
                                            password: "{meetingPassword}"\n')
    
    
                                        # run the create meeting function
                                    getUsers()
                                    # getMeetingParticipants()
                                    createMeeting()
                                    
                                                                                          
        
if (__name__=='__main__'):
                   app()
