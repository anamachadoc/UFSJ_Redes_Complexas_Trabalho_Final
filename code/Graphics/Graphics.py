import matplotlib.pyplot as plt
import os
import Graphs.Graph 

class Graphics:
    @classmethod
    def create_graphic_degrees(cls, *, data, xLabel, yLabel, title, limit, lines, name_network='network'):

        if not os.path.exists(f'../graphics/{name_network}'): os.makedirs(f'../graphics/{name_network}')

        fig, axs = plt.subplots(nrows = 1, ncols = 2, figsize=(12, 4))
        
        axs[0].scatter(range(1,len(data)+1, 1), data, s = 3, marker = '.', color='black')
        axs[0].set_xlabel(xLabel, fontsize=12)
        axs[0].set_ylabel(yLabel, fontsize=12)
        axs[0].set_title(title, fontsize=12)
        axs[0].set_ylim(0, max(data)+limit)
        if lines == True: axs[0].plot(range(1, len(data)+1, 1), data, color = 'black', linestyle = '-', alpha = 0.1)

        axs[1].scatter(range(1,len(data)+1, 1), data, s = 3, marker = '.', color='black')
        axs[1].set_xscale('log')
        axs[1].set_yscale('log')
        axs[1].set_xlabel(xLabel, fontsize=12)
        axs[1].set_ylabel(yLabel, fontsize=12)
        axs[1].set_title(f'{title} (loglog)', fontsize=12)
        
        plt.xticks(fontsize=12)
        plt.yticks(fontsize=12)
        plt.tight_layout()

        plt.savefig(f'../graphics/{name_network}/{title.replace(" ", "_").lower()}.png', dpi = 300,  bbox_inches = 'tight', pad_inches = 0.1)
        plt.show()

        plt.close()

    @classmethod
    def create_graphic_centrality(cls, *, data, title, name_network='network'):

        if not os.path.exists(f'../graphics/{name_network}'): os.makedirs(f'../graphics/{name_network}')

        analysis_centrality = {'value': [], 'frequency': []}
        values = list(data.values())
        values.sort(reverse = True)
        for value in values:
            if value not in analysis_centrality['value']:
                analysis_centrality['value'].append(value)
                analysis_centrality['frequency'].append(values.count(value))

        plt.scatter(analysis_centrality['value'], analysis_centrality['frequency'], s = 2, marker = '.', color = 'black')
        plt.xlabel('Valor')
        plt.ylabel('Frequência')
        plt.title(title)
        plt.tight_layout()

        plt.savefig(f'../graphics/{name_network}/valores_{title.replace("(", "").replace(")", "").replace(" ", "_").lower()}.png', dpi = 300,  bbox_inches = 'tight', pad_inches = 0.1)
        
        plt.show()
        plt.close()

        return analysis_centrality

    @classmethod
    def create_ranking_centrality(cls, *, centrality, graph, title, name_network='network', label = 'degree'):

        if not os.path.exists(f'../graphics/{name_network}'): os.makedirs(f'../graphics/{name_network}')

        listArtists = []
        listValuesCoefficient = []

        data = [(round(centrality[node], 4), node) for node in centrality.keys()]
        data = sorted(data, reverse = True)[:20]

        for valueCoefficient, artist_id in data:
            artist_name = graph.graph.nodes[artist_id]['name']
            if label == 'degree': listArtists.append(str(artist_name) + f' ({graph.get_degree(artist_id)})')
            if label == 'genre': listArtists.append(str(artist_name) + f' ({graph.graph.nodes[artist_id]["genre"]})')
            listValuesCoefficient.append(valueCoefficient)

        fig, ax = plt.subplots(figsize=(18, 12))
        
        ax.barh(listArtists, listValuesCoefficient, color = 'black')
        ax.set_xlabel('Valor da Centralidade', fontsize=16)
        if label == 'degree': ax.set_ylabel('Vértice (grau)', fontsize=16)
        if label == 'genre': ax.set_ylabel('Vértice (gênero)', fontsize=16)
        for index, value in enumerate(listValuesCoefficient):
            ax.text(value, index, str(f'{value:.4f}'), ha = 'right', va = 'center', fontsize=16)
            ax.set_title(title, fontsize=16)
        
        plt.xticks(fontsize=16)
        plt.yticks(fontsize=16)
        plt.tight_layout()

        plt.savefig(f'../graphics/{name_network}/{title.replace("(", "").replace(")", "").replace(" ", "_").lower()}.png', dpi = 300,  bbox_inches = 'tight', pad_inches = 0.1)
        
        plt.show()
        plt.close()