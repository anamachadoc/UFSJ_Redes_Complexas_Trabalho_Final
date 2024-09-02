import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
from tqdm import tqdm
import time
import pickle

client_id = '94269806d3214e3680c23489795b8e2e'
client_secret = 'f4f4e1036c4a4d70880cd09e878e87bf'
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id = client_id,
                                                           client_secret = client_secret))

artists = pd.read_csv('spotify_artists.csv')

filtered_artists = artists[artists['popularity'] >= 65]
filtered_artists.reset_index(drop=True, inplace=True)
list_album = []

for i in tqdm(range(len(filtered_artists))):
    albums = sp.artist_albums(filtered_artists['id'][i], album_type='album')['items']
    name = filtered_artists['name'][i]
    list_album.append(albums)
    with open('artistas_e_albuns.pkl', 'wb') as file:
        pickle.dump(list_album, file)
    time.sleep(1.5)

filtered_artists['albums'] = list_album
csv_filename = 'saved_artists.csv'
filtered_artists.to_csv(csv_filename, index=False)

