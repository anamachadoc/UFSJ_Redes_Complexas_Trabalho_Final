from Artists.Artist import Artist
from Recommender import Recommender

class PopularityRecommender(Recommender):
    def __init__(self, G):
        super().__init__(G)

    def create_artist(self, artist_id):
        artist = Artist(self.graph, artist_id)
        return artist
    
    def make_recommendations(self, artist_id, number_recommendations):
        self.recommended_artists = []
        artist = self.create_artist(artist_id)
        
        if not self.graph.node_in_graph(artist.id): 
            return print(f'{artist.id} is not in the graph')
        if not artist.genres:
            return f"Artist '{artist}' is not associated with any genre."
        num_genres = len(artist.genres)
        
        recommendations_per_genre = number_recommendations // num_genres
        recommendations = {genre: [] for genre in artist.genres}
        
        for genre in artist.genres:
            genre_artists = self.graph.get_neighbors(genre)
            sorted_artists = sorted(
                [(a, self.graph.get_weight_edge(genre, a)) for a in genre_artists if a != artist.id],
                key=lambda a: a[1], 
                reverse=True
            )
            recommendations[genre] = sorted_artists[:recommendations_per_genre]

        for genre, artists in recommendations.items():
            self.recommended_artists.extend(artists)
        
        self.recommended_artists = list(set((self.recommended_artists)))
        
        while len(self.recommended_artists) != number_recommendations:
            insufficient_artists = False
            artists = []
            for genre in artist.genres:
                artists_genre = self.graph.get_neighbors(genre)
                
                for a in artists_genre:
                    if not (any(t[0] == a for t in self.recommended_artists)) and a != artist:
                        t = (a, self.graph.get_weight_edge(genre, a))
                        artists.append(t)
                            
            artists = list(set(artists))
            if len(artists) < number_recommendations - len(self.recommended_artists):
                insufficient_artists = True
                
            artists.sort(key=lambda x: x[1])
            self.recommended_artists.extend(artists[:(number_recommendations - len(self.recommended_artists))])
            self.recommended_artists = list(set(self.recommended_artists))
            
            if insufficient_artists:
                #print(f'There are no {number_recommendations} artists to be returned')
                break
        self.recommended_artists.sort(key=lambda x: x[1], reverse=True)
        self.recommended_artists = [artist_id for artist_id, _ in self.recommended_artists]

        return self.recommended_artists
