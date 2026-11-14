# 🎵 Spotify Music Recommendation System

## 📌 Project Overview

The Spotify Music Recommendation System is a Machine Learning project that recommends songs based on their musical characteristics.

The system analyzes audio features such as Danceability, Energy, Acousticness, Instrumentalness, Loudness, Speechiness, Tempo, and Valence to identify similar tracks.

It uses a content-based recommendation approach with Cosine Distance and the NearestNeighbors algorithm.

## 🚀 Features

- Song-based recommendations
- Top 10 similar song suggestions
- Artist and genre information
- Song popularity display
- Audio feature analysis
- Interactive Streamlit application

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Streamlit
- Jupyter Notebook

## 🧠 Machine Learning Approach

1. Data Loading and Exploration
2. Data Cleaning and Preprocessing
3. Exploratory Data Analysis (EDA)
4. Audio Feature Selection
5. Feature Scaling using StandardScaler
6. Cosine Distance Calculation
7. NearestNeighbors Model
8. Music Recommendation
9. Model Evaluation

## 📊 Audio Features

| Feature | Description |
|---|---|
| Danceability | Suitability of a song for dancing |
| Energy | Intensity and activity of a track |
| Acousticness | Acoustic characteristics |
| Instrumentalness | Instrumental content |
| Liveness | Likelihood of a live recording |
| Loudness | Overall loudness |
| Speechiness | Presence of spoken words |
| Tempo | Speed of the song |
| Valence | Musical positivity |

## 📂 Project Structure

```text
Spotify-Music-Recommendation-System/
│
├── Spotify_Music_Recommendation.ipynb
├── Spotify.py
├── SpotifyFeatures.csv
├── README.md
└── requirements.txt
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/Spotify-Music-Recommendation-System.git
```

### 2. Navigate to the project folder

```bash
cd Spotify-Music-Recommendation-System
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit application

```bash
streamlit run Spotify.py
```

## 📦 Requirements

```text
pandas
numpy
matplotlib
seaborn
scikit-learn
streamlit
```

## 📈 Model Evaluation

The recommendation system is inspected using:

- Genre consistency
- Average similarity score
- Audio feature comparison

Similarity scores are calculated from cosine distance:

Similarity = (1 - Cosine Distance) × 100

## 🔮 Future Improvements

- Integrate Spotify API
- Add album artwork
- Improve recommendation diversity
- Add personalized recommendations
- Deploy the application online

## 👨‍💻 Author

**Satyajit Pradhan**

Computer Science Engineering Graduate | Machine Learning Enthusiast

## ⭐ Acknowledgements

This project was developed as a practical learning experience in Python, Machine Learning, Exploratory Data Analysis, and recommendation systems.

If you find this project useful, consider giving the repository a ⭐.
