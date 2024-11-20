from graph_library.Grafo import Grafo
from graph_library.Aresta import Aresta
from graph_library.Vertice import Vertice

if __name__ == "__main__":
    # Criando o grafo
    grafo = Grafo()

    # Adicionando vértices ao grafo
    grafo.addVertice("A", 1)
    grafo.addVertice("B", 2)
    grafo.addVertice("C", 3)
    # grafo.addVertice("D", 3)
    # grafo.addVertice("E", 3)
    # grafo.addVertice("F", 3)
    # grafo.addVertice("G", 3)
    # grafo.addVertice("H", 3)

    # Criando arestas
<<<<<<< HEAD
    grafo.addAresta("A", "B", ponderacao=10, rotulacao="Aresta1", direcionada=False)
    grafo.addAresta("B", "C", ponderacao=5, rotulacao="Aresta2", direcionada=False)
    # grafo.addAresta("B", "D", ponderacao=10, rotulacao="Aresta1", direcionada=False)
    # grafo.addAresta("D", "E", ponderacao=5, rotulacao="Aresta2", direcionada=False)
    # grafo.addAresta("E", "F", ponderacao=10, rotulacao="Aresta1", direcionada=False)
    # grafo.addAresta("E", "F", ponderacao=5, rotulacao="Aresta2", direcionada=False)
    # grafo.addAresta("F", "G", ponderacao=10, rotulacao="Aresta1", direcionada=False)
    # grafo.addAresta("F", "H", ponderacao=5, rotulacao="Aresta2", direcionada=False)
    # grafo.addAresta("H", "G", ponderacao=5, rotulacao="Aresta2", direcionada=False)
    # grafo.addAresta("4", "6", ponderacao=5, rotulacao="Aresta2", direcionada=False)

    # Exibindo a lista de adjacência

    pontes = grafo.identificar_pontesTarjan()
    print(pontes)

    p2 = grafo.identificar_pontesNaive()
    print(f"Naive", p2)

    arti = grafo.identificar_articulacoes()
    print(arti)
=======
    # grafo.addAresta("1", "2", ponderacao=10, rotulacao="Aresta1", direcionada=True)
    # grafo.addAresta("2", "3", ponderacao=5, rotulacao="Aresta2", direcionada=True)
    # grafo.addAresta("3", "4", ponderacao=10, rotulacao="Aresta1", direcionada=True)
    # grafo.addAresta("2", "4", ponderacao=5, rotulacao="Aresta2", direcionada=True)
    # grafo.addAresta("2", "3", ponderacao=10, rotulacao="Aresta1", direcionada=True)
    # grafo.addAresta("3", "4", ponderacao=5, rotulacao="Aresta2", direcionada=True)
    # grafo.addAresta("6", "7", ponderacao=10, rotulacao="Aresta1", direcionada=True)
    # grafo.addAresta("3", "6", ponderacao=5, rotulacao="Aresta2", direcionada=True)
    # grafo.addAresta("1", "4", ponderacao=5, rotulacao="Aresta2", direcionada=True)
    # grafo.addAresta("4", "6", ponderacao=5, rotulacao="Aresta2", direcionada=True)

    # Exibindo a lista de adjacência

    # pontes = grafo.identificar_pontes()
    # print(pontes)

    # arti = grafo.identificar_articulacoes()
    # print(arti)
>>>>>>> 9f0da4596206206fe8cad41dc5a680dcc2638815
    # grafo.exibir_matriz_incidencia()
    # grafo.exibir_matriz_adjacencia()
    print(grafo.kosaraju())