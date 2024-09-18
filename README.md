# rotten_tomatoes_soup
## Project Description

This project is a web scraper that extracts movie director names and corresponding movie ratings from an archived version of the **Rotten Tomatoes** website using **requests** and **BeautifulSoup**. The primary goal of this project is to scrape and analyze movie ratings to calculate the average rating of movies directed by each director, and rank them in descending order. Additionally, the project outputs the top 10 and bottom 10 directors based on their average ratings.

### Data Extracted:
- **Director Names**: The scraper extracts the names of movie directors from each movie's details.
- **Ratings**: The scraper also extracts movie ratings (as percentages) from Rotten Tomatoes.

### Purpose:
This project automates the process of gathering movie rating data for directors to provide insights into which directors consistently produce high-rated movies and which do not. The data is then processed to compute the average ratings for each director, allowing us to identify the top and bottom performing directors based on Rotten Tomatoes ratings.

---

## Website Used

We chose the **[archived version of Rotten Tomatoes](https://web.archive.org/web/20240916202321/https://editorial.rottentomatoes.com/guide/best-netflix-movies-to-watch-right-now/)** for scraping due to its rich data on movie reviews and ratings. The archived version is used to ensure stable access to the page content.

The Rotten Tomatoes website is a popular source for both critic and audience movie reviews and ratings, making it an ideal platform for this project. Rotten Tomatoes does not provide a public API for this specific type of data, so we opted for web scraping to obtain the required information.

---

## How to Run the Project

### Prerequisites:

Before running the scraper, you need the following installed on your system:
- **Python 3.x**
- **Pandas**
- **BeautifulSoup4**
- **Requests**

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

3. **Run the Scraper**:

   To run the scraper and save the data to a JSON file, execute the following command:
   ```bash
   python main.py
   ```

   This will fetch the Rotten Tomatoes page (from the archive) and extract movie director names and ratings. The data will be saved in `movies_data.json`.

4. **Analyze the Data**:

   Once the scraping is completed, you can analyze the data by running the analysis script:
   ```bash
   python analyze_directors.py
   ```

   This script will:
   - Calculate the average rating for each director.
   - Display the top 10 and bottom 10 directors by average rating.
   - Save the results to `top_10_directors.csv` and `bottom_10_directors.csv`.

---

## Key Files in This Repository

- **main.py**: The web scraper script that fetches movie director names and ratings from the Rotten Tomatoes page and saves them to `movies_data.json`.
- **analyze_directors.py**: A script to analyze the scraped data, calculate average movie ratings per director, and display the top and bottom 10 directors.
- **movies_data.json**: The JSON file where scraped data is stored.
- **top_10_directors.csv** & **bottom_10_directors.csv**: The results of the analysis, containing the top and bottom 10 directors based on average ratings.
- **requirements.txt**: A file listing all necessary dependencies to run the project.

---

## Ethical Considerations

Web scraping can put a load on websites, so it's important to respect the target website's terms of service. This project avoids overwhelming the website by using appropriate request headers and adding pauses between requests. The data is scraped from an archived version of the Rotten Tomatoes page, ensuring stable access without overloading the live site.

Before running this scraper extensively, users should verify that scraping is compliant with the website’s terms of service.
See the `ETHICS` file for more details.
