# BMI Calculator
import streamlit as st

st.title('My First Streamlit BMI Cauculator')

weight = st.number_input("Enter Your Weight (in kgs)")
height = st.number_input("Enter Your height (in cms)")

try:
    bmi = weight / ((height/100)**2)
except:
    st.text("Enter some value of height")

if(st.button('Calculate BMI')):
    st.text("Your BMI Index is {}".format(bmi))

    if(bmi < 16):
        st.error("You are Extremely Underweight")
    elif(bmi >= 16 and bmi < 18.5):
        st.warning("You are Underweight")
    elif(bmi >= 18.5 and bmi < 25):
        st.success("Healthy")
    elif(bmi >= 25 and bmi < 30):
        st.warning("Overweight")
    elif(bmi >= 30):
        st.error("Extremely Overweight")
