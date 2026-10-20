import pickle
import pandas as pd

class MovieRecommender:
    def __init__(self, movies_path='models/movies.pkl',
                 similarity_path='models/similarity.pkl'):
        
        try:
            self.movies = pickle.load(open(movies_path, 'rb'))
            self.similarity = pickle.load(open(similarity_path, 'rb'))
        except FileNotFoundError:
            print(" Model files not found! Please run train.py 1st.")
            self.movies = None
            self.similarity = None

    def recommend(self, title, top_n=5):
        if self.movies is None:
            return ["Model not loaded. Train first."]

        
        if title not in self.movies['title'].values:
            return []

        idx = self.movies[self.movies['title'] == title].index[0]
        distances = list(enumerate(self.similarity[idx]))
        distances = sorted(distances, key=lambda x: x[1], reverse=True)

        results = []
        for i in distances[1:top_n + 1]:
            results.append(self.movies.iloc[i[0]]['title'])
        return results

if __name__ == "__main__":
    rec = MovieRecommender()
    if rec.movies is not None:
        print(rec.recommend('Avatar'))