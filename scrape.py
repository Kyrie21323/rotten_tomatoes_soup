from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import pandas as pd
import time

# Path to your ChromeDriver
webdriver_path = 'C:/Users/2028e/Documents/chromedriver-win64/chromedriver.exe'

# Initialize the Chrome WebDriver
service = Service(webdriver_path)
driver = webdriver.Chrome(service=service)

# Open the Rotten Tomatoes home page
driver.get('https://www.rottentomatoes.com/')

# Give the page some time to load completely
time.sleep(5)  # Adjust this sleep time if your internet is slower/faster

# Parse the fully loaded page with BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Find all sections for movies on the home page
movie_sections = soup.find_all('section', {'class': 'dynamic-poster-list'})

# Lists to store movie data
movies = []
ratings = []
directors = []
links = []

# Loop through each section to extract movie details
for section in movie_sections:
    movie_items = section.find_all('div', {'class': 'dynamic-poster'})
    for movie in movie_items:
        title = movie.find('span', {'class': 'p--small'}).text.strip() if movie.find('span', {'class': 'p--small'}) else 'N/A'
        rating = movie.find('span', {'class': 'tMeterScore'}).text.strip() if movie.find('span', {'class': 'tMeterScore'}) else 'N/A'
        link = 'https://www.rottentomatoes.com' + movie.find('a')['href'] if movie.find('a') else 'N/A'
        
        # Append movie data to lists
        movies.append(title)
        ratings.append(rating)
        links.append(link)

# Visit each movie page to extract director names
for link in links:
    if link != 'N/A':
        # Visit the movie page
        driver.get(link)
        time.sleep(3)  # Wait for the page to load

        # Parse the movie page with BeautifulSoup
        movie_soup = BeautifulSoup(driver.page_source, 'html.parser')

        # Try to extract the director's name
        director = movie_soup.find('a', {'data-qa': 'movie-info-director'})
        if director:
            directors.append(director.text.strip())
        else:
            directors.append('N/A')
    else:
        directors.append('N/A')

# Close the Selenium browser
driver.quit()

# Create a DataFrame to store the data
df = pd.DataFrame({
    'Movie Title': movies,
    'Rating': ratings,
    'Director': directors,
    'Link': links
})

# Display the DataFrame
print(df)

# Save the data to a CSV file
df.to_csv('rottentomatoes_home_movies_with_directors.csv', index=False)

