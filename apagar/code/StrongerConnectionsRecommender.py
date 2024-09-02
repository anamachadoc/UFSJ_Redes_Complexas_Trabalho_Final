import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from Graph import Graph

class StrongerConnectionsRecommender:
    def __init__(self, G, x):
        self.graph = G
        self.number_recommendations = x
        self.artists_recommendations = None
    
    def convert_recommendations(self, artist_id, artists_ids):
        print(f'recommended artists based on {artists_ids[artist_id]}:')
        for i, recommendation in enumerate(self.artists_recommendations):
            print(f'{i+1}: {artists_ids[recommendation]}')

    def get_collaborations(self, artist_id):
        sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id='76e709d9b20c4cfd92322dae744a8a24',
                                                         client_secret='ca2ce1227ecf4500a1918025cfcdb2a4'))
        albums = sp.artist_albums(artist_id, album_type='album')['items']
        
        self.collaborations = []
        for album in albums:
            collaborations = set()
            for album in albums:
                tracks = sp.album_tracks(album['id'])['items']
                for track in tracks:
                    track_artists = [artist['id'] for artist in track['artists']]
                    if len(track_artists) > 1:
                        for artist in track_artists:
                            if artist != artist_id: #and artist not in collaborations:
                                collaborations.add(artist)
            self.collaborations.append(collaborations)
        
    def recommend_based_on_connections(self, artist_id, collaborations : bool = False):
        self.artists_recommendations = []
        
        if not self.graph.node_in_graph(artist_id): 
            return print(f'{artist_id} is not in the graph')

        connections = {}
        for artist_id_neighbor in self.graph.get_neighbors(artist_id):
            connections[artist_id_neighbor] = (self.graph.graph[artist_id][artist_id_neighbor]['weight'], self.graph.graph.nodes[artist_id_neighbor]['popularity'])

        if collaborations:
            self.get_collaborations(artist_id)
            for collaboration in self.collaborations:
                for artist_id_collaboration in collaboration:
                    if artist_id_collaboration in connections:
                        weight, popularity = connections[artist_id_collaboration]
                        connections[artist_id_collaboration] = (weight+2, popularity) 
                    elif artist_id_collaboration in self.graph.get_nodes():
                        connections[artist_id_collaboration] = (2, self.graph.graph.nodes[artist_id_collaboration]['popularity']) 

        connections_sorted = dict(sorted(connections.items(), key=lambda item: (item[1][0], item[1][1]), reverse=True))

        for counter, artist_id_neighbor in enumerate(connections_sorted):
            if counter == self.number_recommendations: break
            self.artists_recommendations.append(artist_id_neighbor)
        
        return self.artists_recommendations
