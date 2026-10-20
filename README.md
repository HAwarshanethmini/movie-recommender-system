# Movie Recommender System

A content-based movie recommendation system that recommends 5 similar movies based on genre, cast, crew, and plot.

## Live Demo
You can try the live application here: 
**[Click Here to Open the App](https://movie-recommender-system-vcclyldgq5c5cjyvbuynqx.streamlit.app/)**

## Features
- Content-Based Filtering: Recommends movies based on genres, cast, crew, and keywords.
- Fast UI built with Streamlit.
- Uses Hugging Face to store and load the large `similarity.pkl` model file efficiently.

## Tech Stack
- **Frontend:** Streamlit
- **Backend / ML:** Python, Pandas, Scikit-learn
- **Model Storage:** Hugging Face Hub
- **Hosting:** Streamlit Community Cloud

## Project Structure
- `app/ui.py`: The Streamlit frontend interface.
- `src/recommender.py`: The core ML logic that loads the model and recommends movies.
- `src/train.py`: Script used to train the model and generate the `.pkl` files.
- `models/movies.pkl`: Pre-processed movie data.
- `requirements.txt`: Python dependencies.

## How to Run Locally
1. Clone the repository:
   ```bash
   git clone https://github.com/HAwarshanethmini/movie-recommender-system.git

2. Install dependencies:
   ```bash
   pip install -r requirements.txt

3. Run the app:
   ```bash
   streamlit run app/ui.py
   
### Author
   HAwarshanethmini
