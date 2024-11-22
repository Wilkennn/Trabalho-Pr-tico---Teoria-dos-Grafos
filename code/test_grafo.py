from graph_library.Grafo import Grafo
from graph_library.Aresta import Aresta
from graph_library.Vertice import Vertice

if __name__ == "__main__":

    grafo = Grafo()

    grafo.addVertice("A", 1)
    grafo.addVertice("B", 2)
    grafo.addVertice("C", 3)
    grafo.addVertice("D", 3)

    grafo.addAresta("A", "B", ponderacao=10, rotulacao="Aresta1", direcionada=False)
    grafo.addAresta("B", "C", ponderacao=5, rotulacao="Aresta2", direcionada=False)
    grafo.addAresta("C", "D", ponderacao=10, rotulacao="Aresta1", direcionada=False)
    grafo.addAresta("D", "A", ponderacao=5, rotulacao="Aresta2", direcionada=False)

    grafoCopy = grafo.copy();

    print(grafo.getVertices())
    print(grafoCopy.getVertices())
    grafo.identificar_conectividade()