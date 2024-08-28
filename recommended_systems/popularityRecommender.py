from artist import Artist

class PopularityRecommender:
    def __init__(self, G, x):
        self.graph = G
        self.number_recommendations = x
        self.artists_recommendations = None
    
    def create_artist(self, artist_id):
        artist = Artist(self.graph, artist_id)
        return artist
    
    def convert_recommendations(self, artist_id, artists_ids):
        print(f'recommended artists based on {artists_ids[artist_id]}:')
        for i, recommendation in enumerate(self.artists_recommendations):
            print(f'{i+1}: {artists_ids[recommendation[0]]} - {recommendation[1]}')
        
    def recommend_based_on_popularity(self, artist_id):
        self.artists_recommendations = []
        artist = self.create_artist(artist_id)
        
        if not self.graph.node_in_graph(artist.id): 
            return print(f'{artist.id} is not in the graph')
        if not artist.genres:
            return f"Artist '{artist}' is not associated with any genre."
        print(artist.genres)
        num_genres = len(artist.genres)
        
        recommendations_per_genre = self.number_recommendations // num_genres
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
            self.artists_recommendations.extend(artists)
        
        self.artists_recommendations = list(set((self.artists_recommendations)))
        
        while len(self.artists_recommendations) != self.number_recommendations:
            insufficient_artists = False
            artists = []
            for genre in artist.genres:
                artists_genre = self.graph.get_neighbors(genre)
                
                for a in artists_genre:
                    if not (any(t[0] == a for t in self.artists_recommendations)) and a != artist:
                        t = (a, self.graph.get_weight_edge(genre, a))
                        artists.append(t)
                            
            artists = list(set(artists))
            if len(artists) < self.number_recommendations - len(self.artists_recommendations):
                insufficient_artists = True
                
            artists.sort(key=lambda x: x[1])
            self.artists_recommendations.extend(artists[:(self.number_recommendations - len(self.artists_recommendations))])
            self.artists_recommendations = list(set(self.artists_recommendations))
            
            if  insufficient_artists:
                print(f'There are no {self.number_recommendations} artists to be returned')
                break
        self.artists_recommendations.sort(key=lambda x: x[1], reverse=True)
        return self.artists_recommendations
