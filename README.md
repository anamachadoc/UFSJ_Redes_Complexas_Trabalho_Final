<h1 align="center"> Similaridade entre Artistas </h1>

### 💻 _Descrição do Projeto_

Este trabalho investiga a similaridade entre artistas no Spotify utilizando dados da sua API. A premissa é que artistas do mesmo gênero musical são considerados semelhantes e que a preferência dos usuários está mais relacionada ao gênero do que aos artistas individuais. Redes complexas foram construídas conectando artistas por gêneros, com o objetivo de aplicar essas estruturas em duas estratégias de recomendação: uma baseada em popularidade e outra em proximidade (K-Vizinhos Mais Próximos). A análise mostrou que, embora as duas estratégias tenham alta interseção entre si, apresentam baixa interseção com a similaridade proposta pelo Spotify. Além disso, uma pesquisa com 24 participantes revelou que as relações entre artistas no Spotify não são tão adequadas.

### 📁 _Como executar_

A versão utilizada do python foi 3.10.12

Todas as dependências necessárias estão no arquivo [requirements.txt](./requirements.txt). Instale-o com:
```
pip install -r requirements.txt
```
As análises estão em [code](./code).

###  📄 _Dados_

A organização dos dados gerados e utilizados dá-se da seguinte forma:
1. [data](./data): dados obtidos a partir da API
2. [graphics](./graphics): gráficos gerados a partir das análises das redes criadas
3. [google_forms](./google_forms): análises das respostas da [pesquisa online](https://forms.gle/B5ntdwDJ2xwzQFpR9) realizada
4. [credentials](./credentials): **onde devem ser inseridas as credenciais fornecidas pela [API](https://developer.spotify.com/documentation/web-api)**

### 💭 _Autores_

| [<img src="https://avatars.githubusercontent.com/u/108549971?v=4" width=100 > <br>Ana Cláudia Machado</sub>](https://github.com/anamachadoc) |  [<img src="https://avatars.githubusercontent.com/u/108549890?v=4" width=100 > <br> Gabriel Silva Prenassi </sub>](https://github.com/gabrielprenassi)|
| :---: | :---: |