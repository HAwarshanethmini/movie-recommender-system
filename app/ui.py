import streamlit as st
import requests

st.set_page_config(page_title="Movie Recommender System", layout="centered")

st.title("🎬 Movie Recommendation System")
st.write("Select a movie you like, and we'll recommend 5 similar movies for you!")

# FastAPI Backend URL
API_URL = "http://127.0.0.1:8000/recommend"

# Movie title input
movie_input = st.text_input("Enter Movie Name (e.g., Avatar, Spectre):", "Avatar")

if st.button("Get Recommendations 🍿"):
    if movie_input.strip() == "":
        st.warning("Please enter a movie name!")
    else:
        with st.spinner("Fetching recommendations..."):
            try:
                # Call FastAPI backend
                response = requests.get(API_URL, params={"movie_title": movie_input})
                
                if response.status_code == 200:
                    data = response.json()
                    st.success("Recommended Movies:")
                    
                    # Display top 5 recommendations
                    for idx, movie in enumerate(data["recommended_movies"], 1):
                        st.subheader(f"{idx}. {movie['title']}")
                elif response.status_code == 404:
                    st.error("Movie not found in the database. Try another title!")
                else:
                    st.error("Something went wrong on the server.")
            except Exception as e:
                st.error("Could not connect to backend server. Make sure FastAPI is running!")