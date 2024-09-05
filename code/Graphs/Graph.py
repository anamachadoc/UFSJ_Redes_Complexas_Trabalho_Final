import networkx as nx
from abc import ABC, abstractmethod

class Graph(ABC):
    def __init__(self):
        self.graph = nx.Graph()

    @abstractmethod
    def add_nodes(self): ...
    
    @abstractmethod
    def add_edges(self): ...

    def get_artist_name(self, id):
        return self.graph.nodes[id]['name']

    def get_artist_popularity(self, id):
        return self.graph.nodes[id]['popularity']
    
    def node_in_graph(self, node):
        if node in self.graph: return True
        
    def get_number_of_nodes(self):
        return self.graph.number_of_nodes()
    
    def get_number_of_edges(self):
        return self.graph.number_of_edges()
    
    def get_number_connected_components(self):
        return nx.number_connected_components(self.graph)
    
    def get_connected_components(self):
        return nx.connected_components(self.graph)
    
    def get_degree(self, node = 'all'):
        if node == 'all': return self.graph.degree()
        else: return self.graph.degree(node)
    
    def get_minimum_degree(self):
        return min(dict(self.get_degree()).values())
    
    def get_maximum_degree(self):
        return max(dict(self.get_degree()).values())
    
    def get_average_degree(self):
        return sum(dict(self.get_degree()).values())/self.get_number_of_nodes()
    
    def get_density(self):
        return nx.density(self.graph)
    
    def average_shortest_path_length(self): # based on the calculation done by Gephi
        
        total_sum = 0
        total_pairs = 0
        components = [self.graph.subgraph(component).copy() for component in self.get_connected_components()]

        for component in components:
            n = component.number_of_nodes()
            if n > 1:
                avg_length = nx.average_shortest_path_length(component)
                num_pairs = n * (n - 1) / 2
                total_sum += avg_length * num_pairs
                total_pairs += num_pairs
        
        if total_pairs == 0:
            return 0
        else:
            return total_sum / total_pairs
        
    def get_nodes(self):
        return self.graph.nodes()
        
    def get_average_clustering_coefficient(self, weight=None):
        
        selected_nodes = []
        
        for node in self.get_nodes():
            if self.get_degree(node) > 1:
                selected_nodes.append(node)
        
        average_clustering_coefficient = nx.average_clustering(self.graph, nodes = selected_nodes, count_zeros = True, weight=None)
        percentage_of_considered_nodes = len(selected_nodes)/self.get_number_of_nodes()

        return average_clustering_coefficient, percentage_of_considered_nodes

    def get_node_clustering_coefficient(self, node, weight=None):
        
        selected_nodes = []
        
        for node in self.get_nodes():
            if self.get_degree(node) > 1:
                selected_nodes.append(node)
        
        if node not in selected_nodes:
            return 0
        else:
            clustering_coefficient = nx.clustering(self.graph, nodes = selected_nodes, weight=weight)
            return clustering_coefficient[node]
        
    def get_neighbors(self, node):
        return list(self.graph.neighbors(node))
    
    #def get_weight_edge(self, genre, artist):
    def get_weight_edge(self, node_1, node_2):
        return self.graph[node_1][node_2]['weight']

    def get_louvain_communities(self, weight=None):
        return nx.community.louvain_communities(self.graph, weight=weight, seed=42)
        
    def get_degree_distribution(self):
        frequencies_of_degrees = nx.degree_histogram(self.graph)
        probability_of_degrees = [degree/(nx.number_of_nodes(self.graph)) for degree in frequencies_of_degrees]
        accumulated_probability_of_degress = [sum(probability_of_degrees[index:]) for index in range(len(probability_of_degrees))]
        return frequencies_of_degrees, probability_of_degrees, accumulated_probability_of_degress

    def get_degree_centrality(self):
        return nx.degree_centrality(self.graph)
    
    def get_eigenvector_centrality(self, max_iter : int = 1000, weight : str | None = None):
        return nx.eigenvector_centrality(self.graph, max_iter=max_iter, weight=weight)
    
    def get_closeness_centrality(self, wf_improved : bool = True):
        return nx.closeness(self.graph, wf_improved = wf_improved)
    
    def get_betweenness_centrality(self):
        return nx.betweenness_centrality(self.graph)