import matplotlib.pyplot as plt
import os

def createGraphic(*, data, xLabel, yLabel, title, limit, lines, name_network):
    
    """
    Função para criar gráficos relacionados às distribuições de graus
    """

    if not os.path.exists(f'graphics/{name_network}'): os.makedirs(f'graphics/{name_network}')

    fig, axs = plt.subplots(nrows = 1, ncols = 2, figsize=(12, 4))

    axs[0].scatter(range(1,len(data)+1, 1), data, s = 3, marker = '.')
    axs[0].set_xlabel(xLabel)
    axs[0].set_ylabel(yLabel)
    axs[0].set_title(title)
    axs[0].set_ylim(0, max(data)+limit)
    if lines == True: axs[0].plot(range(1, len(data)+1, 1), data, color = 'black', linestyle = '-', alpha = 0.1)

    axs[1].scatter(range(1,len(data)+1, 1), data, s = 3, marker = '.')
    axs[1].set_xscale('log')
    axs[1].set_yscale('log')
    axs[1].set_xlabel(xLabel)
    axs[1].set_ylabel(yLabel)
    axs[1].set_title(f'{title} (loglog)')

    plt.tight_layout()

    plt.savefig(f'graphics/{name_network}/{title.replace(" ", "_").lower()}.png', dpi = 300,  bbox_inches = 'tight', pad_inches = 0.1)
    plt.show()

    plt.close()

def createGraphicCentrality(*, data, title, name_network):
    
    """
    Função para criar um gráfico de frequência de centralidades
    """

    if not os.path.exists(f'graphics/{name_network}'): os.makedirs(f'graphics/{name_network}')

    analysis_centrality = {'value': [], 'frequency': []}
    values = list(data.values())
    values.sort(reverse = True)
    for value in values:
        if value not in analysis_centrality['value']:
            analysis_centrality['value'].append(value)
            analysis_centrality['frequency'].append(values.count(value))

    plt.scatter(analysis_centrality['value'], analysis_centrality['frequency'], s = 2, marker = '.')
    plt.xlabel('Valor')
    plt.ylabel('Frequência')
    plt.title(title)
    plt.tight_layout()

    plt.savefig(f'graphics/{name_network}/valores_{title.replace(" ", "_").lower()}.png', dpi = 300,  bbox_inches = 'tight', pad_inches = 0.1)
    plt.show()

    plt.close()

    return analysis_centrality

def createRankingCentrality(*, df, centrality, network, title, name_network):
  
    """
    Função para rankear os vértices com maiores centralidades na rede
    """

    if not os.path.exists(f'graphics/{name_network}'): os.makedirs(f'graphics/{name_network}')

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

    plt.savefig(f'graphics/{name_network}/ranking_{title.replace(" ", "_").lower()}.png', dpi = 300,  bbox_inches = 'tight', pad_inches = 0.1)
    plt.show()

    plt.close()