import streamlit as st
import os
import sys

# Add the root directory to the system path so 'src' can be found
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.recommender import MovieRecommender

st.set_page_config(page_title="Movie Recommender System", layout="centered")

st.title("🎬 Movie Recommendation System")
st.write("Select a movie you like, and we'll recommend 5 similar movies for you!")

# Initialize the recommender model
@st.cache_resource
def load_model():
    return MovieRecommender()

# Load the model only once and store it in cache
try:
    rec_model = load_model()
except Exception as e:
    st.error(f"Error loading model: {e}")
    rec_model = None

# Movie title input
movie_input = st.text_input("Enter Movie Name (e.g., Avatar, Spectre):", "Avatar")

if st.button("Get Recommendations 🍿"):
    if movie_input.strip() == "":
        st.warning("Please enter a movie name!")
    elif rec_model is None or rec_model.movies is None:
        st.error("Model is not loaded properly. Check the backend logs.")
    else:
        with st.spinner("Fetching recommendations..."):
            try:
                # Get recommendations directly from the Python class
                recommended_movies = rec_model.recommend(movie_input)
                
                if len(recommended_movies) > 0 and recommended_movies[0] != "Model not loaded. Please check your files.":
                    st.success("Recommended Movies:")
                    
                    # Display top 5 recommendations
                    for idx, movie in enumerate(recommended_movies, 1):
                        st.subheader(f"{idx}. {movie}")
                else:
                    st.error("Movie not found in the database. Try another title!")
            except Exception as e:
                st.error(f"An error occurred: {e}")