# This is a sample Python script.
import requests
import spotipy
from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyOAuth

# Taking the credentials from spotify Developer settings and pasitng/exporting them here
CLIENT_ID = 'a3c0c8cf624844fca3b7c216f615a034'
CLIENT_SECRET = 'f92d517404a2434fad3e97c88d45bee8'
URL = 'https://www.billboard.com/charts/hot-100/'
# we define the scope that we will nee to work with user and private playlist
scope = 'playlist-modify-private'
# taking user input in the format of a date to search songs from the billboard site from that exact date
user_input = input('What year would you like to travel to(in YYYY-MM-DD format): ')
year = user_input.split('-')[0]
# here we will collect the id-s of all the songs we find through the spotify API
song_uris = []
# we take the response from the main page of the billboards
response = requests.get(f"{URL}/{user_input}/")
response.raise_for_status()
data = response.text
# we scrape the data
soup = BeautifulSoup(data, 'html.parser')
top_songs = soup.select('li.o-chart-results-list__item > h3')

# this is how we use spotypy library
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    scope=scope,
    redirect_uri='http://example.com',
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    show_dialog=True,
    cache_path='.cache',
    username='21g2tasgyupmdflui2suylwjq'

))
user_id = sp.current_user()['id']



for song in top_songs:
    track = song.text.strip()
    search = sp.search(q=f'track:{track} year:{year}', type='track')
    try:
        uri = search["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")
playlist = sp.user_playlist_create(user_id, name=f"{user_input} Billboard 100", public=False)

sp.playlist_add_items(playlist_id=playlist['id'], items=song_uris)
