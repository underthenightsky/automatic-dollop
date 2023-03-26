import streamlit as st
import pandas as pd
import os

def app():
    # Set page title and favicon
    # st.set_page_config(page_title='Find a Doctor',page_icon=':hospital:')

    # Load data
    doctors_df = pd.read_csv(f'{os.getcwd()}/doctors_names.csv')
    
    # Define page layout
    st.title('Doctor Finder')
    st.write('')
    # Create navigation bar

    # Show appropriate page based on selection
    st.sidebar.title('Filter Doctors')
    symptoms = st.sidebar.multiselect('Select Symptoms', doctors_df['Symptoms'].explode().unique())

    # Filter data
    filtered_df = doctors_df[doctors_df['Symptoms'].apply(lambda x: any(item for item in symptoms if item in x))]

    # Display results
    if len(filtered_df) == 0:
        st.warning('No doctors found with the selected symptoms.')
    else:
        for index, row in filtered_df.iterrows():
            st.image(row['Image'], width=250)
            st.write(f"## {row['Name']} ({row['Specialty']})")
            st.write(f"Address: {row['Address']}")
            st.write(f"Phone: {row['Phone']}")
            st.write(f"Experience: {row['XP']} years")
            st.write('---')
if __name__=='__main__':
    app()   