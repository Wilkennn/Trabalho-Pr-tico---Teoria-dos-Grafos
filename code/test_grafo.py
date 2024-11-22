from graph_library.Grafo import Grafo
from graph_library.Aresta import Aresta
from graph_library.Vertice import Vertice

if __name__ == "__main__":

    grafo = Grafo.importar_de_gexf('./files/input/grafo.gexf');

    grafo.adicionar_vertice("W", 1)

    grafo.exportar_para_gexf('./files/output/graph.gexf')

    # grafo.adicionar_vertice("B", 2)
    # grafo.adicionar_vertice("C", 3)
    # grafo.adicionar_vertice("D", 3)

    # grafo.adicionar_aresta("A", "B", ponderacao=10, rotulacao="Aresta1", direcionada=False)
    # grafo.adicionar_aresta("B", "C", ponderacao=5, rotulacao="Aresta2", direcionada=False)
    # grafo.adicionar_aresta("C", "D", ponderacao=10, rotulacao="Aresta1", direcionada=False)
    # grafo.adicionar_aresta("D", "A", ponderacao=5, rotulacao="Aresta2", direcionada=False)

    #grafo.exibir_lista_adjacencia()
    #grafo.exibir_matriz_adjacencia()
    #grafo.exibir_matriz_incidencia()
