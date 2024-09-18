# rotten_tomatoes_soup
## Project Description

This project is a web scraper designed to extract movie director names and their corresponding movie ratings from the **Rotten Tomatoes** website. It uses **Selenium** to automate the browser, allowing the scraper to navigate to each movie's page and gather the necessary information. The primary goal of this project is to generate insights by calculating the average rating of movies directed by each director.

### Data Extracted:
- **Director Names**: The scraper extracts the names of the movie directors.
- **Ratings**: The movie ratings (as percentages) from Rotten Tomatoes are also scraped.
   - **Ratings**: The movie ratings (as percentages) from Rotten Tomatoes are also scraped.
### Purpose:
The purpose of this project is to provide an automated method of gathering movie data for analysis. By scraping Rotten Tomatoes, we can uncover which directors consistently produce high-rated movies and which don't, providing insights into their success and the reception of their films. The final analysis involves calculating the average rating of each director’s movies and ranking them in descending order.

---

## Website Used

We chose **[Rotten Tomatoes](https://www.rottentomatoes.com/)** as the website for scraping due to its reputation as a trusted and widely used platform for movie reviews and ratings. Rotten Tomatoes aggregates movie reviews from critics and audience members, making it an ideal source for unbiased and widely accepted movie ratings.

Rotten Tomatoes does not have an easily accessible public API for this kind of data, making this scraper a valuable tool for gathering such information.

---

## How to Run the Project

### Prerequisites:

Before running the scraper, you need the following installed on your system:
- **Python 3.x**
- **Selenium**
- **ChromeDriver** (compatible with your version of Chrome)
- **Pandas**
- **BeautifulSoup**

### Step-by-Step Instructions

1. **Clone the Repository**:

   First, clone this GitHub repository to your local machine:
   ```bash
   git clone https://github.com/your-username/rotten_tomatoes_soup.git
   cd rotten_tomatoes_soup
   ```

2. **Set Up the Environment**:

   Install the required Python libraries by running the following command:
   ```bash
   pip install -r requirements.txt
   ```

3. **Download ChromeDriver**:

   You need to download ChromeDriver and make sure it's compatible with your version of Google Chrome:
   - Download ChromeDriver from [here](https://sites.google.com/chromium.org/driver/).
   - After downloading, place the `chromedriver.exe` in your desired folder and update the path in the `scrape.py` file.

4. **Run the Scraper**:

   To run the scraper, execute the following command:
   ```bash
   python scrape.py
   ```

   This will start the Selenium Chrome browser, navigate through the Rotten Tomatoes website, and begin scraping movie directors and ratings.

5. **Analyze the Data**:

   Once the scraping is completed, the data will be saved in a CSV file (`directors_and_ratings.csv`). To analyze the data and calculate the average rating for each director, you can run the analysis script:
   ```bash
   python analyze_directors.py
   ```

   This script will output the directors and their average movie ratings, sorted in descending order. The results are saved in the `average_ratings_by_director.csv` file.

---

## Key Files in This Repository

- **scrape.py**: The main web scraping script using Selenium to extract movie director names and ratings from Rotten Tomatoes.
- **analyze_directors.py**: A script to analyze the scraped data, calculate average movie ratings per director, and list them in descending order.
- **movies.csv**: The raw CSV file containing scraped data for directors and ratings.
- **requirements.txt**: A file listing all necessary dependencies to run the project.

---

## Ethical Considerations

Web scraping can place a load on the target website, so it's important to be respectful of the website's terms of service. This project respects the website by implementing pauses between requests to avoid overloading Rotten Tomatoes' servers. Users should verify that scraping Rotten Tomatoes complies with their terms of service before using the scraper extensively.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

Feel free to adjust the repository link and author information to match your project!

Let me know if you need further customization!
