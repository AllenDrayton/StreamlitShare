import streamlit as st
import pandas as pd
from PIL import Image

st.write("My First Stremlit app")
# Create sample data 
data={"sales":[30,40,50,20,10,40]}
df=pd.DataFrame(data)

#Draw Line chart of dataframe
st.line_chart(df)

#Opening Image file 
image = Image.open('Sage.png')

#displaying the image on streamlit app
st.image(image, caption='Display Lenna Image')
