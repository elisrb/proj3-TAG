"""
Universidade de Brasília
Departamento de Ciência da Computação

Projeto 3
Teoria e Aplicação de Grafos, Turma A, 2024/2
Prof. Díbio

Desenvolvido por: Elis Rodrigues Borges - 231018875
"""

import networkx as nx  # para representar o grafo
import matplotlib.pyplot as plt  # para visualizar o grafo
#from itertools import permutations # para mudar a ordem dos vértices
from random import shuffle # para mudar a ordem dos vértices

### CONSTRUÇÃO DO GRAFO ###

times = ["DFC", "TFC", "AFC", "LFC", "FFC", "OFC", "CFC"]
grafo = nx.Graph()

# para adicionar os vértices dos jogos:
for time1 in times:
    for time2 in times:
        if time1 != time2:
            # o formato do nome do vértice é "mandante, visitante"
            grafo.add_node(f"{time1}, {time2}")
            grafo.add_node(f"{time2}, {time1}")

# para adicionar as restrições de jogos:
for vertice1 in list(grafo.nodes()):

    # separa os nomes dos times que vão jogar
    mandante1, visitante1 = vertice1.split(", ")

    # verifica todos os vértices do grafo
    for vertice2 in list(grafo.nodes()):

        # não considera para análise o próprio vértice 1
        if vertice1 != vertice2:

            # adiciona uma aresta entre jogos com times em comum
            # (já que o mesmo time não pode jogar duas vezes em um mesmo turno)
            if mandante1 in vertice2 or visitante1 in vertice2:
                grafo.add_edge(vertice1, vertice2)
                print(f"{vertice1} não pode com {vertice2}")

            else:
                # separa os nomes dos times que vão jogar
                mandante2, visitante2 = vertice2.split(", ")

                # TFC mandante não com OFC mandante:
                if mandante1 == "TFC" and mandante2 == "OFC":
                    grafo.add_edge(vertice1, vertice2)
                    print(f"{vertice1} não pode com {vertice2}")

                # AFC mandante não com FFC mandante:
                elif mandante1 == "AFC" and mandante2 == "FFC":
                    grafo.add_edge(vertice1, vertice2)
                    print(f"{vertice1} não pode com {vertice2}")

# para adicionar os vértices das rodadas:
for i in range(1, 15):
    grafo.add_node(f"R{i}")
    
# para adicionar uma aresta entre cada par de rodadas:
# (pois cada rodada é uma coloração)
for i in range(2, 15):
    for j in range(1, i):
            grafo.add_edge(f"R{j}", f"R{i}")

# para adicionar as restrições de rodadas:
grafo.add_edge("R1", "DFC, CFC")
grafo.add_edge("R1", "CFC, DFC")
grafo.add_edge("R14", "DFC, CFC")
grafo.add_edge("R14", "CFC, DFC")
grafo.add_edge("R7", "LFC, FFC")
grafo.add_edge("R7", "FFC, LFC")
grafo.add_edge("R13", "LFC, FFC")
grafo.add_edge("R13", "FFC, LFC")
grafo.add_edge("R10", "OFC, LFC")
grafo.add_edge("R10", "LFC, OFC")
grafo.add_edge("R11", "OFC, LFC")
grafo.add_edge("R11", "LFC, OFC")
grafo.add_edge("R12", "AFC, FFC")
grafo.add_edge("R12", "FFC, AFC")
grafo.add_edge("R13", "AFC, FFC")
grafo.add_edge("R13", "FFC, AFC")
grafo.add_edge("R2", "TFC, CFC")
grafo.add_edge("R2", "CFC, TFC")
grafo.add_edge("R3", "TFC, CFC")
grafo.add_edge("R3", "CFC, TFC")

### COLORAÇÃO ###

# para atribuir cores para cada rodada:
grafo.nodes["R1"]["color"] = "blue"
grafo.nodes["R2"]["color"] = "green"
grafo.nodes["R3"]["color"] = "red"
grafo.nodes["R4"]["color"] = "cyan"
grafo.nodes["R5"]["color"] = "magenta"
grafo.nodes["R6"]["color"] = "yellow"
grafo.nodes["R7"]["color"] = "tomato"
grafo.nodes["R8"]["color"] = "limegreen"
grafo.nodes["R9"]["color"] = "dodgerblue"
grafo.nodes["R10"]["color"] = "gold"
grafo.nodes["R11"]["color"] = "brown"
grafo.nodes["R12"]["color"] = "pink"
grafo.nodes["R13"]["color"] = "gray"
grafo.nodes["R14"]["color"] = "olive"
for vertice in grafo.nodes():
    if "color" not in grafo.nodes[vertice]:
        grafo.nodes[vertice]["color"] = "white"

# para visualizar o grafo inicial:
node_color = [grafo.nodes[node]["color"] for node in grafo.nodes()]
pos = nx.spring_layout(grafo, k=0.3, iterations=50)
nx.draw(grafo, pos, with_labels=True, node_size=1000, node_color=node_color, font_size=10, edge_color="gray", width=0.5)
plt.title("Coloração Inicial", fontsize = 16, color="black", loc="center")
plt.show()

# dicionário no formato {rodada-1 : cor da rodada}
rodadas_cores = {
    0 : "blue",
    1 : "green",
    2 : "red",
    3 : "cyan",
    4 : "magenta",
    5 : "yellow",
    6 : "tomato",
    7 : "limegreen",
    8 : "dodgerblue",
    9 : "gold",
    10 : "brown",
    11 : "pink",
    12 : "gray",
    13 : "olive"
}

# dicionário no formato {cor da rodada : rodada-1}
cores_rodadas = {
    'blue': 0,
    'green': 1,
    'red': 2,
    'cyan': 3,
    'magenta': 4,
    'yellow': 5,
    'tomato': 6,
    'limegreen': 7,
    'dodgerblue': 8,
    'gold': 9,
    'brown': 10,
    'pink': 11,
    'gray': 12,
    'olive': 13
}

# para fazer a coloração dos demais vértices:

# gerar todas as permutações da ordem dos vértices
#todas_permutacoes = list(permutations(list(grafo.nodes())))
max_vertices_coloridos = 0
vertices = list(grafo.nodes()).copy()

# percorrer as permutações
#for permutacao in todas_permutacoes:
while max_vertices_coloridos < 42:
    # para reatribuir as cores iniciais para cada rodada:
    for vertice in grafo.nodes():
        grafo.nodes[vertice]["color"] = "white"
    grafo.nodes["R1"]["color"] = "blue"
    grafo.nodes["R2"]["color"] = "green"
    grafo.nodes["R3"]["color"] = "red"
    grafo.nodes["R4"]["color"] = "cyan"
    grafo.nodes["R5"]["color"] = "magenta"
    grafo.nodes["R6"]["color"] = "yellow"
    grafo.nodes["R7"]["color"] = "tomato"
    grafo.nodes["R8"]["color"] = "limegreen"
    grafo.nodes["R9"]["color"] = "dodgerblue"
    grafo.nodes["R10"]["color"] = "gold"
    grafo.nodes["R11"]["color"] = "brown"
    grafo.nodes["R12"]["color"] = "pink"
    grafo.nodes["R13"]["color"] = "gray"
    grafo.nodes["R14"]["color"] = "olive"
    
    # dicionário no formato {rodada-1 : número de jogos na rodada}
    rodadas_jogos = {
        0: [],
        1: [],
        2: [],
        3: [],
        4: [],
        5: [],
        6: [],
        7: [],
        8: [],
        9: [],
        10: [],
        11: [],
        12: [],
        13: []
    }

    total = 0  # total de vértices coloridos

    # passa por todos os vértices...
    for vertice in vertices:
        if grafo.nodes[vertice]["color"] == "white":
        # ... mas analisa só os vértices dos jogos (vértices que ainda não têm cor atribuída)
            
            # lê as cores dos vizinhos que possuem cor
            rodadas_vizinhos = {cores_rodadas[grafo.nodes[vizinho]["color"]] for vizinho in grafo.neighbors(vertice) if grafo.nodes[vizinho]["color"] != "white"}

            # encontra a menor rodada disponível
            rodada = 0
            while rodada in rodadas_vizinhos:
                print(f"{vertice} não pode na rodada {rodada+1}")
                rodada += 1

            if(rodada<14):
                # atribui a cor da mesma rodada ao vértice
                grafo.nodes[vertice]["color"] = rodadas_cores[rodada]
                
                # incrementa a contagem de jogos por rodada
                rodadas_jogos[rodada].append(vertice)
                total+=1
                print(f"adicionou {vertice} na rodada {rodada+1}, total de jogos já alocados: {total}")
            else:
                break  # se não foi possível uma coloração com 14 cores, interrompe o processo

    max_vertices_coloridos = max(max_vertices_coloridos, total)
    shuffle(vertices)

print("Lista no formato {rodada: jogos da rodada}")
for i in range(1, 15):
    print(f"R{i}:", rodadas_jogos[i-1])

# para visualizar o grafo final:
node_color = [grafo.nodes[node]["color"] for node in grafo.nodes()]
pos = nx.spring_layout(grafo, k=0.3, iterations=50)
nx.draw(grafo, pos, with_labels=True, node_size=1000, node_color=node_color, font_size=10, edge_color="gray", width=0.5)
plt.title("Coloração Final", fontsize = 16, color="black", loc="center")
plt.show()