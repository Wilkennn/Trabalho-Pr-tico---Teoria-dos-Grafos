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
    # grafo.exibir_matriz_incidencia()
    # grafo.exibir_matriz_adjacencia()
    # grafo.exibir_lista_adjacencia()