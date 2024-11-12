class GrafoMatrizAdjacencia:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.matriz = [[0] * num_vertices for _ in range(num_vertices)]
        self.vertices_rotulos = {}
        self.arestas_peso = {}

    def adicionar_aresta(self, u, v, peso=1):
        self.matriz[u][v] = peso
        self.arestas_peso[(u, v)] = peso

    def remover_aresta(self, u, v):
        self.matriz[u][v] = 0
        self.arestas_peso.pop((u, v), None)

    def mostrar(self):
        for linha in self.matriz:
            print(linha)

    def checar_adjacencia(self, u, v):
        return self.matriz[u][v] != 0

    def num_arestas(self):
        return sum(self.matriz[u][v] != 0 for u in range(self.num_vertices) for v in range(self.num_vertices))

    def num_vertices(self):
        return self.num_vertices


class GrafoMatrizIncidencia:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.matriz = []
        self.arestas = []
        self.vertices_rotulos = {}

    def adicionar_aresta(self, u, v, peso=1):
        aresta = [0] * self.num_vertices
        aresta[u] = peso
        aresta[v] = -peso
        self.matriz.append(aresta)
        self.arestas.append((u, v))

    def remover_aresta(self, u, v):
        for i, (a, b) in enumerate(self.arestas):
            if a == u and b == v:
                self.matriz.pop(i)
                self.arestas.pop(i)
                break

    def mostrar(self):
        for linha in self.matriz:
            print(linha)

    def checar_adjacencia(self, u, v):
        for aresta in self.arestas:
            if aresta == (u, v):
                return True
        return False

    def num_arestas(self):
        return len(self.arestas)

    def num_vertices(self):
        return self.num_vertices


class GrafoListaAdjacencia:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.lista = {i: [] for i in range(num_vertices)}
        self.arestas_peso = {}

    def adicionar_aresta(self, u, v, peso=1):
        self.lista[u].append((v, peso))
        self.arestas_peso[(u, v)] = peso

    def remover_aresta(self, u, v):
        self.lista[u] = [(vertice, p) for vertice, p in self.lista[u] if vertice != v]
        self.arestas_peso.pop((u, v), None)

    def mostrar(self):
        for vertice, adjacentes in self.lista.items():
            print(f"{vertice}: {adjacentes}")

    def checar_adjacencia(self, u, v):
        return any(vertice == v for vertice, _ in self.lista[u])

    def num_arestas(self):
        return sum(len(adjacentes) for adjacentes in self.lista.values())

    def num_vertices(self):
        return self.num_vertices
