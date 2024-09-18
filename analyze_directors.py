import pandas as pd

# Load the CSV file
file_path = 'C:/Users/2028e/Documents/GitHub/rotten_tomatoes_soup/movies.csv'
df = pd.read_csv(file_path)

# Clean the 'rating' column by removing non-numeric characters
df['rating'] = df['rating'].str.extract(r'(\d+)', expand=False)  # Extract only numeric characters

# Convert the cleaned 'rating' column to float
df['rating'] = df['rating'].astype(float)

# Group by director and calculate the average rating for each director
average_ratings = df.groupby('director')['rating'].mean().reset_index()

# Sort by rating in descending order
average_ratings_sorted = average_ratings.sort_values(by='rating', ascending=False)

# Display the result
print(average_ratings_sorted)

# Save to a new CSV file
average_ratings_sorted.to_csv('average_ratings_by_director.csv', index=False)