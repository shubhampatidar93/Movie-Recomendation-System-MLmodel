# Movie Recommendation System

This project is a **Movie Recommendation System** that uses machine learning techniques to recommend movies based on selected features such as genres, keywords, tagline, cast, and director.

## Features
- **Data Preprocessing**: Combines multiple features into a single string for analysis.
- **Machine Learning**: Uses TF-IDF Vectorization and Cosine Similarity to calculate movie recommendations.
- **Extensible**: Can be integrated with APIs like TMDB for dynamic data fetching.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/movie-recommendation-ml.git
   ```
2. Navigate to the project directory:
   ```bash
   cd movie-recommendation-ml
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Ensure the dataset (`movies.csv`) is in the project directory.
2. Run the script:
   ```bash
   python main.py
   ```
3. Follow the prompts to get movie recommendations.

## API Integration (Optional)
You can use APIs like TMDB to fetch movie data dynamically. Replace the dataset loading logic with API calls.

