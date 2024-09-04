import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

class Spotify:

    __client_id = 'bf5aacb1d35a484cbd7a31afc2b2a821'
    __client_secret='dca1eb5cca1643c1bf4087a6133a166b'
    __sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=__client_id, 
                                                                        client_secret=__client_secret))
    @classmethod
    def artists_related_to(self, artist_id : str):
        return self.__sp.artist_related_artists(artist_id)
    
    @classmethod
    def search(self, q : str, type : str = 'artist', limit : int = 50, offset: int = 0):
        return self.__sp.search(q=q, type=type, limit=limit, offset=offset)
    
    @classmethod
    def compare_with_spotify_recommendation(self, artists_id, recommendations):
        spotify_recommendation = self.__sp.artist_related_artists(artists_id)
        spotify_recommendation = [artist['name'] for artist in spotify_recommendation['artists']]
        
        counter=0
        for artist in spotify_recommendation:
            if artist in recommendations:
                counter+=1
        
        return counter/len(spotify_recommendation)
    
    @classmethod
    def get_collaborations(self, artist_id):
        
        albums = self.__sp.artist_albums(artist_id, album_type='album')['items']
        
        collaborations = set()

        for album in albums:
            for album in albums:
                tracks = self.__sp.album_tracks(album['id'])['items']
                for track in tracks:
                    track_artists = [artist['id'] for artist in track['artists']]
                    if len(track_artists) > 1:
                        for artist in track_artists:
                            if artist != artist_id: #and artist not in collaborations:
                                collaborations.add(artist)

        return list(collaborations)