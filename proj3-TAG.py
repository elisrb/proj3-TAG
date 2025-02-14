"""
Universidade de Brasília
Departamento de Ciência da Computação

Projeto 3
Teoria e Aplicação de Grafos, Turma A, 2024/2
Prof. Díbio

Desenvolvido por: Elis Rodrigues Borges - 231018875
"""

import networkx as nx
import matplotlib.pyplot as plt

times = ["DFC", "TFC", "AFC", "LFC", "FFC", "OFC", "CFC"]
grafo = nx.Graph()

# para adicionar os vértices dos jogos:
for time1 in times:
    for time2 in times:
        if time1 != time2:
            grafo.add_node(f"{time1}, {time2}")
            grafo.add_node(f"{time2}, {time1}")
            # o primeiro time é o mandante

# para adicionar as restrições de jogos:
for vertice1 in list(grafo.nodes()):
    # separa os nomes dos times que vão jogar
    mandante1, visitante1 = vertice1.split(", ")

    # verifica todos os vértices do grafo
    for vertice2 in list(grafo.nodes()):
        # não considera para análise o vértice igual ao vértice 1
        # nem o vértice (visitante, mandante)
        if mandante1 not in vertice2 or visitante1 not in vertice2:

            # adiciona uma aresta entre jogos com times em comum
            # (já que o mesmo time não pode jogar duas vezes em um mesmo turno)
            if mandante1 in vertice2 or visitante1 in vertice2:
                grafo.add_edge(vertice1, vertice2)

            else:
                # separa os nomes dos times que vão jogar
                mandante2, visitante2 = vertice2.split(", ")

                # TFC mandante não com OFC mandante:
                if mandante1 == "TFC" and mandante2 == "OFC":
                    grafo.add_edge(vertice1, vertice2)

                # AFC mandante não com FFC mandante:
                elif mandante1 == "AFC" and mandante2 == "FFC":
                    grafo.add_edge(vertice1, vertice2)

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

# para visualizar o grafo:
"""
"""
pos = nx.spring_layout(grafo, k=0.3, iterations=50)  # k = distância entre nós, iterations = número de iterações

nx.draw(grafo, pos, with_labels=True, node_size=1000, node_color="lightblue", font_size=10, edge_color="gray", width=0.5)
#nx.draw(grafo, pos, with_labels=True, node_size=100, node_color="lightblue", edge_color="gray", width=0.5)

plt.show()