import pandas as pd

file_path = 'package/dataset/starbucks-menu-nutrition-food.csv'  # Adjust the path as needed

# Step 1: Read the file with specific settings
data = pd.read_csv(file_path, encoding='cp1252', sep=",", skipinitialspace=True, engine="python")

# Step 2: If pandas still reads it as one column, split it manually
if len(data.columns) == 1:
    # Split the single column into multiple columns based on commas
    data = data[data.columns[0]].str.split(",", expand=True)
    data.columns = ['Item', "Calories", "Fat (g)", "Carb. (g)", "Fiber (g)", "Protein (g)"]

# Step 3: Drop rows with all NaN values, if any
data = data.dropna(how='all')

# Display the cleaned DataFrame
print(data.head())
