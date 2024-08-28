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
        if node in self.graph:
            return True
    
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
            print(f"Size of the largest component: {max_size}")
        