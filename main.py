import streamlit as st

name = st.text_input("Enter your name :")
fatername = st.text_input("Enter your father name :")
address = st.text_area("Enter your Text :")
classdata= st.selectbox("Select your class",(1,2,3,4,5,6))
button = st.button("done")
if button:
    st.markdown(f""" Name: {name}
                Father: {fatername}
                Address: {address}
                Class: {classdata}""")