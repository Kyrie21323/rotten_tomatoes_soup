import json
import numpy as np

#load the scraped data
def load_scraped_data():
    with open('movies_data.json', 'r') as file:
        movies_data = json.load(file)
    return movies_data

#analyze director ratings
def analyze_directors():
    movies_data = load_scraped_data()
    director_ratings = {}                   #create a dictionary to store directors and their respective ratings

    #populate the dictionary with ratings for each director
    for movie in movies_data:
        director = movie['director']
        try:
            rating = int(movie['rating'].strip('%'))
        except ValueError:
            continue
#        rating = movie['rating']
        if director not in director_ratings:
            director_ratings[director] = []
        director_ratings[director].append(rating)

    #calculate average ratings for each director
    average_ratings = {director: np.mean(ratings) for director, ratings in director_ratings.items()}

    #sort directors by average ratings (got it from open AI)
    sorted_directors = sorted(average_ratings.items(), key=lambda x: x[1], reverse=True)

    #get top 10 and lowest 10 directors
    top_10_directors = sorted_directors[:10]
    lowest_10_directors = sorted_directors[-10:]

    #show results
    print("Top 10 Directors:")
    for director, avg_rating in top_10_directors:
        print(f"{director}: {avg_rating:.2f}")
    print("\nLowest 10 Directors:")
    for director, avg_rating in lowest_10_directors:
        print(f"{director}: {avg_rating:.2f}")


if __name__ == '__main__':
    analyze_directors()
