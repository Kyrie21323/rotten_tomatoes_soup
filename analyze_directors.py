import json
import numpy as np

# Step 1: Load the scraped data
def load_scraped_data():
    with open('movies_data.json', 'r') as file:
        movies_data = json.load(file)
    return movies_data

# Step 2: Analyze director ratings
def analyze_directors():
    movies_data = load_scraped_data()

    # Create a dictionary to store directors and their respective ratings
    director_ratings = {}

    # Populate the dictionary with ratings for each director
    for movie in movies_data:
        director = movie['director']
        rating = movie['rating']
        if director not in director_ratings:
            director_ratings[director] = []
        director_ratings[director].append(rating)

    # Calculate average ratings for each director
    average_ratings = {director: np.mean(ratings) for director, ratings in director_ratings.items()}

    # Sort directors by average ratings
    sorted_directors = sorted(average_ratings.items(), key=lambda x: x[1], reverse=True)

    # Get top 10 and lowest 10 directors
    top_10_directors = sorted_directors[:10]
    lowest_10_directors = sorted_directors[-10:]

    # Display results
    print("Top 10 Directors:")
    for director, avg_rating in top_10_directors:
        print(f"{director}: {avg_rating:.2f}")

    print("\nLowest 10 Directors:")
    for director, avg_rating in lowest_10_directors:
        print(f"{director}: {avg_rating:.2f}")

# Step 3: Run the analysis
if __name__ == '__main__':
    analyze_directors()
