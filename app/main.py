from fastapi import FastAPI, HTTPException
import pickle
import pandas as pd

app = FastAPI(title="Movie Recommendation API")

# Load saved models
try:
    movies_dict = pickle.load(open('models/movies.pkl', 'rb'))
    movies = pd.DataFrame(movies_dict)
    similarity = pickle.load(open('models/similarity.pkl', 'rb'))
except Exception as e:
    print(f"Error loading model files: {e}")

@app.get("/")
def home():
    return {"message": "Welcome to Movie Recommendation API"}

@app.get("/recommend")
def recommend(movie_title: str):
    if movie_title not in movies['title'].values:
        raise HTTPException(status_code=404, detail="Movie not found in database")
    
    index = movies[movies['title'] == movie_title].index[0]
    distances = similarity[index]
    movies_list = sorted(list(enumerate(distances)), key=lambda x: x[1], reverse=True)[1:6]
    
    recommended_movies = []
    for i in movies_list:
        recommended_movies.append({
            "movie_id": int(movies.iloc[i[0]].movie_id),
            "title": movies.iloc[i[0]].title
        })
        
    return {"recommended_movies": recommended_movies}