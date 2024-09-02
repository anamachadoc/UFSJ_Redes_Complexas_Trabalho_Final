import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
from tqdm import tqdm
import time
import pickle

client_id = '553a5dc1f98e4b9ba10d7ded08519203'
client_secret = 'a6bbcb7364104c428e95e6ab58d07dbc'
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id = client_id,
                                                           client_secret = client_secret))

artists = pd.read_csv('new_artists.csv')
caminho_arquivo = 'artistas_e_albuns.pkl'

with open(caminho_arquivo, 'rb') as arquivo:
    objeto = pickle.load(arquivo)


with open('mudar.pkl', 'rb') as arquivo:
    itera = pickle.load(arquivo)

artists['albums'] = objeto
colabs = []
print('ok')
for i in tqdm(itera):
    collaborations = set()
    albums = artists['albums'][i]
    for album in albums:
        tracks = sp.album_tracks(album['id'])['items']
        for track in tracks:
            track_artists = [artist['id'] for artist in track['artists']]
            if len(track_artists) > 1:
                for artist in track_artists:
                    if artist != artists['name'][i]:
                        collaborations.add(artist)
    colabs.append(collaborations)
    with open('nova_colab.pkl', 'wb') as file:
        pickle.dump(colabs, file)
    time.sleep(0.3)