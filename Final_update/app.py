import streamlit as st
import multiapp 
import pymongo
from flask import redirect
from apps import home,data,doctors,auth,meds,doctors_section,doctor_meeting

colT1,colT2 = st.columns([1,5.8])
with colT2:
            st.title('   New Medicos')
            st.markdown('### A common interface for patients and doctors ###' )    

def func():
    app=multiapp.MultiApp()

    app.add_app('Home Page',home.app)
    app.add_app('Sign Up', auth.Verification)
    app.add_app('Log In',auth.LoginUI)
    app.add_app('Data',data.app)
    app.add_app('Order Medicines',meds.app)
    app.add_app('Consult a Doctor',doctors.app)
    app.add_app("Doctor's Registration",doctors_section.app)
    app.add_app('Talk to patients',doctor_meeting.app)
    app.run()

if __name__=='__main__':
        func()


    