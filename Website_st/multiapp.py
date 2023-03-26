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
    def side_bar_run(self):
        # with st.sidebar :
        #         selected=option_menu(menu_title='Best App',
        #                             options=['Sign Up','Consult a Doctor','Order Medicines','Emergeny Help'],
        #                             icons=['house','book','envelope'],
        #                             menu_icon='cast',
        #                             orientation='horizontal'
        #                     )
         app=st.selectbox(
                'j',
                self.apps_1,label_visibility='hidden',
                format_func=lambda app: app['title'])
         app['function']()
         self.apps_1=[]

    def run(self):
        #     with st.sidebar :
        #         selected=option_menu(menu_title='Best App',
        #                             options=['Sign Up','Consult a Doctor','Order Medicines','Emergeny Help'],
        #                             icons=['house','book','envelope'],
        #                             menu_icon='cast',
        #                             orientation='horizontal'
        #                     )
        app=st.selectbox(
                'j',
                self.apps_1,label_visibility='hidden',
                format_func=lambda app: app['title'])
        app['function']()
        
    
