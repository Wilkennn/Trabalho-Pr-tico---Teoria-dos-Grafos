from graph_library.Grafo import Grafo
from graph_library.Aresta import Aresta
from graph_library.Vertice import Vertice

if __name__ == "__main__":

    
    grafo = Grafo()

    grafo.adicionar_vertice("1", 2)
    grafo.adicionar_vertice("2", 2)
    grafo.adicionar_vertice("3", 3)
    grafo.adicionar_vertice("4", 3)
    grafo.adicionar_vertice("5", 3)
    grafo.adicionar_vertice("6", 3)
    grafo.adicionar_vertice("7", 3)
   
    grafo.adicionar_aresta("1", "2", ponderacao=10, rotulacao="Aresta1", direcionada=False)
    grafo.adicionar_aresta("2", "3", ponderacao=10, rotulacao="Aresta1", direcionada=False)
    grafo.adicionar_aresta("1", "3", ponderacao=10, rotulacao="Aresta1", direcionada=False)
    grafo.adicionar_aresta("2", "5", ponderacao=10, rotulacao="Aresta1", direcionada=False)
    grafo.adicionar_aresta("3", "6", ponderacao=10, rotulacao="Aresta1", direcionada=False)
    grafo.adicionar_aresta("2", "4", ponderacao=10, rotulacao="Aresta1", direcionada=False)
    grafo.adicionar_aresta("3", "4", ponderacao=10, rotulacao="Aresta1", direcionada=False)
    grafo.adicionar_aresta("5", "4", ponderacao=10, rotulacao="Aresta1", direcionada=False)
    grafo.adicionar_aresta("6", "4", ponderacao=10, rotulacao="Aresta1", direcionada=False)
    grafo.adicionar_aresta("5", "6", ponderacao=10, rotulacao="Aresta1", direcionada=False)
    grafo.adicionar_aresta("5", "7", ponderacao=10, rotulacao="Aresta1", direcionada=False)
    grafo.adicionar_aresta("6", "7", ponderacao=10, rotulacao="Aresta1", direcionada=False)

    print(grafo.algoritmo_de_fleury())