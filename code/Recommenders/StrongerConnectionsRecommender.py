from Spotify import Spotify as sp
from Recommender import Recommender

class StrongerConnectionsRecommender(Recommender):
    def __init__(self, G, number_recommendations):
        super().__init__(G, number_recommendations)
        
    def make_recommendations(self, artist_id, collaborations : bool = False):
        self.artists_recommendations = []
        
        if not self.graph.node_in_graph(artist_id): 
            return print(f'{artist_id} is not in the graph')

        connections = {}
        for artist_id_neighbor in self.graph.get_neighbors(artist_id):
            connections[artist_id_neighbor] = (self.graph.graph[artist_id][artist_id_neighbor]['weight'], self.graph.graph.nodes[artist_id_neighbor]['popularity'])

        if collaborations:
            collaborations_list = sp.get_collaborations(artist_id)
            for collaboration in collaborations_list:
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
