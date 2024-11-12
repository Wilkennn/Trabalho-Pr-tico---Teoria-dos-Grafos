from typing import List, Dict, Tuple

class Grafo:

    def __init__(self, isDirecionado=False):
        self.__lista_de_vertices: List[str] = []  # Lista de vértices
        self.__lista_de_arestas: List[Tuple[str, str]] = []  # Lista de arestas
        self.__lista_de_adjacentes: Dict[str, List[str]] = {}  # Dicionário de adjacências
        self.__direcionado: bool = isDirecionado  # Tipo de grafo (direcionado ou não)

    def getVertices(self) -> List[str]:
        return [vertice for vertice in self.__lista_de_vertices]
    
    def getNumVertices(self) -> int:
        return len(self.__lista_de_vertices)

    def getArestas(self) -> List[str]:
        return [f"{aresta[0]} - {aresta[1]}" for aresta in self.__lista_de_arestas]
    
    def getNumArestas(self) -> int:
        return len(self.__lista_de_arestas)
    
    def searchAresta(self, verticeA: str, verticeB: str) -> Tuple[str, str] or None:
        for aresta in self.__lista_de_arestas:
            if self.__direcionado:
                if aresta[0] == verticeA and aresta[1] == verticeB:
                    return aresta
            else:
                if (aresta[0] == verticeA and aresta[1] == verticeB) or \
                   (aresta[0] == verticeB and aresta[1] == verticeA):
                    return aresta
        return None

    def addVertice(self, vertice: str) -> bool:
        if vertice in self.__lista_de_vertices:
            print("Vértice já existe no grafo.")
            return False
        
        self.__lista_de_vertices.append(vertice)
        self.__lista_de_adjacentes[vertice] = []
        print(f"Vértice {vertice} adicionado com sucesso.")
        return True
    
    def removeVertice(self, vertice: str) -> bool:
        if vertice not in self.__lista_de_vertices:
            print("Vértice não existe no grafo.")
            return False
        else:
            # Remove todas as arestas que envolvem o vértice
            self.__lista_de_arestas = [aresta for aresta in self.__lista_de_arestas if aresta[0] != vertice and aresta[1] != vertice]
            self.__lista_de_vertices.remove(vertice)
            del self.__lista_de_adjacentes[vertice]  # Remove o vértice também do dicionário de adjacência
            print(f"Vértice {vertice} removido com sucesso.")
            return True
    
    def addAresta(self, verticeA: str, verticeB: str) -> bool:
        if verticeA in self.__lista_de_vertices and verticeB in self.__lista_de_vertices:
            if self.__direcionado:
                self.__lista_de_arestas.append((verticeA, verticeB))
                self.__lista_de_adjacentes[verticeA].append(verticeB)
            else:
                self.__lista_de_arestas.append((verticeA, verticeB))
                self.__lista_de_arestas.append((verticeB, verticeA))
                self.__lista_de_adjacentes[verticeA].append(verticeB)
                self.__lista_de_adjacentes[verticeB].append(verticeA)
            print(f"Aresta entre {verticeA} e {verticeB} adicionada com sucesso.")
            return True
        else:
            print("Erro: Um ou ambos os vértices não existem no grafo.")
            return False
        
    def removeAresta(self, aresta: Tuple[str, str]) -> bool:
        if aresta not in self.__lista_de_arestas:
            print("Erro: Aresta não existe no grafo.")
            return False
        else:
            self.__lista_de_arestas.remove(aresta)
            if not self.__direcionado:
                # Remove a aresta reversa se o grafo não for direcionado
                verticeA, verticeB = aresta
                self.__lista_de_arestas.remove((verticeB, verticeA))
            print(f"Aresta {aresta} removida com sucesso.")
            return True
                       
    def isEmpty(self) -> bool:
        return len(self.__lista_de_vertices) == 0
    
    def isCompleto(self) -> bool:
        numVertices = len(self.__lista_de_vertices)
        if self.__direcionado:
            numMinArestas = numVertices * (numVertices - 1)
        else:
            numMinArestas = (numVertices * (numVertices - 1)) // 2
        
        return len(self.__lista_de_arestas) == numMinArestas
    
    def isAdjacentes(self, verticeA: str, verticeB: str) -> bool:
        if self.__direcionado:
            return verticeB in self.__lista_de_adjacentes[verticeA]
        else:
            return verticeB in self.__lista_de_adjacentes[verticeA] and verticeA in self.__lista_de_adjacentes[verticeB]
    
    def areArestasAdjacentes(self, arestaA: Tuple[str, str], arestaB: Tuple[str, str]) -> bool:

        verticeA1, verticeB1 = arestaA
        verticeA2, verticeB2 = arestaB

        if self.__direcionado:
            return verticeB1 == verticeA2 or verticeA1 == verticeB2
        else:
            return verticeA1 == verticeA2 or verticeA1 == verticeB2 or verticeB1 == verticeA2 or verticeB1 == verticeB2