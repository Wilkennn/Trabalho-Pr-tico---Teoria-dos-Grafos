from graph_library.Grafo import Grafo
from graph_library.Aresta import Aresta
from graph_library.Vertice import Vertice

if __name__ == "__main__":
    # Criando o grafo
    grafo = Grafo()

    # Adicionando vértices ao grafo
    grafo.addVertice("1", 1)
    grafo.addVertice("2", 2)
    grafo.addVertice("3", 3)
    grafo.addVertice("4", 3)
    # grafo.addVertice("4", 3)
    # grafo.addVertice("6", 3)
    # grafo.addVertice("7", 3)

    # Criando arestas
    grafo.addAresta("1", "2", ponderacao=10, rotulacao="Aresta1", direcionada=True)
    grafo.addAresta("2", "3", ponderacao=5, rotulacao="Aresta2", direcionada=True)
    grafo.addAresta("3", "4", ponderacao=10, rotulacao="Aresta1", direcionada=True)
    # grafo.addAresta("2", "4", ponderacao=5, rotulacao="Aresta2", direcionada=True)
    # grafo.addAresta("2", "3", ponderacao=10, rotulacao="Aresta1", direcionada=True)
    # grafo.addAresta("3", "4", ponderacao=5, rotulacao="Aresta2", direcionada=True)
    # grafo.addAresta("6", "7", ponderacao=10, rotulacao="Aresta1", direcionada=True)
    # grafo.addAresta("3", "6", ponderacao=5, rotulacao="Aresta2", direcionada=True)
    # grafo.addAresta("1", "4", ponderacao=5, rotulacao="Aresta2", direcionada=True)
    # grafo.addAresta("4", "6", ponderacao=5, rotulacao="Aresta2", direcionada=True)

    # Exibindo a lista de adjacência

    pontes = grafo.identificar_pontes()
    print(pontes)

    arti = grafo.identificar_articulacoes()
    print(arti)
    # grafo.exibir_matriz_incidencia()
    # grafo.exibir_matriz_adjacencia()
    # grafo.exibir_lista_adjacencia()