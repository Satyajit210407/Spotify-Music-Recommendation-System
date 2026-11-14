import streamlit as st
import pandas as pd
import numpy as np

from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import NearestNeighbors

# -----------------------------
# PAGE CONFIGURATION
# -----------------------------

st.set_page_config(
    page_title="Spotify Music Recommender",
    page_icon="🎵",
    layout="wide"
)

# -----------------------------
# CUSTOM DESIGN
# -----------------------------

st.markdown("""
<style>
.stApp {
    background-color: #121212;
    color: white;
}

h1, h2, h3, p, label {
    color: white !important;
}

.stButton button {
    background-color: #1DB954;
    color: white;
    border-radius: 20px;
    border: none;
    font-weight: bold;
}

.song-card {
    background-color: #222222;
    padding: 18px;
    border-radius: 12px;
    margin-bottom: 12px;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# AUDIO FEATURES
# -----------------------------

audio_features = [
    'danceability',
    'energy',
    'acousticness',
    'instrumentalness',
    'liveness',
    'loudness',
    'speechiness',
    'tempo',
    'valence'
]

# -----------------------------
# LOAD DATA AND MODEL
# -----------------------------

@st.cache_resource
def load_model():

    df = pd.read_csv("SpotifyFeatures.csv")

    df = df.dropna(
        subset=['track_id', 'track_name', 'artist_name']
    )

    df = df.drop_duplicates(
        subset=['track_id']
    ).reset_index(drop=True)

    for col in audio_features:
        df[col] = pd.to_numeric(
            df[col], errors='coerce'
        )

        df[col] = df[col].fillna(df[col].median())

    scaler = StandardScaler()

    features_scaled = scaler.fit_transform(
        df[audio_features]
    )

    model = NearestNeighbors(
        metric='cosine',
        algorithm='brute',
        n_neighbors=11,
        n_jobs=-1
    )

    model.fit(features_scaled)

    return df, features_scaled, model


df, features_scaled, model = load_model()

# -----------------------------
# APPLICATION HEADER
# -----------------------------

st.title("🎵 Spotify Music Recommender")

st.write(
    "Discover songs based on their musical characteristics."
)

st.divider()

# -----------------------------
# SEARCH SONG
# -----------------------------

st.subheader("Find Your Favourite Song")

song_name = st.text_input(
    "Enter Song Name",
    placeholder="Search for a song..."
)

if song_name:

    matches = df[
        df['track_name'].str.contains(
            song_name,
            case=False,
            na=False,
            regex=False
        )
    ]

    if matches.empty:

        st.warning("No matching songs found.")

    else:

        options = {
            f"{row.track_name} — {row.artist_name}": row.Index
            for row in matches.itertuples()
        }

        selected_song = st.selectbox(
            "Select a song",
            list(options.keys())
        )

        if st.button("Recommend Songs"):

            song_index = options[selected_song]

            song = df.iloc[song_index]

            st.success(
                f"Recommendations for {song['track_name']}"
            )

            col1, col2, col3 = st.columns(3)

            col1.metric("Artist", song['artist_name'])
            col2.metric("Genre", song['genre'])
            col3.metric("Popularity", song['popularity'])

            distances, indices = model.kneighbors(
                features_scaled[song_index].reshape(1, -1),
                n_neighbors=11
            )

            recommended_indices = indices[0][1:]
            recommended_distances = distances[0][1:]

            recommendations = df.iloc[
                recommended_indices
            ][
                ['track_name', 'artist_name', 'genre', 'popularity']
            ].copy()

            recommendations['Similarity'] = (
                (1 - recommended_distances) * 100
            ).round(2)

            st.divider()
            st.subheader("🎧 Recommended Songs")

            st.dataframe(
                recommendations.reset_index(drop=True),
                use_container_width=True,
                hide_index=True
            )

# -----------------------------
# FOOTER
# -----------------------------

st.divider()

st.caption(
    "Built using Python, Pandas, Scikit-learn and Streamlit."
)
