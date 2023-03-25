import streamlit as st
from apps import home,doctors,data,auth
from streamlit_option_menu import option_menu
class MultiApp():
    def __init__(self):
        self.apps=[]
    def add_app(self,title,func):
        self.apps.append({
        'title':title,
        'function':func
    })
    def run(self):
        #     with st.sidebar :
        #         selected=option_menu(menu_title='Best App',
        #                             options=['Sign Up','Consult a Doctor','Order Medicines','Emergeny Help'],
        #                             icons=['house','book','envelope'],
        #                             menu_icon='cast',
        #                             orientation='horizontal'
        #                     )
        app=st.selectbox(
                '',
                self.apps,
                format_func=lambda app: app['title'])
        app['function']()
        pass
    
