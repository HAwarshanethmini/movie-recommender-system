import pickle
from huggingface_hub import hf_hub_download

class MovieRecommender:
    def __init__(self, movies_path='models/movies.pkl'):
        try:
            # Load movies list from local
            self.movies = pickle.load(open(movies_path, 'rb'))
            
            # Download similarity matrix from Hugging Face
            print("Downloading similarity.pkl from Hugging Face...")
            hf_path = hf_hub_download(
                repo_id="WNethmini/movie-recommender-model", 
                filename="similarity.pkl"
            )
            self.similarity = pickle.load(open(hf_path, 'rb'))
            print("Models loaded successfully!")
            
        except Exception as e:
            print(f"Error loading models: {e}")
            self.movies = None
            self.similarity = None

    def recommend(self, title, top_n=5):
        if self.movies is None or self.similarity is None:
            return ["Model not loaded. Please check your files."]

        title_lower = title.lower().strip()
        found_idx = -1

        # Search through the list to find the matching movie dictionary
        for i, movie in enumerate(self.movies):
            # Check if the item is a dictionary and contains the 'title' key
            if isinstance(movie, dict) and 'title' in movie:
                if str(movie['title']).lower().strip() == title_lower:
                    found_idx = i
                    break
            # If it's just a string, check it directly
            elif isinstance(movie, str):
                if movie.lower().strip() == title_lower:
                    found_idx = i
                    break

        if found_idx == -1:
            return [] # Movie not found

        # Get similarity scores for that movie
        distances = list(enumerate(self.similarity[found_idx]))
        distances = sorted(distances, key=lambda x: x[1], reverse=True)

        results = []
        for i in distances[1:top_n + 1]:
            movie_item = self.movies[i[0]]
            
            # Extract the title whether it's a dict or a string
            if isinstance(movie_item, dict) and 'title' in movie_item:
                results.append(movie_item['title'])
            else:
                results.append(movie_item)
                
        return results