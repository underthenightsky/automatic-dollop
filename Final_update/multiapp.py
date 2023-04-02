import streamlit as st
from apps import home,doctors,data,auth
class MultiApp():
    def __init__(self):
        self.apps_1=[]
    def add_app(self,title,func):
        self.apps_1.append({
        'title':title,
        'function':func
    })
   

    def run(self):
      
        app=st.selectbox(
                'j',
                self.apps_1,label_visibility='hidden',
                format_func=lambda app: app['title'])
        app['function']()
        
    
