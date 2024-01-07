# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset (replace 'your_dataset.csv' with your actual dataset)
df = pd.read_csv('your_dataset.csv')

# Explore the first few rows of the dataset
print(df.head())

# Basic statistics of the numerical columns
print(df.describe())

# Visualize data distribution (replace 'column_name' with an actual column name)
plt.hist(df['column_name'])
plt.title('Data Distribution')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.show()

# Correlation matrix
correlation_matrix = df.corr()
print(correlation_matrix)

# Scatter plot to visualize correlation (replace 'column1' and 'column2' with actual column names)
plt.scatter(df['column1'], df['column2'])
plt.title('Scatter Plot')
plt.xlabel('Column 1')
plt.ylabel('Column 2')
plt.show()