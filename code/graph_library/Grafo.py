from typing import List, Dict
from graph_library.Aresta import Aresta
from graph_library.Vertice import Vertice

import random
import string
import xml.etree.ElementTree as ET

class Grafo:

    def __init__(self, isDirecionado=False):
        self.__lista_de_vertices = []
        self.__lista_de_arestas = []
        self.__lista_de_adjacentes: Dict[str, List[str]] = {}
        self.__predecessores: Dict[str, List[str]] = {}
        self.__sucessores: Dict[str, List[str]] = {}
        self.__direcionado: bool = isDirecionado

    def copy(self):
        copia = Grafo()
        
        # Copia os vértices
        for vertice in self.getVertices():
            copia.addVertice(vertice.getNome(), vertice.getPonderacao())
        
        # Copia as arestas
        for aresta in self.getArestas():
            copia.addAresta(
                aresta.getVerticeA().getNome(),
                aresta.getVerticeB().getNome(),
                aresta.getPonderacao(),
                aresta.getRotulacao(),
                aresta.isDirecionada()
            )
        
        return copia
    
    def reverse(self):
        reverso = Grafo()
        
        for vertice in self.getVertices():
            reverso.addVertice(vertice.getNome(), vertice.getPonderacao())
        
        for aresta in self.getAllArestas():
            if aresta.isDirecionada():
                # Inverte apenas arestas direcionadas
                reverso.addAresta(
                    aresta.getVerticeB().getNome(),  # Troca B com A
                    aresta.getVerticeA().getNome(),  # Troca A com B
                    aresta.getPonderacao(),
                    aresta.getRotulacao(),
                    aresta.isDirecionada()
                )
            else:
                # Copia arestas não direcionadas sem alterações
                reverso.addAresta(
                    aresta.getVerticeA().getNome(),
                    aresta.getVerticeB().getNome(),
                    aresta.getPonderacao(),
                    aresta.getRotulacao(),
                    aresta.isDirecionada()
                )
        
        return reverso
        
    def getVertices(self) -> List[str]:
        return self.__lista_de_vertices
    
    def getVertice(self, rotulacao: str):
        for vertice in self.__lista_de_vertices:
            if vertice.getNome() == rotulacao:
                return vertice
        return None
    
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

    @staticmethod
    def gerar_grafo_aleatorio(num_vertices=10, num_arestas=15):

        grafo = Grafo()

        for i in range(1, num_vertices + 1):
            id_vertice = str(i)
            peso = random.randint(1, 10)
            grafo.addVertice(id_vertice, peso)

        for _ in range(num_arestas):
            origem = str(random.randint(1, num_vertices))
            destino = str(random.randint(1, num_vertices))
            while origem == destino:
                destino = str(random.randint(1, num_vertices))
            
            ponderacao = random.randint(1, 100)
            rotulacao = random.choice(string.ascii_uppercase)
            direcionada = random.choice([True, False])

            grafo.addAresta(origem, destino, ponderacao=ponderacao, rotulacao=rotulacao, direcionada=direcionada)

        return grafo
    
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
    
        print(f"'{verticeA}' e '{verticeB}' NÃO são adjacentes.")
        return False

    def areAdjA(self, aresta1: Aresta, aresta2: Aresta) -> bool:
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
                self.__direcionado = True
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
        # Iterando sobre todas as arestas
        for aresta in self.__lista_de_arestas:
            # Verificando se a aresta é direcionada
            direcionada = aresta.isDirecionada()

            # Verificando a existência de uma aresta direcionada
            if direcionada:
                if aresta.getVerticeA().getNome() == verticeA and aresta.getVerticeB().getNome() == verticeB:
                    print(f"A aresta direcionada {verticeA} -> {verticeB} existe")
                    return True  # Retorna True assim que encontrar a aresta
            else:
                # Verificando a existência de uma aresta não direcionada
                if (
                    (aresta.getVerticeA().getNome() == verticeA and aresta.getVerticeB().getNome() == verticeB) or 
                    (aresta.getVerticeA().getNome() == verticeB and aresta.getVerticeB().getNome() == verticeA)
                ):
                    print(f"A aresta não direcionada {verticeA} - {verticeB} existe")
                    return True  # Retorna True assim que encontrar a aresta

        # Se não encontrou a aresta, retorna False
        print(f"A aresta entre {verticeA} e {verticeB} não existe.")
        return False

    
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
        
        matriz_incidencia = [[0 for _ in range(num_arestas)] for _ in range(num_vertices)]
        
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
        
        print("Matriz de Incidência (linhas = vértices, colunas = arestas):")
        
        header = "       " + "  ".join(f"({a}, {b})" for a, b in arestas)
        print(header)
        
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
        matriz = self.gerar_matriz_adjacencia()
        
        vertices = [vertice.getNome() for vertice in self.__lista_de_vertices]
        
        print("Matriz de Adjacência (linhas = vértices, colunas = vértices):")
        
        header = "     " + "  ".join(f"{v:2}" for v in vertices)
        print(header)
        
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

        print("Lista de Adjacência:")
        for vertice, adjacentes in lista_adjacencia.items():
            adjacentes_formatados = ", ".join(adjacentes)
            print(f"{vertice}: {adjacentes_formatados}")

    def busca_em_profundidade(self, visitados, start=None, direcionado=True):

        if start is None:
            if not self.__lista_de_vertices:
                print("O grafo não possui vértices.")
                return []
            start = self.__lista_de_vertices[0]

        if start.getNome() not in self.__lista_de_adjacentes:
            print(f"O vértice '{start.getNome()}' não existe no grafo.")
            return []

        for v in self.__lista_de_vertices:
            v.set_tempo_termino(0)
            v.set_tempo_descoberta(0)
            v.set_vertice_pai(None)

        t = 0

        visitados = set() 
        
        def busca_profundidade_recursiva(v):
            nonlocal t
            visitados.add(v.getNome())
            v.set_tempo_descoberta(t)
            t += 1

            for adjNome in self.__lista_de_adjacentes[v.getNome()]:
                adj = None
                for vAdj in self.getVertices():
                    if vAdj.getNome() == adjNome:
                        adj = vAdj
                        break

                if adj.get_tempo_descoberta() == 0:
                    adj.set_vertice_pai(v)
                    busca_profundidade_recursiva(adj)

            v.set_tempo_termino(t)
            t += 1

        start.set_tempo_descoberta(t)
        t += 1
        busca_profundidade_recursiva(start)

        if not direcionado:
            for v in self.__lista_de_vertices:
                if v.get_tempo_descoberta() == 0:
                    busca_profundidade_recursiva(v)

        return visitados

    def exibir_resultado_busca(self):
        vertices = self.getVertices()
        cabecalho = f"{'Atributo':<20}" + ''.join([f"{v.getNome():<10}" for v in vertices])
        print(cabecalho)
        print("=" * len(cabecalho))

        atributos = ['Tempo Descoberta', 'Tempo Término', 'Pai']

        for atributo in atributos:
            print(f"{atributo:<20}", end=" ")

            for v in vertices:
                if atributo == 'Pai':
                    pai_nome = v.get_vertice_pai().getNome() if v.get_vertice_pai() else "Nenhum"
                    print(f"{pai_nome:<10}", end=" ")
                elif atributo == 'Tempo Descoberta':
                    print(f"{v.get_tempo_descoberta():<10}", end=" ")
                elif atributo == 'Tempo Término':
                    print(f"{v.get_tempo_termino():<10}", end=" ")

            print()

    def kosaraju(self):
        if self.isEmpty():
            print("O grafo está vazio. Adicione vértices e arestas antes de executar o algoritmo.")
            return []

        visitados = set()
        self.busca_em_profundidade(visitados=visitados)

        grafo_reverso = self.reverse()

        self.__lista_de_vertices = sorted(self.__lista_de_vertices, key=lambda v: v.get_tempo_termino() if v.get_tempo_termino() is not None else float('inf'))

        visitados = set()
        grafo_reverso.busca_em_profundidade(visitados=visitados)

        count = 0
        for vertice in grafo_reverso.getVertices():
            pai = vertice.get_vertice_pai()
            if pai is None:
                count += 1

        return count

    def transformar_em_nao_direcionado(self):
        grafo_nao_direcionado = Grafo()
        
        for vertice in self.__lista_de_vertices:
            grafo_nao_direcionado.addVertice(vertice.getNome(), vertice.getPonderacao())
        
        for aresta in self.__lista_de_arestas:
            verticeA = aresta.getVerticeA().getNome()
            verticeB = aresta.getVerticeB().getNome()
            ponderacao = aresta.getPonderacao()
            rotulacao = aresta.getRotulacao()
            
            grafo_nao_direcionado.addAresta(verticeA, verticeB, ponderacao, rotulacao, direcionada=False)

        return grafo_nao_direcionado
    
    def verificar_semi_fortemente_conexo(self):
        grafo_nao_direcionado = self.transformar_em_nao_direcionado()

        visitados = set()
        grafo_nao_direcionado.busca_em_profundidade(visitados=visitados)
        
        return len(visitados) == grafo_nao_direcionado.getNumVertices()

    def verificar_simplesmente_conexo(self):
        if self.isEmpty():
            return False
        
        visitados = set()
        self.busca_em_profundidade(visitados, direcionado=False)
        
        return len(visitados) == self.getNumVertices()

    def identificar_conectividade(self):
        
        numComponentes = self.kosaraju()

        if not self.__direcionado or numComponentes == 1:
            print("O grafo é fortemente conexo.")
            return "fortemente conexo"

        if self.verificar_semi_fortemente_conexo():
            print("O grafo é semi-fortemente conexo.")
            return "semi-fortemente conexo"

        if self.verificar_simplesmente_conexo():
            print("O grafo é simplesmente conexo.")
            return "simplesmente conexo"

        print("O grafo não é conexo.")
        return "não conexo"

    def identificar_pontes(self):
        visitados = set()
        low = {}
        descobertas = {}
        pontes = []
        t = 0

        for v in self.__lista_de_vertices:
            low[v.getNome()] = float('inf')
            descobertas[v.getNome()] = 0

        def dfs_pontes(v):
            nonlocal t
            visitados.add(v.getNome())
            descobertas[v.getNome()] = low[v.getNome()] = t
            t += 1

            for adjNome in self.__lista_de_adjacentes[v.getNome()]:
                adj = None
                for vAdj in self.getVertices():
                    if vAdj.getNome() == adjNome:
                        adj = vAdj
                        break

                if adj.getNome() not in visitados:
                    adj.set_vertice_pai(v)
                    dfs_pontes(adj)

                    low[v.getNome()] = min(low[v.getNome()], low[adj.getNome()])

                    if low[adj.getNome()] > descobertas[v.getNome()]:
                        pontes.append((v.getNome(), adj.getNome()))

                elif adj != v.get_vertice_pai():
                    low[v.getNome()] = min(low[v.getNome()], descobertas[adj.getNome()])

        for v in self.__lista_de_vertices:
            if v.getNome() not in visitados:
                dfs_pontes(v)

        return pontes

    def identificar_articulacoes(self):
        tempo = 0
        articulacoes = set()
        visitados = set()
        tempos_descoberta = {}
        tempos_low = {}
        pais = {}

        for v in self.__lista_de_vertices:
            tempos_descoberta[v.getNome()] = -1 
            tempos_low[v.getNome()] = -1
            pais[v.getNome()] = None

    
        def dfs_articulacao(u):
            nonlocal tempo
            visitados.add(u)
            tempos_descoberta[u] = tempos_low[u] = tempo
            tempo += 1
            filhos = 0  

            for v in self.__lista_de_adjacentes[u]:
                if v not in visitados:
                    pais[v] = u
                    filhos += 1
                    dfs_articulacao(v)

                
                    tempos_low[u] = min(tempos_low[u], tempos_low[v])

            
                    if pais[u] is None and filhos > 1:
                        articulacoes.add(u)

                    if pais[u] is not None and tempos_low[v] >= tempos_descoberta[u]:
                        articulacoes.add(u)

                elif v != pais[u]:
                    tempos_low[u] = min(tempos_low[u], tempos_descoberta[v])


        for vertice in self.__lista_de_vertices:
            if vertice.getNome() not in visitados:
                dfs_articulacao(vertice.getNome())

        return articulacoes
    
    def exportar_para_gexf(self, nome_arquivo: str):

        gexf = ET.Element("gexf", xmlns="http://www.gexf.net/1.2draft", version="1.2")
        graph = ET.SubElement(gexf, "graph", defaultedgetype="directed" if self.__direcionado else "undirected", mode="static")

        nodes = ET.SubElement(graph, "nodes")
        for vertice in self.__lista_de_vertices:
            ET.SubElement(nodes, "node", id=vertice.getNome(), label=vertice.getNome())

        edges = ET.SubElement(graph, "edges")
        for index, aresta in enumerate(self.__lista_de_arestas):
            edge_attribs = {
                "id": str(index),
                "source": aresta.getVerticeA().getNome(),
                "target": aresta.getVerticeB().getNome(),
            }
            if aresta.isDirecionada():
                edge_attribs["type"] = "directed"
            ET.SubElement(edges, "edge", **edge_attribs)

        # Salvar no arquivo
        tree = ET.ElementTree(gexf)
        tree.write(nome_arquivo, encoding="utf-8", xml_declaration=True)