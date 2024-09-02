import networkx as nx
from abc import ABC, abstractmethod

class Graph(ABC):
    def __init__(self):
        self.graph = nx.Graph()

    @abstractmethod
    def add_nodes(self): ...
    
    @abstractmethod
    def add_edges(self): ...
    
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
    
    def get_average_distance(self): # based on the calculation done by Gephi
        
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
        
    def get_average_clustering_coefficient(self):
        
        selected_nodes = []
        
        for node in self.get_nodes():
            if self.get_degree(node) > 1:
                selected_nodes.append(node)
        
        average_clustering_coefficient = nx.average_clustering(self.graph, nodes = selected_nodes, count_zeros = True, weight='weight')
        percentage_of_considered_nodes = len(selected_nodes)/self.get_number_of_nodes()

        return average_clustering_coefficient, percentage_of_considered_nodes

    def get_node_clustering_coefficient(self, node):
        
        selected_nodes = []
        
        for node in self.get_nodes():
            if self.get_degree(node) > 1:
                selected_nodes.append(node)
        
        if node not in selected_nodes:
            return 0
        else:
            clustering_coefficient = nx.clustering(self.graph, nodes = selected_nodes, weight='weight')
            return clustering_coefficient[node]
        
    def get_neighbors(self, node):
        return list(self.graph.neighbors(node))
    
    #def get_weight_edge(self, genre, artist):
    def get_weight_edge(self, node_1, node_2):
        return self.graph[node_1][node_2]['weight']
        
    '''
    def print_graph_info(self):
        print(f"Number of nodes: {self.graph.number_of_nodes()}")
        print(f"Number of edges: {self.graph.number_of_edges()}")
        
        is_connected = nx.is_connected(self.graph)
        print(f"Is the graph connected? {is_connected}")
        if not is_connected:
            components = list(nx.connected_components(self.graph))
            print(f"Number of connected components: {len(components)}")
            
            component_sizes = [len(component) for component in components]
            min_size = min(component_sizes)
            max_size = max(component_sizes)
            print(f"Size of the smallest component: {min_size}")
            print(f"Size of the largest component: {max_size}")'''
        