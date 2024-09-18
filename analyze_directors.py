import pandas as pd
import json

# Load the scraped data from JSON
with open('C:/Users/2028e/Documents/Github/rotten_tomatoes_soup/movies_data.json', 'r') as file:
    movies_data = json.load(file)

# Convert the data into a pandas DataFrame
df = pd.DataFrame(movies_data)

# Clean the 'rating' column by removing non-numeric characters
df['rating'] = df['rating'].str.extract(r'(\d+)', expand=False)  # Extract only numeric characters

# Convert the cleaned 'rating' column to float
df['rating'] = df['rating'].astype(float)

# Group by director and calculate the average rating for each director
average_ratings = df.groupby('director')['rating'].mean().reset_index()

# Sort by rating in descending order
average_ratings_sorted = average_ratings.sort_values(by='rating', ascending=False)

# Get top 10 and bottom 10 directors
top_10_directors = average_ratings_sorted.head(10)
bottom_10_directors = average_ratings_sorted.tail(10)

# Display the top 10 and bottom 10 directors
print("Top 10 Directors by Rating:")
print(top_10_directors)

print("\nBottom 10 Directors by Rating:")
print(bottom_10_directors)

# Optionally, save the result to CSV files
top_10_directors.to_csv('top_10_directors.csv', index=False)
bottom_10_directors.to_csv('bottom_10_directors.csv', index=False)
