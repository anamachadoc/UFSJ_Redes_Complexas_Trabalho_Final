from Graph import Graph

class SimpleGraph(Graph):
    def __init__(self):
        super().__init__()
        
    def add_nodes(self, artists : list):
        self.graph.add_nodes_from(artists)
        
    def add_edges(self, edges : list):
        for artist_node_1, artist_node_2, weight in edges:
            self.graph.add_edge(artist_node_1, artist_node_2, weight=weight)
