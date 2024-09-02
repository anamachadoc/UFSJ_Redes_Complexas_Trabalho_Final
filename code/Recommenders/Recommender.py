from abc import ABC, abstractmethod
from Graphs import Graph

class Recommender(ABC):
    def __init__(self, G : Graph, number_recommendations : int):
        self.graph = G
        self.number_recommendations = number_recommendations
        self.artists_recommendations = None

    def convert_recommendations(self, artist_id, artists_ids):
        print(f'recommended artists based on {artists_ids[artist_id]}:')
        for i, recommendation in enumerate(self.artists_recommendations):
            print(f'{i+1}: {artists_ids[recommendation]}')
    
    @abstractmethod
    def make_recommendations(self): ...