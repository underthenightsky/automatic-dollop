import streamlit as st
def app():
        st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://th.bing.com/th?id=OIP.70VZJExiK-YLhdiz4Oc7iQHaFj&w=288&h=216&c=8&rs=1&qlt=90&o=6&dpr=1.3&pid=3.1&rm=2");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
        st.write('Home page of the site')