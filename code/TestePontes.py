import time
from graph_library.Grafo import Grafo

def teste_grafos():
    tamanhos = [100, 1000, 10000, 100000]
    
    for tamanho in tamanhos:
        grafo = Grafo()
        for i in range(tamanho):
            grafo.addVertice(f"v{i}")
        
        for i in range(tamanho - 1):
            grafo.addAresta(f"v{i}", f"v{i+1}")
        
        start_time = time.time()
        pontes_naive = grafo.identificar_pontesNaive()
        print(f"Pontes (Método Naive) para grafo de {tamanho} vértices: {time.time() - start_time} segundos")
        
        start_time = time.time()
        pontes_tarjan = grafo.identificar_pontesTarjan()
        print(f"Pontes (Método Tarjan) para grafo de {tamanho} vértices: {time.time() - start_time} segundos")
        
        if grafo.grafo_conexo() and grafo.isEuleriano():
            start_time = time.time()
            caminho_euleriano = grafo.algoritmo_de_fleury()
            print(f"Caminho Euleriano para grafo de {tamanho} vértices: {time.time() - start_time} segundos")
        else:
            print(f"O grafo de {tamanho} vértices não é euleriano.")

teste_grafos()
