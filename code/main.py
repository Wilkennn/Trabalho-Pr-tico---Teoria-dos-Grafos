from biblioteca_grafos import GrafoMatrizAdjacencia, GrafoMatrizIncidencia, GrafoListaAdjacencia

def main():
    num_vertices = int(input("Informe o número de vértices do grafo: "))

    print("\n=== Grafo com Matriz de Adjacência ===")
    grafo_adj = GrafoMatrizAdjacencia(num_vertices)
    grafo_adj.adicionar_aresta(0, 1, 5)
    grafo_adj.mostrar()
    print(f"Adjacência entre 0 e 1: {grafo_adj.checar_adjacencia(0, 1)}")

    print("\n=== Grafo com Matriz de Incidência ===")
    grafo_inc = GrafoMatrizIncidencia(num_vertices)
    grafo_inc.adicionar_aresta(0, 1, 5)
    grafo_inc.mostrar()
    print(f"Adjacência entre 0 e 1: {grafo_inc.checar_adjacencia(0, 1)}")

    print("\n=== Grafo com Lista de Adjacência ===")
    grafo_lista = GrafoListaAdjacencia(num_vertices)
    grafo_lista.adicionar_aresta(0, 1, 5)
    grafo_lista.mostrar()
    print(f"Adjacência entre 0 e 1: {grafo_lista.checar_adjacencia(0, 1)}")

if __name__ == "__main__":
    main()
