import streamlit as st

st.title("Hello I am Abhilash !!")

status = st.radio("Select Gender: ", ('Male', 'Female'))

if status == 'Male':
    st.success("Male")
else:
    st.success("Female")

hobby = st.selectbox("Select your bike: ",
                     ['None','Royal Enfield Meteor350', 'TVS Ronin', 'Triumph Speed 400', 'Harley Davidson X440'])
st.write(f"You have selected '{hobby}' as you best bike.")