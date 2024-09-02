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