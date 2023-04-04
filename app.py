import streamlit as st
import pandas as pd

# Load the dataset
df = pd.read_csv('data/Spotify_Youtube.csv')

# Display a table with the most interesting columns
interesting_cols = ['Artist', 'Track', 'Album',]
st.write("Table of Artists and songs:")
st.write(df[interesting_cols])

# Radio buttons
st.write("Select an Artist:")
artist_options = df['Artist'].unique()[:20]  # Only show the first 20 artists
artist = st.radio("", artist_options)

# Text box
st.write("Enter a song name:")
song_name = st.text_input("Song Name")

# Text field
st.write("Enter your comment:")
comment = st.text_area("Comment")

# Display the inputs
st.write("Your inputs:")
st.write("Artist:", artist)
st.write("Song Name:", song_name)
st.write("Comment:", comment)
