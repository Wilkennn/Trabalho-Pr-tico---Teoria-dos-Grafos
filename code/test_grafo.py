from graph_library.Grafo import Grafo
from graph_library.Aresta import Aresta
from graph_library.Vertice import Vertice

if __name__ == "__main__":
    # Criando o grafo
    grafo = Grafo()

    # # Criando arestas
    # Adicionando vértices ao grafo
    grafo.addVertice("A", 1)
    grafo.addVertice("B", 2)
    grafo.addVertice("C", 3)
    grafo.addVertice("D", 3)
    # grafo.addVertice("E", 3)
    # grafo.addVertice("F", 3)
    # grafo.addVertice("G", 3)
    # grafo.addVertice("H", 3)

    # Criando arestas
    grafo.addAresta("A", "B", ponderacao=10, rotulacao="Aresta1", direcionada=False)
    grafo.addAresta("B", "C", ponderacao=5, rotulacao="Aresta2", direcionada=False)
    grafo.addAresta("C", "D", ponderacao=10, rotulacao="Aresta1", direcionada=False)
    grafo.addAresta("D", "A", ponderacao=5, rotulacao="Aresta2", direcionada=False)
    # grafo.addAresta("E", "F", ponderacao=10, rotulacao="Aresta1", direcionada=False)
    # grafo.addAresta("E", "F", ponderacao=5, rotulacao="Aresta2", direcionada=False)
    # grafo.addAresta("F", "G", ponderacao=10, rotulacao="Aresta1", direcionada=False)
    # grafo.addAresta("F", "H", ponderacao=5, rotulacao="Aresta2", direcionada=False)
    # grafo.addAresta("H", "G", ponderacao=5, rotulacao="Aresta2", direcionada=False)
    # grafo.addAresta("4", "6", ponderacao=5, rotulacao="Aresta2", direcionada=False)

    # cone = grafo.identificar_conectividade()
    pontes = grafo.identificar_pontesTarjan()
    # arti = grafo.identificar_articulacoes()
    # p2 = grafo.identificar_pontesNaive()
    # grafo.isEuleriano()

    print("Pontes: ", pontes)
    # print("Pontes Naive : ", p2)
    # print("Articulações: ", arti)
    # print("Cone", cone)  
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

    # # Exibindo a lista de adjacência

    kosaraju = grafo.kosaraju()
    print(kosaraju)
    pontes = grafo.identificar_conectividade()
    grafo.algoritmo_de_fleury()
    # # print(pontes)

    # # arti = grafo.identificar_articulacoes()
    # # print(arti)
    # grafo.exibir_matriz_incidencia()
    # grafo.exibir_matriz_adjacencia()
    # # #print(grafo.kosaraju())
    # grafo.exportar_para_gexf("grafo2.gexf");

