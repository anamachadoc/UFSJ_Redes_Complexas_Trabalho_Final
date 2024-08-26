import networkx as nx
from tqdm import tqdm
import pandas as pd

def createNetowrk(df, name_column):
    network = nx.Graph()
    df[name_column] = df[name_column].fillna('')
    for index, artist_id_node_1 in tqdm(enumerate(df['id'])):
        list_artists_id = (df[name_column].iloc[index]).split(', ')
        if list_artists_id != ['']:
            for artist_id_node_2 in list_artists_id:
                if (artist_id_node_1, artist_id_node_2) not in network.edges and (artist_id_node_2, artist_id_node_1) not in network.edges:
                    network.add_edge(artist_id_node_1, artist_id_node_2)
    return network

def toEdgesList(network, name_network):
    edges_list = list(network.edges())

    df = pd.DataFrame(edges_list)

    df.to_csv(f'../data/{name_network}/{name_network}_edges_list.csv', index=False, header=False)

    return edges_list
