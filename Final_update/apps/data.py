import streamlit as st
from apps import auth
import pymongo
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
    if (len(auth.export_username)==0):
        st.warning('Please Log in or Sign up to view patient data.')
    else:    
        client = pymongo.MongoClient("mongodb+srv://Garv:bcss1972@cluster0.wjgguh1.mongodb.net/?retryWrites=true&w=majority")
        db = client["mydatabase"]
        results=db.users.find_one({"username":auth.export_username})
        col1,col2=st.columns(2)
        with col1:
                                st.markdown('')
                                st.write('Fullname',f"{results['name']}",placeholder='Please fill up this section')
                                st.write('Age',f"{results['age']}",placeholder='Please fill up this section')
                                st.write('Weight (in Kg)',f"{results['Weight']}",placeholder='Please fill up this section')
        with col2:
                                st.markdown('')
                                st.write('Gender',f"{results['gender']}",placeholder='Please fill up this section')
                                st.write('Height (in cms)',f"{results['Height']}",placeholder='Please fill up this section')
                                st.write("Medical Issues or Allergies",f"{results['MedicalHistory']}",placeholder='Please fill up this section')