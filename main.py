
import requests
from bs4 import BeautifulSoup
import csv

def scrape_movie_info(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    movies = []
    
    for item in soup.find_all('div', class_='countdown-item-content'):
        title = item.find('h2').text.strip()
        rating = item.find('div', class_='countdown-adjusted-score').text.strip()
        
        critics_consensus = item.find('div', class_='info critics-consensus').text.strip()
        synopsis = item.find('div', class_='info synopsis').text.strip()
        
        cast = item.find('div', class_='info cast').text.strip()
        director = item.find('div', class_='info director').text.strip()
        
        movies.append({
            'title': title,
            'rating': rating,
            'critics_consensus': critics_consensus,
            'synopsis': synopsis,
            'cast': cast,
            'director': director
        })
    
    return movies

def save_to_csv(movies, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['title', 'rating', 'critics_consensus', 'synopsis', 'cast', 'director']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for movie in movies:
            writer.writerow(movie)

# Usage
url = 'https://editorial.rottentomatoes.com/guide/popular-movies/'
movie_data = scrape_movie_info(url)

# Save to CSV
save_to_csv(movie_data, 'movies.csv')

print(f"Data has been saved to movies.csv")
