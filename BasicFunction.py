# Stream Basic Functions
import streamlit as st

#Title
st.title("Hello Streamlit")

#Header
st.header("This is header")

#Subheader
st.subheader("This is subheader")

#Text
st.text("Hello Welcome to Streamlit")

# Success, Info, Warning, Error, Exception

#Success
st.success("THis is Success Message")

#Success
st.info("Information")

#success
st.warning("Warning Message")

#success
st.error("Error Message")

# Exception - This has been added later
exp = ZeroDivisionError("Trying to divide by Zero")
st.exception(exp)

# Write Text
st.write("Text with write")

# Writing python inbuilt function range()
st.write(range(10))