class Artist:
    def __init__(self, G, id):
        self.id = id
        if G.node_in_graph(id):
            self.genres = list(G.get_neighbors(self.id))
        else:
            self.genres = None
        