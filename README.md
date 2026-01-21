Robô Navigator – Algoritmos de Busca em Grafos

Este projeto é uma aplicação web que simula a movimentação de um robô em um grid 10x10, utilizando diferentes algoritmos de busca em grafos para encontrar o melhor caminho entre um ponto inicial e um ponto objetivo.

A aplicação permite visualizar, de forma interativa, como cada algoritmo se comporta diante de obstáculos gerados dinamicamente, facilitando o entendimento e a comparação entre as estratégias de busca.

Algoritmos de Busca Implementados

O sistema oferece suporte aos seguintes algoritmos:

- Busca em Amplitude (BFS)
- Busca em Profundidade (DFS)
- Busca em Profundidade Limitada
- Aprofundamento Iterativo
- Busca Bidirecional
- Busca de Custo Uniforme
- Busca Gulosa (Greedy)
- A*
- AIA* (A* Iterativo)

> Os algoritmos Custo Uniforme, Greedy, A* e AIA* utilizam uma estrutura de busca otimizada compartilhada, com reaproveitamento de lógica para:
> - controle de nós visitados  
> - expansão de estados  
> - reconstrução do caminho final

> Cada algoritmo diferencia-se apenas pela função de custo/heurística, evitando duplicação de código e melhorando a organização do projeto.

Tecnologias Utilizadas

Backend
- Python
- Flask

Frontend
- HTML
- CSS
- JavaScript
