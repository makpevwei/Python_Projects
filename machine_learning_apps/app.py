# Import necessary libraries
import os  # For file path management
import pickle  # For loading the trained model
import pandas as pd  # For creating and manipulating DataFrames
import streamlit as st  # For building the web app

# Define the file path to the trained model
file_directory = os.path.dirname(os.path.abspath(__file__))
path_model = os.path.join(file_directory, 'model.pkl')

# Create a sidebar form for user input
with st.sidebar.form("price"):
    # Collect house features from the user
    my_house = {
        "Bedrooms": st.number_input("Number of Bedrooms:", min_value=0, step=1),
        "Bathrooms": st.number_input("Number of Bathrooms:", min_value=0, step=1),
        "Garage": st.number_input("Number of Garage:", min_value=0, step=1),
        "Build Year": st.number_input("Year Built (Minimum):", min_value=1900, step=1),
        "Floor Area": st.number_input("Floor Area Size (sq ft):", min_value=0, step=1)
    }
    
    # Submit button for prediction
    submit = st.form_submit_button("Predict Price")

# Define an index name for the input DataFrame
name = "Lagos"

# Convert user input into a DataFrame
my_house_df = pd.DataFrame(my_house, index=[name])

# Load the trained model
with open(path_model, "rb") as file:
    model = pickle.load(file)

# Make a prediction using the input features
y_pred = model.predict(my_house_df)[0]

# Display the predicted price and input details
st.write(f"The estimated price is ${y_pred:,.2f}.")
st.write("Given the features of your house:")
st.write(my_house_df)
