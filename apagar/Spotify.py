import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

class Spotify:
    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret
        self.sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id, 
                                                                        client_secret=client_secret))
    
    def artists_related_to(self, artist_id : str):
        return self.sp.artist_related_artists(artist_id)
    
    def compare_with_spotify_recommendation(self, artists_id, recommendations):
        spotify_recommendation = self.sp.artist_related_artists(artists_id)
        spotify_recommendation = [artist['name'] for artist in spotify_recommendation['artists']]
        
        counter=0
        for artist in spotify_recommendation:
            if artist in recommendations:
                counter+=1
        
        return counter/len(spotify_recommendation)

