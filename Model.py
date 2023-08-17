import streamlit as st
import pickle

# Load the model
model_filename = 'model.pkl'
with open(model_filename, 'rb') as model_file:
    loaded_model = pickle.load(model_file)

# Define the Streamlit app
def main():
    st.title("Income Prediction App")
    st.write("Enter your age and years of experience to predict income.")

    age = st.slider("Age", 18, 100, 25)
    experience = st.slider("Experience (years)", 0, 50, 5)

    if st.button("Predict Income"):
        input_data = [[age, experience]]
        predicted_income = loaded_model.predict(input_data)[0]
        st.success(f"Predicted Income: ${predicted_income:.2f}")

if __name__ == "__main__":
    main()