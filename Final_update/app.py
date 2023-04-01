import streamlit as st
import multiapp 
import pymongo
from flask import redirect
from apps import home,data,doctors,auth,meds
# from apps.auth.func import Verification,LoginUI

# col1,col2,col3,col4,col5,col6,col7,col8=st.columns(8)
# with col1:
#     pass
# with col2:
#     pass
# with col4:
#     pass
# with col3:
#     pass
# with col6:
#     pass
# with col7:
#      if st.button('Log In', key=None, help="Click to log in ", on_click='Please Log in ', args=None, kwargs=None, type="primary", disabled=False, use_container_width=True): 

#         auth.login
    
# with col5:
#     pass
# # with col8:
# #     pass
# # with col9:ss
# #     pass
# with col8:
   
#     if st.button('Sign Up', key=None, help="Click to sign up ", on_click='Please Sign up ', args=None, kwargs=None, type="primary", disabled=False, use_container_width=True): 
#         auth.signup
# app=MultiApp()
# app.add_app('Login In',auth.login)
# app.add_app('Sign Up',auth.signup('ahh','afdjjssdm','a@gmail.com'))
# app.side_bar_run()

# app=st.selectbox(
#                 'j',
#                 self.apps,label_visibility='hidden',
#                 format_func=lambda app: app['title'])
# app['function']()
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
    app.run()

if __name__=='__main__':
        func()


    