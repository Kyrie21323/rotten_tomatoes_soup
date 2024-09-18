import requests
from bs4 import BeautifulSoup
import time
import json                                 #save data as .json

# URL of the Rotten Tomatoes page to scrape
URL = 'https://editorial.rottentomatoes.com/guide/best-netflix-movies-to-watch-right-now/'

def fetch_page(url):
    """Fetches the content of the page using requests."""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching page: {e}")
        return None

def parse_page(html):
    """Parses the page content to extract movie names and ratings."""
    soup = BeautifulSoup(html, 'html.parser')
    movies = []

    # Locate the blocks containing both the title and rating
    for item in soup.find_all('div', class_='col-sm-20 col-full-xs'):
        title_tag = item.find('a')  # Movie title is in the <a> tag
        title = title_tag.text.strip() if title_tag else 'N/A'

        # The rating is inside the <span> with class tMeterScore
        rating_tag = item.find('span', class_='tMeterScore')
        rating = rating_tag.text.strip() if rating_tag else 'N/A'

        movies.append({'title': title, 'rating': rating})
    
    return movies

def main():
    html = fetch_page(URL)
    if html:
        movies = parse_page(html)
        for movie in movies:
            print(f"Title: {movie['title']}, Rating: {movie['rating']}")
        # Respectful scraping: Add delay between requests
        time.sleep(1)

if __name__ == "__main__":
    main()

#===========================================
def save_scraped_data(movies_data):
    with open('movies_data.json', 'w') as file:
        json.dump(movies_data, file, indent=4)

#assuming movies_data is the list of dictionaries with director and rating
movies_data = [
    {'director': 'Director A', 'rating': 85},
    {'director': 'Director B', 'rating': 90},
    {'director': 'Director A', 'rating': 80},
    {'director': 'Director C', 'rating': 70},
    # Add more data here after scraping
]

save_scraped_data(movies_data)
