import streamlit as st
import pandas as pd

from apps import auth



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
    # new_path_meds='C:/Users/Friend/Downloads/doctor_app-master/apps/
    # if os.path.exists("C:/Users/Friend/Downloads/doctor_app-master/apps/medicines_names.xlsx"):
    #      os.chdir("C:/Users/Friend/Downloads/doctor_app-master/apps")
    meds_df = pd.read_csv("C:/Users/1/Downloads/doctor_app-master/doctor_app-master/Final_update/apps/medicines_names.csv")
    # else :    
    # # # Load data
    #     meds_df = pd.read_csv(f'{os.getcwd()}/medicines_names.xlxs')
    
    # Define page layout
    st.title('Buy Medicines')
    st.write('')
    # Create navigation bar

    # Show appropriate page based on selection
    st.sidebar.title('Select type of medicines')
    Type_1 = st.sidebar.multiselect('Select Type of Medicines ', meds_df['Type'].explode().unique())

    # Filter data
    filtered_meds= meds_df[meds_df['Type'].apply(lambda x: any(item for item in Type_1 if item in x))]

    # Display results
    if len(filtered_meds) == 0:
        st.warning('Please select a type of medicines.')
    else:
        for index, row in filtered_meds.iterrows():
            st.image(row['Image'], width=250)
            st.write(f"## {row['Name']} ({row['Type']})")
            st.write(f"Price: {row['Price']}")
            st.write(f"Delivery Date: {row['Delivery Date']}")
            st.write(f"Expiry Date: {row['Expiry Date']} ")
            st.write('---')
    # if len(filtered_meds)>1:
    #       st.error("Please chose only one doctor at a time.")
    # # while True :
            
    # if len(filtered_meds) == 1:
            
    if len(auth.export_username)==0:                 
                   st.error("Please Log in or Sign up to buy medicines.")
    else:     
                if st.button("Click here to Buy") or st.session_state.load_state:
                    st.session_state.load_state=True
                    # cluster=pymongo.MongoClient('mongodb+srv://Garv:bcss1972@cluster0.wjgguh1.mongodb.net/?retryWrites=true&w=majority')
                    # db=cluster['mydatabase']
                    # results=db.users.find_one({"username":export_username})
