import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json

class Spotify:

    __client_id = None
    __client_secret = None
    __sp = None

    @classmethod
    def initialize(cls, credentials_file):
        with open(credentials_file, 'r') as file:
            credentials = json.load(file)
            cls.__client_id = credentials.get("Client_ID")
            cls.__client_secret = credentials.get("Client_secret")

        cls.__sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
            client_id=cls.__client_id, 
            client_secret=cls.__client_secret))
        
    @classmethod
    def artists_related_to(cls, artist_id : str):
        if cls.__sp is None:
            raise ValueError("SpotifyClient has not been initialized. Call 'initialize' first.")
        
        return cls.__sp.artist_related_artists(artist_id)
    
    @classmethod
    def search(cls, q : str, type : str = 'artist', limit : int = 50, offset: int = 0):
        if cls.__sp is None:
            raise ValueError("SpotifyClient has not been initialized. Call 'initialize' first.")
        
        return cls.__sp.search(q=q, type=type, limit=limit, offset=offset)
    
    @classmethod
    def compare_with_spotify_recommendation(cls, artists_id, recommendations):
        if cls.__sp is None:
            raise ValueError("SpotifyClient has not been initialized. Call 'initialize' first.")
        
        spotify_recommendation = cls.__sp.artist_related_artists(artists_id)
        spotify_recommendation = [artist['name'] for artist in spotify_recommendation['artists']]
        
        counter=0
        for artist in spotify_recommendation:
            if artist in recommendations:
                counter+=1
        
        return counter/len(spotify_recommendation)
    
    @classmethod
    def get_collaborations(cls, artist_id):
        if cls.__sp is None:
            raise ValueError("SpotifyClient has not been initialized. Call 'initialize' first.")
        
        albums = cls.__sp.artist_albums(artist_id, album_type='album')['items']
        
        collaborations = set()

        for album in albums:
            for album in albums:
                tracks = cls.__sp.album_tracks(album['id'])['items']
                for track in tracks:
                    track_artists = [artist['id'] for artist in track['artists']]
                    if len(track_artists) > 1:
                        for artist in track_artists:
                            if artist != artist_id:
                                collaborations.add(artist)

        return list(collaborations)