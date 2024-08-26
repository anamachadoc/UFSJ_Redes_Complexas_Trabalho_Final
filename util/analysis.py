import networkx as nx
import matplotlib.pyplot as plt
import os

def printInformationAnalysisCentrality(analysis_centrality):
    
    """
    Função para printar informações gerais sobre a centralidade a partir dos dados gerados com a função createGraphicCentrality
    """

    print('Informações gerais sobre os resultados encontrados:')
    print(f'\tQuantidade de valores diferentes para a centralidade em estudo: {len(analysis_centrality["value"])}.')
    print(f'\tO menor valor é {analysis_centrality["value"][len(analysis_centrality["value"])-1]} e sua frequência é {analysis_centrality["frequency"][len(analysis_centrality["value"])-1]}.')
    print(f'\tO maior valor é {analysis_centrality["value"][0]} e sua frequência é {analysis_centrality["frequency"][0]}.')


def average_shortest_path_length(network):

    """
    Cálculo utilizado para a distância média dado que a biblioteca networkx não o realiza no caso de mais de uma componente. Tal cálculo foi baseado no utilizado pelo Gephi
    """

    components = [network.subgraph(component).copy() for component in nx.connected_components(network)]
    
    total_sum = 0
    total_pairs = 0
    
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
    
def printInformations(network):

    """
    Função para printar as informações gerais da estrutura de uma rede
    """
    
    print(f'Quantidade de vértices: {network.number_of_nodes()}')
    print(f'Quantidade de arestas: {network.number_of_edges()}')
    print(f'Quantidade de componentes: {nx.number_connected_components(network)}')
    print(f'Menor grau da rede: {min(dict(network.degree()).values())}')
    print(f'Maior grau da rede: {max(dict(network.degree()).values())}')
    print(f'Grau médio da rede: {sum(dict(network.degree()).values())/network.number_of_nodes()}')
    print(f'Densidade da rede: {nx.density(network)}')
    print(f'Distância média: {average_shortest_path_length(network)}')
    
    selected_nodes = []
    for node in network.nodes():
        if network.degree(node) > 1:
            selected_nodes.append(node)
    clustering_coefficient = nx.clustering(network, nodes = selected_nodes)
    average_clustering_coefficient = nx.average_clustering(network, nodes = selected_nodes, count_zeros = True)
    
    print(f'Coeficiente de clustering médio: {average_clustering_coefficient} (apenas {len(selected_nodes)/network.number_of_nodes():.2%} da rede foi considerada no cálculo, que que possuem grau maior do que um)')

    clustering_nodes = [(round(clustering_coefficient[node],4), node) if node in selected_nodes else ('-', node) for node in network.nodes()]


def createRankingCentrality(*, df, centrality, network, title, name_network):
  
    """
    Função para rankear os vértices com maiores centralidades na rede
    """

    if not os.path.exists(f'../data/real/{name_network}/graphics'): os.makedirs(f'../data/real/{name_network}/graphics')

    listSingers = []
    listValuesCoefficient = []

    data = [(round(centrality[node], 4), node) for node in centrality.keys()]
    data = sorted(data, reverse = True)[:20]

    df_id_list = df['id'].to_list()

    for valueCoefficient, singer_id in data:
        index = df_id_list.index(singer_id)
        singer = df['name'].iloc[index]
        listSingers.append(str(singer) + f' ({network.degree[singer_id]})')
        listValuesCoefficient.append(valueCoefficient)

    plt.barh(listSingers, listValuesCoefficient)
    plt.xlabel('Valor da Centralidade')
    plt.ylabel('Vértice (grau)')
    for index, value in enumerate(listValuesCoefficient):
        plt.text(value, index, str(f'{value:.4f}'), ha = 'right', va = 'center')
        plt.title(title)

    plt.savefig(f'../data/real/{name_network}/graphics/ranking_{title.replace(" ", "_").lower()}.png', dpi = 300,  bbox_inches = 'tight', pad_inches = 0.1)
    plt.show()

    plt.close()

def degreeDistribution(network):
    frequencies_of_degrees = nx.degree_histogram(network)
    probability_of_degrees = [degree/(nx.number_of_nodes(network)) for degree in frequencies_of_degrees]
    accumulated_probability_of_degress = [sum(probability_of_degrees[index:]) for index in range(len(probability_of_degrees))]

    return frequencies_of_degrees, probability_of_degrees, accumulated_probability_of_degress

def calculateCentralities(network):
    degree_centrality = nx.degree_centrality(network)
    eigenvector_centrality = nx.eigenvector_centrality(network, max_iter=1000)

    return degree_centrality, eigenvector_centrality


    