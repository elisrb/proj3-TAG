Código desenvolvido para o projeto 3 da disciplina Teoria e Aplicação de Grafos, no semestre 2024.2 na Universidade de Brasília.

# Projeto 3

Por: Elis Rodrigues Borges - 231018875

Repositório do projeto no GitHub: https://github.com/elisrb/proj3-TAG

## Descrição

O objetivo deste projeto é implementar um algoritmo de coloração ótima de arestas no contexto do problema de double round-robin com 7 times e 14 rodadas. Ele foi desenvolvido em Python, e o código-fonte da solução está no arquivo ```proj3-TAG.py```.

## Dependências

Instale as bibliotecas **NetworkX** e **Matplotlib** usando o pip. Os seguintes comandos podem ser utilizados:

```pip install networkx```

```pip install matplotlib```

Tendo as dependências instaladas, o arquivo ```proj3-TAG.py``` poderá ser executado de forma a fornecer a solução do problema. O tempo para produzir e carregar a imagem do grafo pode deixar a execução do código um pouco lenta.

## Implementação

O projeto foi implementado utilizando coloração de vértices em um grafo que segue as seguintes regras:

- há um vértice *Ri* para cada rodada *i* de 1 a 14;
- cada cor corresponde a uma rodada, ou seja, cada vértice *Ri* terá uma cor distinta;
- há dois vértices *A, B* e *B, A* para cada par de times distintos *A* e *B*, representando os dois jogos que vão ocorrer entre *A* e *B* no torneio (com mandos opostos);
- há uma aresta entre dois vértices se eles não podem ter a mesma cor, isto é, se os jogos não podem ocorrer na mesma rodada (restrições de jogos e rodadas conforme foi especificado no roteiro, e restrições entre jogos que possuem os mesmos times, uma vez que um time só pode jogar uma vez por rodada)

A partir do grafo, foi implementado um algoritmo guloso de coloração de vértices para determinar quais jogos aconteceriam em cada rodada. Como a ordem dos vértices impacta no resultado, o algoritmo é executado quantas vezes for necessário, com uma ordem aleatória dos vértices do grafo, até encontrar uma coloração válida de acordo com as especificações do projeto (14 rodadas com 3 jogos cada).

Os resultados são exibidos na tela, sendo a primeira tela exibida a coloração inicial e, **ao fechar esta tela**, o restante do código é executado e é exibida a coloração final. Além disso, a lista de quais jogos pertencem a cada rodada é fornecida como output no terminal ao fim da execução do código.

## Referências

Slides de aula fornecidos pelo Prof. Díbio;

Lewis, R. & Thompson, J. On the Application of Graph Colouring Techniques in Round-Robin Sports Scheduling (2010).
