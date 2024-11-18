from graph_library.Grafo import Grafo
from graph_library.Aresta import Aresta
from graph_library.Vertice import Vertice

if __name__ == "__main__":
    # Criando o grafo
    grafo = Grafo()

    # Adicionando vértices ao grafo
    grafo.addVertice("0", 3)
    grafo.addVertice("1", 1)
    grafo.addVertice("2", 2)
    grafo.addVertice("5", 3)
    grafo.addVertice("3", 3)
    grafo.addVertice("4", 3)
    grafo.addVertice("6", 3)
    grafo.addVertice("7", 3)

    # Criando arestas
    grafo.addAresta("0", "1", ponderacao=10, rotulacao="Aresta1", direcionada=True)
    grafo.addAresta("1", "2", ponderacao=5, rotulacao="Aresta2", direcionada=True)
    grafo.addAresta("2", "0", ponderacao=10, rotulacao="Aresta1", direcionada=True)
    grafo.addAresta("2", "3", ponderacao=5, rotulacao="Aresta2", direcionada=True)
    grafo.addAresta("3", "4", ponderacao=10, rotulacao="Aresta1", direcionada=True)
    grafo.addAresta("4", "7", ponderacao=5, rotulacao="Aresta2", direcionada=True)
    grafo.addAresta("4", "5", ponderacao=10, rotulacao="Aresta1", direcionada=True)
    grafo.addAresta("5", "6", ponderacao=5, rotulacao="Aresta2", direcionada=True)
    grafo.addAresta("6", "7", ponderacao=5, rotulacao="Aresta2", direcionada=True)
    grafo.addAresta("6", "4", ponderacao=5, rotulacao="Aresta2", direcionada=True)

    # Exibindo a lista de adjacência
    #grafo.busca_em_profundidade(grafo.getVertice('E'));
    print(grafo.kosaraju());
