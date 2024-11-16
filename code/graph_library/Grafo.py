from typing import List, Dict
from graph_library.Aresta import Aresta
from graph_library.Vertice import Vertice

class Grafo:

    def __init__(self, isDirecionado=False):
        self.__lista_de_vertices = []  # Lista de vértices
        self.__lista_de_arestas = []  # Lista de arestas
        self.__lista_de_adjacentes: Dict[str, List[str]] = {}  # Dicionário de adjacências
        self.__predecessores: Dict[str, List[str]] = {}  # Dicionário de predecessores
        self.__sucessores: Dict[str, List[str]] = {}  # Dicionário de sucessores
        self.__direcionado: bool = isDirecionado  # Tipo de grafo (direcionado ou não)

    def getVertices(self) -> List[str]:
        return self.__lista_de_vertices
    
    def getAdj(self) -> Dict[str, List[str]]:
        return self.__lista_de_adjacentes
    
    def getPredecessores(self) -> Dict[str, List[str]]:
        return self.__predecessores
    
    def getSucessores(self) -> Dict[str, List[str]]:
        return self.__sucessores

    def getNumVertices(self) -> int:
        return len(self.__lista_de_vertices)

    def getAllArestas(self) -> List['Aresta']:
        return self.__lista_de_arestas
    
    def getNumArestas(self) -> int:
        return len(self.__lista_de_arestas)
    
    def areAdjV(self, verticeA: str, verticeB: str) -> bool:
        for aresta in self.__lista_de_arestas:
            direcionada = aresta.isDirecionada()

            # Verifica se a aresta é direcionada
            if direcionada:
                if aresta.getVerticeA().getNome() == verticeA and aresta.getVerticeB().getNome() == verticeB:
                    print(f"Os vértices '{verticeA}' e '{verticeB}' são adjacentes.")
                    print(f"{direcionada}")
                    return True
            else:
                # Verifica a adjacência em ambas as direções para arestas não direcionadas
                if (
                    (aresta.getVerticeA().getNome() == verticeA and aresta.getVerticeB().getNome() == verticeB) or
                    (aresta.getVerticeA().getNome() == verticeB and aresta.getVerticeB().getNome() == verticeA)
                ):
                    print(f"Os vértices '{verticeA}' e '{verticeB}' são adjacentes.")
                    return True
    
        # Se não encontrou arestas conectando os vértices
        print(f"'{verticeA}' e '{verticeB}' NÃO são adjacentes.")
        return False

    def areAdjA(self, aresta1: Aresta, aresta2: Aresta) -> bool:
        # Obtendo os vértices das arestas
        verticeA1 = aresta1.getVerticeA().getNome()
        verticeB1 = aresta1.getVerticeB().getNome()
        verticeA2 = aresta2.getVerticeA().getNome()
        verticeB2 = aresta2.getVerticeB().getNome()
    
        # Verificando se as arestas são adjacentes
        if verticeA1 == verticeA2 or verticeA1 == verticeB2 or verticeB1 == verticeA2 or verticeB1 == verticeB2:
            print(f"As arestas com vértices ('{verticeA1}', '{verticeB1}') e ('{verticeA2}', '{verticeB2}') são adjacentes.")
            return True
        else:
            print(f"As arestas com vértices ('{verticeA1}', '{verticeB1}') e ('{verticeA2}', '{verticeB2}') NÃO são adjacentes.")
            return False

    def addAresta(self, verticeA, verticeB, ponderacao, rotulacao, direcionada):
        vA = next((v for v in self.__lista_de_vertices if v.getNome() == verticeA), None)
        vB = next((v for v in self.__lista_de_vertices if v.getNome() == verticeB), None)
    
        if not vA or not vB:
            print("Um ou ambos os vértices não existem no grafo.")
            return False

        aresta = Aresta(vA, vB, ponderacao, rotulacao, direcionada)

        if direcionada:
            if not any(a.getVerticeA() == vA and a.getVerticeB() == vB for a in self.__lista_de_arestas):
                self.__lista_de_arestas.append(aresta)
                self.__lista_de_adjacentes.setdefault(verticeA, []).append(verticeB)
                self.__predecessores.setdefault(verticeB, []).append(verticeA)
                self.__sucessores.setdefault(verticeA, []).append(verticeB)
                print(f"Aresta direcionada entre '{verticeA}' e '{verticeB}' adicionada com sucesso.")
            else:
                print("Aresta direcionada já existe. Aresta não adicionada.")
        else:
            if not any(
                (a.getVerticeA() == vA and a.getVerticeB() == vB) or 
                (a.getVerticeA() == vB and a.getVerticeB() == vA) for a in self.__lista_de_arestas
            ):
                self.__lista_de_arestas.append(aresta)
                self.__lista_de_adjacentes.setdefault(verticeA, []).append(verticeB)
                self.__lista_de_adjacentes.setdefault(verticeB, []).append(verticeA)
                print(f"Aresta não direcionada entre '{verticeA}' e '{verticeB}' adicionada com sucesso.")
            else:
                print("Aresta não direcionada já existe. Aresta não adicionada.")
    
        return True

    def removeAresta(self, verticeA, verticeB):
        arestas_removidas = False

        # Remove a aresta da lista de arestas
        self.__lista_de_arestas = [
            aresta for aresta in self.__lista_de_arestas
            if not (
                (aresta.getVerticeA().getNome() == verticeA and aresta.getVerticeB().getNome() == verticeB) or
                (not self.__direcionado and aresta.getVerticeA().getNome() == verticeB and aresta.getVerticeB().getNome() == verticeA)
            )
        ]

        # Atualiza as listas de adjacências, predecessores e sucessores
        if verticeA in self.__lista_de_adjacentes and verticeB in self.__lista_de_adjacentes[verticeA]:
            self.__lista_de_adjacentes[verticeA].remove(verticeB)
        if verticeB in self.__lista_de_adjacentes and verticeA in self.__lista_de_adjacentes[verticeB]:
            self.__lista_de_adjacentes[verticeB].remove(verticeA)

        if verticeA in self.__sucessores and verticeB in self.__sucessores[verticeA]:
            self.__sucessores[verticeA].remove(verticeB)
        if verticeB in self.__predecessores and verticeA in self.__predecessores[verticeB]:
            self.__predecessores[verticeB].remove(verticeA)

        if not self.__direcionado:
            if verticeB in self.__sucessores and verticeA in self.__sucessores[verticeB]:
                self.__sucessores[verticeB].remove(verticeA)
        if verticeA in self.__predecessores and verticeB in self.__predecessores[verticeA]:
                self.__predecessores[verticeA].remove(verticeB)

        arestas_removidas = True

        if arestas_removidas:
            print(f"Aresta entre '{verticeA}' e '{verticeB}' removida com sucesso.")
        else:
            print("Falha ao remover a aresta ou a aresta não existe.")

        return True

    def searchAresta(self, verticeA: str, verticeB: str):
        for aresta in self.__lista_de_arestas:
            direcionada = aresta.isDirecionada()

        if direcionada:
            if aresta.getVerticeA().getNome() == verticeA and aresta.getVerticeB().getNome() == verticeB:          
                print(f"A aresta direcionada {verticeA} -> {verticeB} existe")
        else:
            if (
                (aresta.getVerticeA().getNome() == verticeA and aresta.getVerticeB().getNome() == verticeB) or 
                (aresta.getVerticeA().getNome() == verticeB and aresta.getVerticeB().getNome() == verticeA)
            ):
                print(f"A aresta não direcionada {verticeA} - {verticeB} existe")

        return True
    
    def addVertice(self, rotulacao: str, ponderacao: int = 0) -> bool:
        for vertice in self.__lista_de_vertices:
            if vertice == rotulacao:
                print(f"O vértice '{rotulacao}' já existe no grafo.")
                return False

        novo_vertice = Vertice(rotulacao, ponderacao)
        self.__lista_de_vertices.append(novo_vertice)
        self.__lista_de_adjacentes[rotulacao] = []

        if ponderacao != 0:
            print(f"Vértice '{rotulacao}' com ponderação {ponderacao} adicionado ao grafo.")
        else:
            print(f"Vértice '{rotulacao}' adicionado ao grafo.")

        return True

    def removeVertice(self, rotulacao: str) -> bool:
        vertice_encontrado = None
        for vertice in self.__lista_de_vertices:
            if str(vertice) == rotulacao:  
                vertice_encontrado = vertice
                break


        if not vertice_encontrado:
            print(f"O vértice '{rotulacao}' não existe no grafo.")
            return False

        
        self.__lista_de_vertices.remove(vertice_encontrado)
        self.__lista_de_adjacentes.pop(rotulacao, None)

       
        self.__lista_de_arestas = [
            aresta for aresta in self.__lista_de_arestas
            if aresta.getVerticeA() != rotulacao and aresta.getVerticeB() != rotulacao
        ]

        print(f"Vértice '{rotulacao}' removido com sucesso.")
        return True
    
    def isEmpty(self) -> bool:
        return len(self.__lista_de_vertices) == 0
    
    def iscompleto(self):
        total_vertices = len(self.__lista_de_vertices)
        
        # Para cada par de vértices, devemos verificar se existe uma aresta entre eles.
        for i in range(total_vertices):
            for j in range(i + 1, total_vertices):
                verticeA = self.__lista_de_vertices[i]
                verticeB = self.__lista_de_vertices[j]
                
                # Checando se existe uma aresta entre os vértices i e j (misto)
                aresta_found = False
                for aresta in self.__lista_de_arestas:
                    # Se a aresta for não direcionada (A-B é equivalente a B-A)
                    if not aresta.isDirecionada():
                        if (aresta.getVerticeA() == verticeA and aresta.getVerticeB() == verticeB) or \
                           (aresta.getVerticeA() == verticeB and aresta.getVerticeB() == verticeA):
                            aresta_found = True
                            break
                    # Se a aresta for direcionada, verifica ambos os sentidos
                    elif aresta.isDirecionada():
                        if (aresta.getVerticeA() == verticeA and aresta.getVerticeB() == verticeB) or \
                           (aresta.getVerticeA() == verticeB and aresta.getVerticeB() == verticeA):
                            aresta_found = True
                            break
                
                if not aresta_found:
                    print(f"O grafo NÃO é completo. Falta aresta entre {verticeA} e {verticeB}")
                    return False

                # Para grafos direcionados, também devemos verificar a aresta no sentido contrário, se necessário
                if self.__direcionado:
                    aresta_found_reverse = False
                    for aresta in self.__lista_de_arestas:
                        if (aresta.getVerticeA() == verticeB and aresta.getVerticeB() == verticeA):
                            aresta_found_reverse = True
                            break
                    
                    if not aresta_found_reverse:
                        print(f"O grafo NÃO é completo. Falta aresta de retorno entre {verticeB} e {verticeA}")
                        return False
        
        print("O grafo é completo.")
        return True
    
    def gerar_matriz_incidencia(self) -> List[List[int]]:
        num_vertices = self.getNumVertices()
        num_arestas = self.getNumArestas()
        
        # Inicializa uma matriz de zeros com tamanho adequado
        matriz_incidencia = [[0 for _ in range(num_arestas)] for _ in range(num_vertices)]
        
        # Dicionário para mapear nomes dos vértices para índices da matriz
        vertice_to_index = {vertice.getNome(): index for index, vertice in enumerate(self.__lista_de_vertices)}

        for index_aresta, aresta in enumerate(self.__lista_de_arestas):
            verticeA = aresta.getVerticeA().getNome()
            verticeB = aresta.getVerticeB().getNome()
            direcionada = aresta.isDirecionada()

            matriz_incidencia[vertice_to_index[verticeA]][index_aresta] = -1 if direcionada else 1
            matriz_incidencia[vertice_to_index[verticeB]][index_aresta] = 1

        return matriz_incidencia

    def exibir_matriz_incidencia(self) -> None:
        matriz = self.gerar_matriz_incidencia()
        vertices = [vertice.getNome() for vertice in self.__lista_de_vertices]
        arestas = [(aresta.getVerticeA().getNome(), aresta.getVerticeB().getNome()) for aresta in self.__lista_de_arestas]
        
        # Título
        print("Matriz de Incidência (linhas = vértices, colunas = arestas):")
        
        # Cabeçalhos de arestas
        header = "       " + "  ".join(f"({a}, {b})" for a, b in arestas)
        print(header)
        
        # Corpo da matriz
        for vertice, linha in zip(vertices, matriz):
            valores = "  ".join(f"    {valor:2}" for valor in linha)
            print(f"{vertice}:  {valores}")

    def gerar_matriz_adjacencia(self) -> List[List[int]]:
        num_vertices = self.getNumVertices()
        num_arestas = self.getNumArestas()
        
        matriz_adjacencia = [[0] * num_vertices for _ in range(num_vertices)]
        
        vertice_to_index = {vertice.getNome(): index for index, vertice in enumerate(self.__lista_de_vertices)}

        for aresta in self.__lista_de_arestas:
            verticeA = aresta.getVerticeA().getNome()
            verticeB = aresta.getVerticeB().getNome()
            direcionada = aresta.isDirecionada()

            i = vertice_to_index[verticeA]
            j = vertice_to_index[verticeB]
            
            if direcionada:
                matriz_adjacencia[i][j] = 1
            else:
                matriz_adjacencia[i][j] = 1
                matriz_adjacencia[j][i] = 1

        return matriz_adjacencia

    def exibir_matriz_adjacencia(self) -> None:
        """
        Exibe a matriz de adjacência de forma legível, com linhas e colunas representando os vértices.
        """
        # Gera a matriz de adjacência
        matriz = self.gerar_matriz_adjacencia()
        
        # Obtém os nomes dos vértices
        vertices = [vertice.getNome() for vertice in self.__lista_de_vertices]
        
        # Título
        print("Matriz de Adjacência (linhas = vértices, colunas = vértices):")
        
        # Cabeçalhos de vértices
        header = "       " + "  ".join(f"{v:2}" for v in vertices)
        print(header)
        
        # Corpo da matriz
        for vertice, linha in zip(vertices, matriz):
            valores = "  ".join(f"{valor:2}" for valor in linha)
            print(f"{vertice:2}: {valores}")


    def gerar_lista_adjacencia(self) -> dict:

        # Inicializa o dicionário para a lista de adjacência
        lista_adjacencia = {vertice.getNome(): [] for vertice in self.__lista_de_vertices}

        # Preenche a lista de adjacência com base nas arestas
        for aresta in self.__lista_de_arestas:
            verticeA = aresta.getVerticeA().getNome()
            verticeB = aresta.getVerticeB().getNome()

            # Adiciona a conexão no dicionário
            lista_adjacencia[verticeA].append(verticeB)

            # Se a aresta não for direcionada, adiciona o inverso
            if not aresta.isDirecionada():
                lista_adjacencia[verticeB].append(verticeA)

        return lista_adjacencia
    
    def exibir_lista_adjacencia(self) -> None:
        lista_adjacencia = self.gerar_lista_adjacencia()

        # Exibe os dados
        print("Lista de Adjacência:")
        for vertice, adjacentes in lista_adjacencia.items():
            adjacentes_formatados = ", ".join(adjacentes)
            print(f"{vertice}: {adjacentes_formatados}")

    def busca_em_profundidade(self, start):
        # Verifica se o vértice de início está no grafo
        if start.getNome() not in self.__lista_de_adjacentes:
            print(f"O vértice '{start.getNome()}' não existe no grafo.")
            return []

        # Inicializa os tempos e pais dos vértices
        for v in self.__lista_de_vertices:
            v.set_tempo_termino(0)
            v.set_tempo_descoberta(0)
            v.set_vertice_pai(None)

        t = 0  # Tempo global
        # Função recursiva de busca em profundidade
        def busca_profundidade_recursiva(v):
            nonlocal t
            v.set_tempo_descoberta(t)
            t += 1

            # percorre os vizinhos do vertice
            for adj in self.__lista_de_adjacentes[v.getNome()]:
                if adj.get_tempo_descoberta() == 0:  # se o vértice adjacente ainda não foi visitado
                    adj.set_vertice_pai(v)
                    busca_profundidade_recursiva(adj)

            v.set_tempo_termino(t)
            t += 1

        start.set_tempo_descoberta(t)
        t += 1
        busca_profundidade_recursiva(start)
        return [v.getNome() for v in self.__lista_de_vertices if v.get_tempo_termino() > 0]

    def exibir_resultado_busca(self):
        print(f"{'Vértice':<10} {'Pai':<10} {'Tempo Descoberta':<20} {'Tempo Término':<20}")
        print("="*60)

        for v in self.__lista_de_vertices:
            pai_nome = v.get_vertice_pai().getNome() if v.get_vertice_pai() else "Nenhum"
            
            print(f"{v.getNome():<10} {pai_nome:<10} {v.get_tempo_descoberta():<20} {v.get_tempo_termino():<20}")
