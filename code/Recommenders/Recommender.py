from abc import ABC, abstractmethod
from Graphs import Graph

class Recommender(ABC):
    def __init__(self, G : Graph):
        self.graph = G
        self.recommended_artists = None

    def convert_recommendations(self, artist_id, artists_ids):
        print(f'Recommended artists based on {artists_ids[artist_id]}:')
        for i, recommendation in enumerate(self.recommended_artists):
            print(f'{i+1}: {artists_ids[recommendation]}')
    
    @abstractmethod
    def make_recommendations(self): ...