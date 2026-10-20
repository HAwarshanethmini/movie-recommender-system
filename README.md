# Movie Recommender System

A content-based movie recommendation system that suggests similar movies based on genre, cast, crew, and plot.

## Tech Stack
- **Python** — Core language
- **Pandas, NumPy** — Data processing
- **scikit-learn** — CountVectorizer & Cosine Similarity
- **FastAPI** — REST API backend
- **Streamlit** — Interactive UI

## How It Works
1. Load TMDB 5000 movie dataset.
2. Create a "soup" of features (genres, keywords, cast, crew, overview).
3. Convert soup to vectors using CountVectorizer.
4. Compute cosine similarity between all movies.
5. Return the top 5 most similar movies.

## How to Run Locally

1. Clone the repository:
   git clone https://github.com/HAwarshanethmini/movie-recommender-system.git
   
2. Install dependencies:
   pip install -r requirements.txt

3. Download the dataset from Kaggle (TMDB 5000) and place the .csv files in the data/ folder.

4. Train the model:
   python src/train.py

5. Run the backend:
   uvicorn app.main:app --reload

6. Run the frontend:
   streamlit run app/ui.py

### Author
   HAwarshanethmini
