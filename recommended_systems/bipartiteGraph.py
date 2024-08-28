from graph import Graph

class BipartiteGraph(Graph):
    def __init__(self):
        super().__init__()
        
    def add_nodes(self, artists, genres):
        self.graph.add_nodes_from(artists, bipartite=0)  # artists are set 0 at bipartite graph
        self.graph.add_nodes_from(genres, bipartite=1)
        
    def add_edges(self, edges):
        for artist, genre, popularity in edges:
            self.graph.add_edge(artist, genre, weight=popularity)
            
    def get_neighbors(self, node):
        return list(self.graph.neighbors(node))
    
    def get_weight_edge(self, genre, artist):
        return self.graph[genre][artist]['weight']
    
