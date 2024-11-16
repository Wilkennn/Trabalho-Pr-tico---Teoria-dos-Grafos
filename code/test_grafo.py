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
    grafo.addVertice("D", 3)
    grafo.addVertice("E", 3)
    grafo.addVertice("F", 3)


    # Criando arestas
    grafo.addAresta("C", "A", ponderacao=10, rotulacao="Aresta1", direcionada=True)
    grafo.addAresta("C", "E", ponderacao=5, rotulacao="Aresta2", direcionada=True)
    grafo.addAresta("A", "B", ponderacao=10, rotulacao="Aresta1", direcionada=True)
    grafo.addAresta("A", "F", ponderacao=5, rotulacao="Aresta2", direcionada=True)
    grafo.addAresta("E", "B", ponderacao=10, rotulacao="Aresta1", direcionada=True)
    grafo.addAresta("E", "F", ponderacao=5, rotulacao="Aresta2", direcionada=True)
    grafo.addAresta("F", "B", ponderacao=10, rotulacao="Aresta1", direcionada=True)
    grafo.addAresta("B", "D", ponderacao=5, rotulacao="Aresta2", direcionada=True)
    grafo.addAresta("D", "F", ponderacao=5, rotulacao="Aresta2", direcionada=True)

    # Exibindo a lista de adjacência
    grafo.busca_em_profundidade(grafo.getVertice('E'));
    grafo.exibir_resultado_busca();
