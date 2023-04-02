import streamlit as st
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
        st.write('Whether you need professional medical help or just need to buy medicines we have got you covered.')
        st.subheader("Confused about how to use the website ?")
        st.write("The site is basically divided into 2 sections a doctor's section where doctors can sign up and meet patients and a patient section where people can order medicines and consult doctors.")
       
        st.subheader('  About Us  ')
        st.write('This effort started as an effort to connect doctors and people so that everyone can have access to high quality medical advice and medicines at affordable rates.')