import networkx as nx
from Graph import Graph
from SimpleGraph import SimpleGraph

class BipartiteGraph(Graph):
    def __init__(self):
        super().__init__()
        
    def add_nodes(self, artists, genres):
        self.graph.add_nodes_from(artists, bipartite=0)  # artists are set 0 at bipartite graph
        self.graph.add_nodes_from(genres, bipartite=1)
        
    def add_edges(self, edges):
        for artist, genre, popularity in edges:
            self.graph.add_edge(artist, genre, weight=popularity)

    def transform_bipartite_into_simple(self, nodes : list):
        graph = nx.bipartite.projected_graph(self.graph, nodes)
        simpleGraph = SimpleGraph()
        simpleGraph.add_nodes(list(graph.nodes(data=True)))
        simpleGraph.add_edges(list(graph.edges(data=True)))
        return simpleGraph