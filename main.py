"""
Movie Recommendation System
This script processes movie data and generates recommendations based on selected features.
"""

# Import necessary libraries
import pandas as pd
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load and preprocess data
def load_and_preprocess_data(file_path):
    """Load movie data from a CSV file and preprocess it."""
    # Load data into a pandas DataFrame
    movies_data = pd.read_csv(file_path)

    # Select relevant features for recommendation
    selected_features = ['genres', 'keywords', 'tagline', 'cast', 'director']

    # Replace null values with empty strings
    for feature in selected_features:
        movies_data[feature] = movies_data[feature].fillna('')

    # Combine all selected features into a single string
    movies_data['combined_features'] = (
        movies_data['genres'] + ' ' +
        movies_data['keywords'] + ' ' +
        movies_data['tagline'] + ' ' +
        movies_data['cast'] + ' ' +
        movies_data['director']
    )

    return movies_data

# Define the file path to the dataset
FILE_PATH = r'C:\Users\shubh\OneDrive\Desktop\PROJECTS\Movie Recomendation ML\movies.csv'

# Load and preprocess the movie data
movies_data = load_and_preprocess_data(FILE_PATH)

# converting text data to feature vectors
vectorizer = TfidfVectorizer()
feature_vectors = vectorizer.fit_transform(movies_data['combined_features'])

# getting the similarity score using cosine similarity
similarity = cosine_similarity(feature_vectors)

# getting the movie name
movie_name = input("Enter a movie name: ")

# creating a list of all movie names given in the dataset
list_of_all_titles = movies_data['title'].tolist()

# finding the closest match from user input
find_closest_match = difflib.get_close_matches(movie_name,list_of_all_titles)
close_match = find_closest_match[0] # only first value from output

# finding the index of movie with title
index_of_movie = movies_data[movies_data.title == close_match]['index'].values[0]

# getting list of similar movies
similarity_score = list(enumerate(similarity[index_of_movie]))

# sorting the movies based on their similarity score
sorted_similar_movies = sorted(similarity_score, key = lambda x:x[1],reverse = True)

# print the name of similar movies based on index
print('Suggested Movies: \n')
i = 1
for movie in sorted_similar_movies:
    index = movie[0]
    title_from_index = movies_data[movies_data.index == index]['title'].values[0]
    if (i <= 10):
        print(i,'.',title_from_index)
        i += 1

