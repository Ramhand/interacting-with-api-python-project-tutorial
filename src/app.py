import os
import pandas as pd
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import matplotlib.pyplot as plt

# load the .env file variables
load_dotenv()

SPOTIPY_CLIENT_ID = os.environ.get('SPOTIPY_CLIENT_ID')
SPOTIPY_CLIENT_SECRET = os.environ.get('SPOTIPY_CLIENT_SEC')

mayday_uri = 'spotify:artist:71WhWdsVNTLxsnfe8M3Peh'
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
results = spotify.artist_top_tracks(mayday_uri)
df = pd.DataFrame(results['tracks'])
df = df[['name', 'popularity', 'duration_ms']]
df = df[:3]

plt.scatter(df['duration_ms'], df['popularity'])
plt.show()

# With an apparent difference of less than one second between the first and third most popular songs, but a
# 6 second disparity with the second most popular, it seems pretty clear that there is nowhere near enough
# information to determine a relationship.  But it doesn't appear so.  It is still interesting to note that
# their three most popular songs are within 6 seconds of each other length wise, though.  But that range 
# being 4:39 - 4:45 kinda points towards lack of length being entirely unrelated to popularity.