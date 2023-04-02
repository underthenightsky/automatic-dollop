import pymongo
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
    if "load_state" not in st.session_state:
                                                    
                                st.session_state.load_state = False   
    st.header('Doctors Section')
    st.write('Are you a doctor looking to provide healthcare advice at low rates for people living in inacccessible regions?')
    st.write('Then look no furthur, start providing medical advice in 3 simple steps.')
    st.write('1.Fill up the form.')
    st.write('2.Wait while we verify your credentials.')
    st.write('3.Get started.')
    if st.button("Click here to fill up the form .") or st.session_state.load_state:
                            st.session_state.load_state=True
                            cluster=pymongo.MongoClient('mongodb+srv://Garv:bcss1972@cluster0.wjgguh1.mongodb.net/?retryWrites=true&w=majority')
                            db=cluster['mydatabase']
                            with st.form('Talk to Patients'):
                                st.header("Doctors Registration Form")
                                st.write('Please fill up this form')
                                col1,col2=st.columns(2)
                                with col1:
                                     st.markdown('')
                                     fullname=st.text_input('Fullname',placeholder='Please fill up this section')
                                     username=st.text_input('Please enter a username',placeholder='Please fill up this section.')
                                     age=st.text_input('Age',placeholder='Please fill up this section')
                                    # weight=st.text_input('Weight (in Kg)',placeholder='Please fill up this section')
                                     password = st.text_input("Password", type="password",placeholder='Please fill up this section')
                            
                                with col2:
                                    st.markdown('')
                                    gender=st.text_input('Gender',placeholder='Please fill up this section')
                                    # height=st.text_input('Height (in cms)',placeholder='Please fill up this section')
                                    medical_speciality=st.text_input("What is your medical speciality ?",placeholder='Please fill up this section')
                                    confirm_password = st.text_input("Confirm Password", type="password",placeholder='Please fill up this section')
                                Hospital_name=st.text_input("Where are you currently practising ?",placeholder='Please fill up this section')
                                email = st.text_input("Email")
                                Experience=st.text_input("For how may yers have you been practising ?",placeholder='Please fill up this section')
                                Phone_number=st.text_input("What si your registered Phon?",placeholder='Please fill up this section')
                                Address=st.text_area("What is your address ?",placeholder='Please fill up this section')                     
                                # st.success("Form Submitted successfully!")
                                submission=st.form_submit_button("Submit")
                                if submission==True:
                                    if (password!=confirm_password):
                                            st.error("Input in password and confirm password fileds should be the same.")
                                    elif ((len(email.strip()) == 0) or not('.com' in email)):
                                        st.error("Please enter a vail email address.")
                                    elif len(password.strip()) <= 7:
                                        st.error("Minimum pass lenght is 8.")        
                                    elif (len(fullname)==0 or len(age)==0 or len(medical_speciality)==0 or len(gender)==0 or len(Experience)==0 or len(Address)==0 or len(Phone_number)==0 or len(Hospital_name)==0 or len(username)==0):
                                        st.error('Please fill up all the required sections')
                                    else :
                                        # doctors.export_username_1=username      
                                        user = {"username": username, "password":password, "email": email, "name": fullname,"age": age,"gender":gender, " medical_speciality":  medical_speciality, "Hospital_name": Hospital_name, " Phone_number":  Phone_number,'Address':Address}
                                        # db.users.delete_many({"username":f"{results['username']}"})
                                        db.users.insert_one(user)
                                        st.write('Form submitted successfully.')
                                        st.write('Please wait 4 to 5 working days while our team verifies yours credentials.')
                                        # consult_1(user.values())
                                        cluster.close()
if __name__=='__main__':
        app()
                                    