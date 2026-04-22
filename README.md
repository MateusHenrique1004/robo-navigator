# 🤖 Robô Navigator – Algoritmos de Busca em Grafos

Este projeto é uma aplicação web interativa que simula a navegação de um robô em um grid 10x10, utilizando diferentes algoritmos de busca para encontrar o melhor caminho entre um ponto inicial e um objetivo.

A proposta é permitir a visualização prática e comparativa dos algoritmos, demonstrando como cada estratégia se comporta diante de obstáculos gerados dinamicamente.

---

## 🚀 Funcionalidades

- Simulação de movimentação de um robô em ambiente controlado  
- Geração dinâmica de obstáculos  
- Visualização passo a passo dos algoritmos  
- Comparação entre diferentes estratégias de busca  
- Reconstrução do caminho encontrado  

---

## 🧠 Algoritmos Implementados

- Busca em Amplitude (BFS)  
- Busca em Profundidade (DFS)  
- Busca em Profundidade Limitada  
- Aprofundamento Iterativo  
- Busca Bidirecional  
- Busca de Custo Uniforme  
- Busca Gulosa (Greedy)  
- A*  
- AIA* (A* Iterativo)  

---

## ⚙️ Estrutura e Arquitetura

Os algoritmos de busca informada (Custo Uniforme, Greedy, A* e AIA*) compartilham uma base otimizada, permitindo reutilização de código e melhor organização do projeto.

Essa estrutura inclui:

- Controle de nós visitados  
- Expansão de estados  
- Reconstrução do caminho final  

Cada algoritmo se diferencia apenas pela função de custo ou heurística, evitando duplicação e facilitando manutenção e escalabilidade.

---

## 🛠️ Tecnologias Utilizadas

### Backend
- Python  
- Flask  

### Frontend
- HTML  
- CSS  
- JavaScript  

---

## 🎯 Objetivo do Projeto

Este projeto foi desenvolvido com foco educacional, visando facilitar o entendimento de algoritmos de busca por meio de visualização prática e interativa, além de demonstrar boas práticas de organização e reutilização de código.
