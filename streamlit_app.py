import streamlit as st
import pandas as pd
from PIL import Image

#Todo1
# Function to recommend music genre based on user input
def recommend_genre(popularity, tempo):
    # Dummy logic, replace with your actual genre prediction logic
    if tempo == 'High' and popularity > 120:
        return 'Rock'
    elif tempo == 'Low' and popularity < 100:
        return 'Classical'
    else:
        return 'Pop'

#Todo2
# Function to get top songs for a given genre (dummy data, replace with your data)
def get_top_songs(genre):
    # Dummy data, replace with your actual data
    data = {
        'Track Name': ['Song 1', 'Song 2', 'Song 3', 'Song 4', 'Song 5', 'Song 6', 'Song 7', 'Song 8', 'Song 9', 'Song 10'],
        'Artist': ['Artist 1', 'Artist 2', 'Artist 3', 'Artist 4', 'Artist 5', 'Artist 6', 'Artist 7', 'Artist 8', 'Artist 9', 'Artist 10'],
        'Year': [2020, 2019, 2018, 2017, 2016, 2015, 2014, 2013, 2012, 2011],
        'YouTube Link': ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
    }
    df = pd.DataFrame(data)
    return df

# Streamlit UI
st.title('Music Recommender')

# User input for Popularity (categorical)
tempo = st.selectbox('tempo:', ['Low', 'Medium', 'High'])

# User input for key (categorical)
key = st.selectbox('key:', ['Low', 'Medium', 'High'])

# User input for mode (categorical)
mode = st.selectbox('mode:', ['Low', 'Medium', 'High'])

# User input for popularity (numeric)
popularity = st.slider('popularity:', min_value=60, max_value=180, value=120, step=10)

# User input for acousticness (numeric)
acousticness = st.slider('acousticness:', min_value=60, max_value=180, value=120, step=10)

# User input for danceability (numeric)
danceability = st.slider('danceability:', min_value=60, max_value=180, value=120, step=10)

# User input for duration_ms (numeric)
duration_ms = st.slider('duration_ms:', min_value=60, max_value=180, value=120, step=10)

# User input for energy (numeric)
energy = st.slider('energy:', min_value=60, max_value=180, value=120, step=10)

# User input for instrumentalness (numeric)
instrumentalness = st.slider('instrumentalness:', min_value=60, max_value=180, value=120, step=5)

# User input for liveness (numeric)
liveness = st.slider('liveness:', min_value=60, max_value=180, value=120, step=10)

# User input for loudness (numeric)
loudness = st.slider('loudness:', min_value=60, max_value=180, value=120, step=10)

# User input for speechiness (numeric)
speechiness = st.slider('speechiness:', min_value=60, max_value=180, value=120, step=10)

# User input for positivity (numeric)
positivity = st.slider('positivity:', min_value=60, max_value=180, value=120, step=5)

# Submit button
if st.button('Submit'):
    # Get recommended genre
    recommended_genre = recommend_genre(popularity, tempo)

    # Display recommended genre
    st.success(f'Recommended Genre: {recommended_genre}')

    # Get and display top songs for the recommended genre
    top_songs = get_top_songs(recommended_genre)

    # Display a grid of 10 songs with thumbnail images
    thumbnail_path = "images/music-speakers-background.jpg"
    thumbnail_image = Image.open(thumbnail_path)
    youtube_link = "https://youtu.be/1G4isv_Fylg?si=pD0ZHgP5Qer_nXtS"
    for i in range(0, 10, 3):
        col1, col2, col3 = st.columns(3)

        with col1:
            st.image(thumbnail_image, caption=f'{top_songs["Track Name"][i]} - {top_songs["Artist"][i]} ({top_songs["Year"][i]})', use_column_width=True)
            st.write(f'[YouTube Link]({youtube_link})', unsafe_allow_html=True)

        with col2:
            if i + 1 < 10:
                st.image(thumbnail_image, caption=f'{top_songs["Track Name"][i + 1]} - {top_songs["Artist"][i + 1]} ({top_songs["Year"][i + 1]})', use_column_width=True)
                st.write(f'[YouTube Link]({youtube_link})', unsafe_allow_html=True)

        with col3:
            if i + 2 < 10:
                st.image(thumbnail_image, caption=f'{top_songs["Track Name"][i + 2]} - {top_songs["Artist"][i + 2]} ({top_songs["Year"][i + 2]})', use_column_width=True)
                st.write(f'[YouTube Link]({youtube_link})', unsafe_allow_html=True)
