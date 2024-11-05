import pandas as pd
import matplotlib.pyplot as plt

# Load CSV files with error handling
def load_and_clean_data(file_path):
    try:
        # Load the CSV file, treating '-' as NaN, and cleaning up column names
        data = pd.read_csv(file_path,encoding='utf-8',  na_values=['-'])
        data.columns = data.columns.str.strip()
        for col in data.select_dtypes(['object']).columns:
            data[col] = data[col].str.strip()
    except Exception as e:
        print(f"Error loading {file_path}: {e}")
        return None
  
    
    # Convert columns to numeric if possible (especially useful for calculations)
    num_cols = ['Calories', 'Fat (g)', 'Carb. (g)', 'Fiber (g)', 'Protein', 'Sodium']
    for col in num_cols:
        if col in data.columns:
            data[col] = pd.to_numeric(data[col], errors='coerce')    
    return data

#   path 
drink_file_path = 'package\dataset\starbucks-menu-nutrition-drinks.csv'
food_file_path = 'package\dataset\starbucks-menu-nutrition-food.csv'

#  load data
drinks_data = load_and_clean_data(drink_file_path)


file_path = 'package/dataset/starbucks-menu-nutrition-food.csv'  # Adjust the path as needed

# load food data 
data = pd.read_csv(file_path, encoding='cp1252', sep=",", skipinitialspace=True, engine="python")

food_data = data[data.columns[0]].str.split(",", expand=True)
food_data.columns = ['Item', "Calories", "Fat (g)", "Carb. (g)", "Fiber (g)", "Protein"]
numeric_columns = ["Calories", "Fat (g)", "Carb. (g)", "Fiber (g)", "Protein"]
for col in numeric_columns:
    food_data[col] = pd.to_numeric(food_data[col], errors='coerce')

# Display the cleaned DataFrame
print(food_data.head())

print(drinks_data.head())
# Descriptive statistics function
def descriptive_stats(data, name):
    print(f"\n{name} Dataset Statistics:")
    
    print(f"\nTotal calories in {name} items: {data['Calories'].dropna().sum()}")
    print(f"Average sugar content in {name} items: {data['Carb. (g)'].dropna().mean()}")
    fat_protein_ratio = (data['Fat (g)'].dropna().sum() / data['Protein'].dropna().sum()) if data['Protein'].sum() != 0 else 0
    print(f"Fat-to-Protein ratio in {name} items: {fat_protein_ratio:.2f}")

# Show basic statistics
descriptive_stats(drinks_data, 'Drinks')
descriptive_stats(food_data, 'Food')

# Comparison of key metrics
def compare_metrics():
    avg_calories_drinks = drinks_data['Calories'].dropna().mean()
    avg_calories_food = food_data['Calories'].dropna().mean()
    print("\nComparison of Average Calories:")
    print(f"Average Calories in Drinks: {avg_calories_drinks:.2f}")
    print(f"Average Calories in Food: {avg_calories_food:.2f}")

compare_metrics()

# Visualization function for nutritional comparison
def plot_nutritional_comparison():
    categories = ['Calories', 'Carb. (g)', 'Fat (g)', 'Protein']
    avg_nutrition_drinks = drinks_data[categories].dropna().mean()
    avg_nutrition_food = food_data[categories].dropna().mean()
    
    # Plot bar chart for average nutritional content
    fig, ax = plt.subplots(figsize=(10, 6))
    width = 0.35
    index = range(len(categories))
    
    ax.bar(index, avg_nutrition_drinks, width, label='Drinks')
    ax.bar([i + width for i in index], avg_nutrition_food, width, label='Food')
    
    ax.set_xlabel('Nutritional Components')
    ax.set_ylabel('Average Amount')
    ax.set_title('Average Nutritional Comparison Between Drinks and Food Items')
    ax.set_xticks([i + width / 2 for i in index])
    ax.set_xticklabels(categories)
    ax.legend()
    
    plt.show()

plot_nutritional_comparison()

# Data filtering function
def filter_data(data, criteria):
    # Example: Filter drinks with calories under a threshold
    if 'Calories' in criteria:
        data = data[data['Calories'] < criteria['Calories']]
  
    return data

# Example usage of filtering (filter drinks under 100 calories)
filtered_drinks = filter_data(drinks_data, {'Calories': 100})
print("\nFiltered Drinks with less than 100 Calories:")
print(filtered_drinks[['Item']].head())
