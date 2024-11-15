# Import necessary libraries
import os  # For file path management
import pickle  # For saving and loading the trained model
import pandas as pd  # For data manipulation
from sklearn.tree import DecisionTreeRegressor  # For regression model

# Define the file path to the dataset
file_directory = os.path.dirname(os.path.abspath(__file__))
path_model = os.path.join(file_directory, 'data/house-price.csv')

# Load the dataset into a DataFrame
house_df = pd.read_csv(path_model)

# Display basic information about the dataset
print(house_df.head())  # Display the first few rows
print(house_df.tail())  # Display the last few rows
print(house_df.dtypes)  # Display data types of each column
print(house_df.shape)  # Display the shape of the DataFrame
print(house_df.info())  # Display a concise summary of the DataFrame

# Separate the target variable (`Price`) and feature set (`X`)
y = house_df["Price"]  # Target variable: House prices
X = house_df.drop(columns=["Price", "Address"])  # Features, excluding non-numeric column

# Initialize and train the Decision Tree Regressor
model = DecisionTreeRegressor()
model.fit(X, y)

# Evaluate the model's performance on the training data
score = model.score(X, y)
print(f"Model R^2 score on training data: {score:.2f}")

# Save the trained model to a pickle file for later use
with open("model.pkl", "wb") as file:
    pickle.dump(model, file)

print("Model saved successfully as 'model.pkl'.")
