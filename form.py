import streamlit as st

esub = st.selectbox("Elective : ", ['Music', 'Korean', 'Japanese'])

st.write("Your elective subject is : ", esub)

hobbies = st.multiselect("Hobbies : ", ['Painting', 'Sport', 'Music', 'Reading'])

st.write("You selected", len(hobbies), 'hobbies')

if(st.button("Click me!")):
    st.text("Hello! Welcome to Streamlit")

name = st.text_input("Enter Your name", "Type Here...")

if(st.button('Submit')):
    result = name.title()
    st.write("Hello ", result)

level = st.slider("Select the level", 1,10)

st.text('Selected: {}'.format(level))