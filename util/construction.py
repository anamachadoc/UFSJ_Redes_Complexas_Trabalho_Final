import networkx as nx
from tqdm import tqdm
import pandas as pd
import os

def createNetowrk(df, name_column):
    network = nx.Graph()
    df[name_column] = df[name_column].fillna('')
    for index, artist_id_node_1 in tqdm(enumerate(df['id'])):
        list_artists_id = (df[name_column].iloc[index]).split(', ')
        if list_artists_id != ['']:
            for artist_id_node_2 in list_artists_id:
                if (artist_id_node_1, artist_id_node_2) not in network.edges and (artist_id_node_2, artist_id_node_1) not in network.edges:
                    network.add_edge(artist_id_node_1, artist_id_node_2)
        elif network.has_node(artist_id_node_1) == False:
            network.add_node(artist_id_node_1)
    return network

def get_genres_artists(df):
    genres = {}
    genres['nan'] = []
    for i in range(len(df)):
        if type(df['genres'][i]) != float: # nan
            #genres_artist = [item.strip() for item in df['genres'][i].split(',')]
            genres_artist = df['genres'][i].split(', ')
            for g in genres_artist:
                if g not in genres.keys():
                    genres[g] = [df['id'][i]]
                else:
                    genres[g].append(df['id'][i])
        else:
            genres['nan'].append(df['id'][i])
    return genres

def createNetworkGenres(df):

    genres = get_genres_artists(df)

    network = nx.Graph()
    
    network.add_nodes_from(genres['nan'])
    del genres['nan']

    for key in genres.keys():
        artists = genres[key]
        if len(artists) != 1:
            for i in range(len(artists)):
                for j in range(i + 1, len(artists)):
                    if (artists[i], artists[j]) not in network.edges and (artists[j], artists[i]) not in network.edges:
                        network.add_edge(artists[i], artists[j])
        elif network.has_node(artists[0]) == False:
            network.add_node(artists[0])   

    return network

def toEdgesList(network, name_network):

    if not os.path.exists(f'data/{name_network}/{name_network}_edges_list.csv'):

        edges_list = list(network.edges())

        df = pd.DataFrame(edges_list)

        df.to_csv(f'data/{name_network}/{name_network}_edges_list.csv', index=False, header=False)