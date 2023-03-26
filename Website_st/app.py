import streamlit as st
import matplotlib as plt
from sklearn import datasets
import numpy as np
import pandas as pd
from streamlit_option_menu import option_menu
from multiapp import MultiApp
from apps import home,data,doctors,auth
col1,col2,col3,col4,col5,col6,col7,col8=st.columns(8)
with col1:
    pass
with col2:
    pass
with col4:
    pass
with col3:
    pass
with col6:
    pass
with col7:
    pass
with col5:
    pass
# with col8:
#     pass
# with col9:
#     pass
with col8:
   
    if st.button('Sign Up', key=None, help="Click to log in ", on_click='Please Log in ', args=None, kwargs=None, type="primary", disabled=False, use_container_width=True): 
        auth.verification()
        # <div class="css-6dnr6u edgvbvh1"><div class="stTooltipIcon css-1aqmucy e1j25pv60"><div data-testid="tooltipHoverTarget" id="bui4__anchor" style="display: flex; flex-direction: row; justify-content: flex-end;"><button kind="secondary" class="css-fxzapv edgvbvh10"><div data-testid="stMarkdownContainer" class="css-1offfwp e16nr0p34"><p>Sign Up</p></div></button></div></div></div>
colT1,colT2 = st.columns([1,5.8])
with colT2:
    st.title('   New Medicos')
    st.write("A common interface for patients and doctors")

app=MultiApp()
app.add_app('Home',home.app)
app.add_app('Data',data.app)
app.add_app('Consult a Doctor',doctors.app)
app.run()

    