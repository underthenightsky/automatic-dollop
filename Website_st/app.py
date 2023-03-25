import streamlit as st
import matplotlib as plt
from sklearn import datasets
import numpy as np
import pandas as pd
from streamlit_option_menu import option_menu
from multiapp import MultiApp
from apps import home,data,doctors,auth

colT1,colT2 = st.columns([1,5.8])
with colT2:
    st.title('   New Medicos')
st.write("India's best doctors just 1 click away.")

app=MultiApp()
app.add_app('Home',home.app)
app.add_app('Data',data.app)
app.add_app('Doctors',doctors.app)
app.run()

    
    
    
