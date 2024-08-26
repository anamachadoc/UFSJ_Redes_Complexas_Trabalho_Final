import matplotlib.pyplot as plt
import os

def createGraphic(*, data, xLabel, yLabel, title, limit, lines, name_network):
    
    """
    Função para criar gráficos relacionados às distribuições de graus
    """

    if not os.path.exists(f'../data/real/{name_network}/graphics'): os.makedirs(f'../data/real/{name_network}/graphics')

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

    plt.savefig(f'../data/real/{name_network}/graphics/{title.replace(" ", "_").lower()}.png', dpi = 300,  bbox_inches = 'tight', pad_inches = 0.1)
    plt.show()

    plt.close()

def createGraphicCentrality(*, data, title, name_network):
    
    """
    Função para criar um gráfico de frequência de centralidades
    """

    if not os.path.exists(f'../data/real/{name_network}/graphics'): os.makedirs(f'../data/real/{name_network}/graphics')

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

    plt.savefig(f'../data/real/{name_network}/graphics/values_{title.replace(" ", "_").lower()}.png', dpi = 300,  bbox_inches = 'tight', pad_inches = 0.1)
    plt.show()

    plt.close()

    return analysis_centrality