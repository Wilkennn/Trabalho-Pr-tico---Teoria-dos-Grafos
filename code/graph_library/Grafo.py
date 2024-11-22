from typing import List, Dict
from graph_library.Aresta import Aresta
from graph_library.Vertice import Vertice

import random
import string
import xml.etree.ElementTree as ET

class Grafo:

    def __init__(self, isDirecionado=None):
        self.__lista_de_vertices = []
        self.__lista_de_arestas = []
        self.__lista_de_adjacentes: Dict[str, List[str]] = {}
        self.__predecessores: Dict[str, List[str]] = {}
        self.__sucessores: Dict[str, List[str]] = {}
        self.__direcionado: bool = isDirecionado

    def copia(self):
        copia = Grafo()
        
        # Copia os vértices
        for vertice in self.obter_vertices():
            copia.adicionar_vertice(vertice.obter_nome(), vertice.obter_ponderacao())
        
        # Copia as arestas
        for aresta in self.obter_arestas():
            copia.adicionar_aresta(
                aresta.obter_vertice_A().obter_nome(),
                aresta.obter_vertice_B().obter_nome(),
                aresta.obter_ponderacao(),
                aresta.obter_rotulacao(),
                aresta.e_direcioanada()
            )
        
        return copia
    
    def inverter(self):
        reverso = Grafo()
        
        for vertice in self.obter_vertices():
            reverso.adicionar_vertice(vertice.obter_nome(), vertice.obter_ponderacao())
        
        for aresta in self.obter_todas_arestas():
            if aresta.e_direcioanada():

                reverso.adicionar_aresta(
                    aresta.obter_vertice_B().obter_nome(),
                    aresta.obter_vertice_A().obter_nome(),
                    aresta.obter_ponderacao(),
                    aresta.obter_rotulacao(),
                    aresta.e_direcioanada()
                )
            else:
                reverso.adicionar_aresta(
                    aresta.obter_vertice_A().obter_nome(),
                    aresta.obter_vertice_B().obter_nome(),
                    aresta.obter_ponderacao(),
                    aresta.obter_rotulacao(),
                    aresta.e_direcioanada()
                )
        
        return reverso
        
    def obter_vertices(self) -> List[str]:
        return self.__lista_de_vertices
    
    def obter_vertice(self, rotulacao: str):
        for vertice in self.__lista_de_vertices:
            if vertice.obter_nome() == rotulacao:
                return vertice
        return None
    
    def obter_adj(self) -> Dict[str, List[str]]:
        return self.__lista_de_adjacentes
    
    def obter_predecessores(self) -> Dict[str, List[str]]:
        return self.__predecessores
    
    def obter_sucessores(self) -> Dict[str, List[str]]:
        return self.__sucessores

    def obter_numero_vertices(self) -> int:
        return len(self.__lista_de_vertices)

    def obter_todas_arestas(self) -> List['Aresta']:
        return self.__lista_de_arestas
    
    def obter_numero_arestas(self) -> int:
        return len(self.__lista_de_arestas)

    @staticmethod
    def gerar_grafo_aleatorio(num_vertices=10, num_arestas=15):

        grafo = Grafo()

        for i in range(1, num_vertices + 1):
            id_vertice = str(i)
            peso = random.randint(1, 10)
            grafo.adicionar_vertice(id_vertice, peso)

        for _ in range(num_arestas):
            origem = str(random.randint(1, num_vertices))
            destino = str(random.randint(1, num_vertices))
            while origem == destino:
                destino = str(random.randint(1, num_vertices))
            
            ponderacao = random.randint(1, 100)
            rotulacao = random.choice(string.ascii_uppercase)
            direcionada = random.choice([True, False])

            grafo.adicionar_aresta(origem, destino, ponderacao=ponderacao, rotulacao=rotulacao, direcionada=direcionada)

        return grafo
    
    def sao_adj_v(self, verticeA: str, verticeB: str) -> bool:
        for aresta in self.__lista_de_arestas:
            direcionada = aresta.e_direcioanada()

            if direcionada:
                if aresta.obter_vertice_A().obter_nome() == verticeA and aresta.obter_vertice_B().obter_nome() == verticeB:
                    print(f"Os vértices '{verticeA}' e '{verticeB}' são adjacentes.")
                    print(f"{direcionada}")
                    return True
            else:
                if (
                    (aresta.obter_vertice_A().obter_nome() == verticeA and aresta.obter_vertice_B().obter_nome() == verticeB) or
                    (aresta.obter_vertice_A().obter_nome() == verticeB and aresta.obter_vertice_B().obter_nome() == verticeA)
                ):
                    print(f"Os vértices '{verticeA}' e '{verticeB}' são adjacentes.")
                    return True
    
        print(f"'{verticeA}' e '{verticeB}' NÃO são adjacentes.")
        return False

    def sao_adj_a(self, aresta1: Aresta, aresta2: Aresta) -> bool:
        verticeA1 = aresta1.obter_vertice_A().obter_nome()
        verticeB1 = aresta1.obter_vertice_B().obter_nome()
        verticeA2 = aresta2.obter_vertice_A().obter_nome()
        verticeB2 = aresta2.obter_vertice_B().obter_nome()
    
        if verticeA1 == verticeA2 or verticeA1 == verticeB2 or verticeB1 == verticeA2 or verticeB1 == verticeB2:
            print(f"As arestas com vértices ('{verticeA1}', '{verticeB1}') e ('{verticeA2}', '{verticeB2}') são adjacentes.")
            return True
        else:
            print(f"As arestas com vértices ('{verticeA1}', '{verticeB1}') e ('{verticeA2}', '{verticeB2}') NÃO são adjacentes.")
            return False

    def adicionar_aresta(self, verticeA, verticeB, ponderacao, rotulacao, direcionada):
        vA = next((v for v in self.__lista_de_vertices if v.obter_nome() == verticeA), None)
        vB = next((v for v in self.__lista_de_vertices if v.obter_nome() == verticeB), None)
    
        if not vA or not vB:
            print("Um ou ambos os vértices não existem no grafo.")
            return False

        aresta = Aresta(vA, vB, ponderacao, rotulacao, direcionada)

        if direcionada:
            if not any(a.obter_vertice_A() == vA and a.obter_vertice_B() == vB for a in self.__lista_de_arestas):
                self.__lista_de_arestas.append(aresta)
                self.__lista_de_adjacentes.setdefault(verticeA, []).append(verticeB)
                self.__lista_de_adjacentes.setdefault(verticeB, []).append(verticeA)
                self.__predecessores.setdefault(verticeB, []).append(verticeA)
                self.__sucessores.setdefault(verticeA, []).append(verticeB)
                if self.__direcionado is None:
                    self.__direcionado = True
                print(f"Aresta direcionada entre '{verticeA}' e '{verticeB}' adicionada com sucesso.")
            else:
                print("Aresta direcionada já existe. Aresta não adicionada.")
        else:
            if not any(
                (a.obter_vertice_A() == vA and a.obter_vertice_B() == vB) or
                (a.obter_vertice_A() == vB and a.obter_vertice_B() == vA) for a in self.__lista_de_arestas
            ):
                self.__lista_de_arestas.append(aresta)
                self.__lista_de_adjacentes.setdefault(verticeA, []).append(verticeB)
                self.__lista_de_adjacentes.setdefault(verticeB, []).append(verticeA)
                self.__direcionado = False
                print(f"Aresta não direcionada entre '{verticeA}' e '{verticeB}' adicionada com sucesso.")
            else:
                print("Aresta não direcionada já existe. Aresta não adicionada.")
    
        return True

    def remover_aresta(self, verticeA, verticeB):
        arestas_removidas = False

        self.__lista_de_arestas = [
            aresta for aresta in self.__lista_de_arestas
            if not (
                (aresta.obter_vertice_A().obter_nome() == verticeA and aresta.obter_vertice_B().obter_nome() == verticeB) or
                (not self.__direcionado and aresta.obter_vertice_A().obter_nome() == verticeB and aresta.obter_vertice_B().obter_nome() == verticeA)
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

    def buscar_aresta(self, verticeA: str, verticeB: str):
        
        for aresta in self.__lista_de_arestas:
            direcionada = aresta.e_direcioanada()

            if direcionada:
                if aresta.obter_vertice_A().obter_nome() == verticeA and aresta.obter_vertice_B().obter_nome() == verticeB:
                    print(f"A aresta direcionada {verticeA} -> {verticeB} existe")
                    return True
            else:
                if (
                    (aresta.obter_vertice_A().obter_nome() == verticeA and aresta.obter_vertice_B().obter_nome() == verticeB) or
                    (aresta.obter_vertice_A().obter_nome() == verticeB and aresta.obter_vertice_B().obter_nome() == verticeA)
                ):
                    print(f"A aresta não direcionada {verticeA} - {verticeB} existe")
                    return True

        print(f"A aresta entre {verticeA} e {verticeB} não existe.")
        return False
    
    def adicionar_vertice(self, rotulacao: str, ponderacao: int = 0) -> bool:
        for vertice in self.__lista_de_vertices:
            if vertice == rotulacao:
                print(f"O vértice '{rotulacao}' já existe no grafo.")
                return False

        novo_vertice = Vertice(rotulacao, ponderacao)
        self.__lista_de_vertices.append(novo_vertice)
        self.__lista_de_adjacentes[rotulacao] = []
        self.__sucessores[rotulacao] = []
        self.__predecessores[rotulacao] = []

        if ponderacao != 0:
            print(f"Vértice '{rotulacao}' com ponderação {ponderacao} adicionado ao grafo.")
        else:
            print(f"Vértice '{rotulacao}' adicionado ao grafo.")

        return True

    def remover_vertice(self, rotulacao: str) -> bool:
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
            if aresta.obter_vertice_A() != rotulacao and aresta.obter_vertice_B() != rotulacao
        ]

        print(f"Vértice '{rotulacao}' removido com sucesso.")
        return True
    
    def esta_vazio(self) -> bool:
        return len(self.__lista_de_vertices) == 0
    
    def e_completo(self):
        total_vertices = len(self.__lista_de_vertices)
        
        for i in range(total_vertices):
            for j in range(i + 1, total_vertices):
                verticeA = self.__lista_de_vertices[i]
                verticeB = self.__lista_de_vertices[j]
                
                
                aresta_found = False
                for aresta in self.__lista_de_arestas:
                    
                    if not aresta.e_direcioanada():
                        if (aresta.obter_vertice_A() == verticeA and aresta.obter_vertice_B() == verticeB) or \
                           (aresta.obter_vertice_A() == verticeB and aresta.obter_vertice_B() == verticeA):
                            aresta_found = True
                            break
                    
                    elif aresta.e_direcioanada():
                        if (aresta.obter_vertice_A() == verticeA and aresta.obter_vertice_B() == verticeB) or \
                           (aresta.obter_vertice_A() == verticeB and aresta.obter_vertice_B() == verticeA):
                            aresta_found = True
                            break
                
                if not aresta_found:
                    print(f"O grafo NÃO é completo. Falta aresta entre {verticeA} e {verticeB}")
                    return False

                if self.__direcionado:
                    aresta_found_inverter = False
                    for aresta in self.__lista_de_arestas:
                        if (aresta.obter_vertice_A() == verticeB and aresta.obter_vertice_B() == verticeA):
                            aresta_found_inverter = True
                            break
                    
                    if not aresta_found_inverter:
                        print(f"O grafo NÃO é completo. Falta aresta de retorno entre {verticeB} e {verticeA}")
                        return False
        
        print("O grafo é completo.")
        return True
    
    def gerar_matriz_incidencia(self) -> List[List[int]]:
        num_vertices = self.obter_numero_vertices()
        num_arestas = self.obter_numero_arestas()
        
        matriz_incidencia = [[0 for _ in range(num_arestas)] for _ in range(num_vertices)]
        
        vertice_to_index = {vertice.obter_nome(): index for index, vertice in enumerate(self.__lista_de_vertices)}

        for index_aresta, aresta in enumerate(self.__lista_de_arestas):
            verticeA = aresta.obter_vertice_A().obter_nome()
            verticeB = aresta.obter_vertice_B().obter_nome()
            direcionada = aresta.e_direcioanada()

            matriz_incidencia[vertice_to_index[verticeA]][index_aresta] = -1 if direcionada else 1
            matriz_incidencia[vertice_to_index[verticeB]][index_aresta] = 1

        return matriz_incidencia

    def exibir_matriz_incidencia(self) -> None:
        matriz = self.gerar_matriz_incidencia()
        vertices = [vertice.obter_nome() for vertice in self.__lista_de_vertices]
        arestas = [(aresta.obter_vertice_A().obter_nome(), aresta.obter_vertice_B().obter_nome()) for aresta in self.__lista_de_arestas]
        
        print("Matriz de Incidência (linhas = vértices, colunas = arestas):")
        
        header = "       " + "  ".join(f"({a}, {b})" for a, b in arestas)
        print(header)
        
        for vertice, linha in zip(vertices, matriz):
            valores = "  ".join(f"    {valor:2}" for valor in linha)
            print(f"{vertice}:  {valores}")

    def gerar_matriz_adjacencia(self) -> List[List[int]]:
        num_vertices = self.obter_numero_vertices()
        num_arestas = self.obter_numero_arestas()
        
        matriz_adjacencia = [[0] * num_vertices for _ in range(num_vertices)]
        
        vertice_to_index = {vertice.obter_nome(): index for index, vertice in enumerate(self.__lista_de_vertices)}

        for aresta in self.__lista_de_arestas:
            verticeA = aresta.obter_vertice_A().obter_nome()
            verticeB = aresta.obter_vertice_B().obter_nome()
            direcionada = aresta.e_direcioanada()

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
        
        vertices = [vertice.obter_nome() for vertice in self.__lista_de_vertices]
        
        print("Matriz de Adjacência (linhas = vértices, colunas = vértices):")
        
        header = "     " + "  ".join(f"{v:2}" for v in vertices)
        print(header)
        
        for vertice, linha in zip(vertices, matriz):
            valores = "  ".join(f"{valor:2}" for valor in linha)
            print(f"{vertice:2}: {valores}")

    def gerar_lista_adjacencia(self) -> dict:

        lista_adjacencia = {vertice.obter_nome(): [] for vertice in self.__lista_de_vertices}

        for aresta in self.__lista_de_arestas:
            verticeA = aresta.obter_vertice_A().obter_nome()
            verticeB = aresta.obter_vertice_B().obter_nome()

            lista_adjacencia[verticeA].append(verticeB)

            if not aresta.e_direcioanada():
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

        if start.obter_nome() not in self.__lista_de_adjacentes:
            print(f"O vértice '{start.obter_nome()}' não existe no grafo.")
            return []

        for v in self.__lista_de_vertices:
            v.set_tempo_termino(0)
            v.set_tempo_descoberta(0)
            v.set_vertice_pai(None)

        t = 0

        visitados = set()
        
        def busca_profundidade_recursiva(v):
            nonlocal t
            visitados.add(v.obter_nome())
            v.set_tempo_descoberta(t)
            t += 1

            for adjNome in self.__lista_de_adjacentes[v.obter_nome()]:
                adj = None
                for vAdj in self.obter_vertices():
                    if vAdj.obter_nome() == adjNome:
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

    def exibir_resultado_busca_em_profundidade(self):
        vertices = self.obter_vertices()
        cabecalho = f"{'Atributo':<20}" + ''.join([f"{v.obter_nome():<10}" for v in vertices])
        print(cabecalho)
        print("=" * len(cabecalho))

        atributos = ['Tempo Descoberta', 'Tempo Término', 'Pai']

        for atributo in atributos:
            print(f"{atributo:<20}", end=" ")

            for v in vertices:
                if atributo == 'Pai':
                    pai_nome = v.get_vertice_pai().obter_nome() if v.get_vertice_pai() else "Nenhum"
                    print(f"{pai_nome:<10}", end=" ")
                elif atributo == 'Tempo Descoberta':
                    print(f"{v.get_tempo_descoberta():<10}", end=" ")
                elif atributo == 'Tempo Término':
                    print(f"{v.get_tempo_termino():<10}", end=" ")

            print()

    def algoritmo_de_kosaraju(self):
        if self.esta_vazio():
            print("O grafo está vazio. Adicione vértices e arestas antes de executar o algoritmo.")
            return []

        visitados = set()
        self.busca_em_profundidade(visitados=visitados)

        grafo_reverso = self.inverter()

        self.__lista_de_vertices = sorted(self.__lista_de_vertices, key=lambda v: v.get_tempo_termino() if v.get_tempo_termino() is not None else float('inf'))

        visitados = set()
        grafo_reverso.busca_em_profundidade(visitados=visitados)

        count = 0
        for vertice in grafo_reverso.obter_vertices():
            pai = vertice.get_vertice_pai()
            if pai is None:
                count += 1

        return count

    def transformar_em_nao_direcionado(self):
        grafo_nao_direcionado = Grafo()
        
        for vertice in self.__lista_de_vertices:
            grafo_nao_direcionado.adicionar_vertice(vertice.obter_nome(), vertice.obter_ponderacao())
        
        for aresta in self.__lista_de_arestas:
            verticeA = aresta.obter_vertice_A().obter_nome()
            verticeB = aresta.obter_vertice_B().obter_nome()
            ponderacao = aresta.obter_ponderacao()
            rotulacao = aresta.obter_rotulacao()
            
            grafo_nao_direcionado.adicionar_aresta(verticeA, verticeB, ponderacao, rotulacao, direcionada=False)

        return grafo_nao_direcionado
    
    def verificar_semi_fortemente_conexo(self):
        grafo_nao_direcionado = self.transformar_em_nao_direcionado()

        visitados = set()
        grafo_nao_direcionado.busca_em_profundidade(visitados=visitados)
        
        return len(visitados) == grafo_nao_direcionado.obter_numero_vertices()

    def verificar_simplesmente_conexo(self):
        if self.esta_vazio():
            return False
        
        visitados = set()
        self.busca_em_profundidade(visitados, direcionado=False)
        
        return len(visitados) == self.obter_numero_vertices()

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

    def identificar_pontes_tarjan(self):
        visitados = set()
        low = {}
        descobertas = {}
        pontes = []
        t = 0

        for v in self.__lista_de_vertices:
            low[v.obter_nome()] = float('inf')
            descobertas[v.obter_nome()] = 0

        def dfs_pontes(v):
            nonlocal t
            visitados.add(v.obter_nome())
            descobertas[v.obter_nome()] = low[v.obter_nome()] = t
            t += 1

            for adjNome in self.__lista_de_adjacentes[v.obter_nome()]:
                adj = None
                for vAdj in self.obter_vertices():
                    if vAdj.obter_nome() == adjNome:
                        adj = vAdj
                        break

                if adj.obter_nome() not in visitados:
                    adj.set_vertice_pai(v)
                    dfs_pontes(adj)

                    low[v.obter_nome()] = min(low[v.obter_nome()], low[adj.obter_nome()])

                    if low[adj.obter_nome()] > descobertas[v.obter_nome()]:
                        pontes.append((v.obter_nome(), adj.obter_nome()))

                elif adj != v.get_vertice_pai():
                    low[v.obter_nome()] = min(low[v.obter_nome()], descobertas[adj.obter_nome()])

        for v in self.__lista_de_vertices:
            if v.obter_nome() not in visitados:
                dfs_pontes(v)

        pontes.inverter()
        return pontes

    def identificar_pontes_naive(self):
        pontes = []
        for aresta in self.__lista_de_arestas:
            verticeA = aresta.obter_vertice_A().obter_nome()
            verticeB = aresta.obter_vertice_B().obter_nome()
            ponderacao = aresta.obter_ponderacao()
            rotulacao = aresta.obter_rotulacao()
            direcionada = aresta.e_direcioanada()

            self.remover_aresta(verticeA, verticeB)

            if self.identificar_conectividade() == "não conexo":
                pontes.append((verticeA, verticeB))
 
            self.adicionar_aresta(verticeA, verticeB, ponderacao, rotulacao, direcionada)
        return pontes

    def identificar_articulacoes(self):
        tempo = 0
        articulacoes = set()
        visitados = set()
        tempos_descoberta = {}
        tempos_low = {}
        pais = {}

        for v in self.__lista_de_vertices:
            tempos_descoberta[v.obter_nome()] = -1
            tempos_low[v.obter_nome()] = -1
            pais[v.obter_nome()] = None

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
            if vertice.obter_nome() not in visitados:
                dfs_articulacao(vertice.obter_nome())

        return articulacoes
            
    def euleriano(self):
        print(self.__direcionado)

        if self.__direcionado:
            conectividade = self.identificar_conectividade()
            if not conectividade == 'fortemente conexo':
                print("Grafo não é fortemente conexo. Não é euleriano.")
                return False

            for v in self.__lista_de_vertices:
                in_degree = len(self.__predecessores.get(v.obter_nome(), []))  
                out_degree = len(self.__sucessores.get(v.obter_nome(), [])) 
        
                if in_degree != out_degree:
                    return False

            print("O grafo é euleriano!")
            return True

        conectividade_nao_direcionado = self.identificar_conectividade()
    
        if conectividade_nao_direcionado == "não conexo":
            print("Grafo não é conexo. Não é euleriano.")
            return False

        grau_impar = 0
        for v in self.__lista_de_vertices:
            adjacentes = self.__lista_de_adjacentes.get(v.obter_nome(), [])
        
            if len(adjacentes) % 2 != 0:
                grau_impar += 1

        if grau_impar == 0 or grau_impar == 2:
            print("O grafo é euleriano!")
            return True
        else:
            print("O grafo não é euleriano!")
            return False
  
    def algoritmo_de_fleury(self):
        if not self.isEuleriano():
            print("O grafo não é euleriano.")
            return None
    
        caminho = []
    
        grafo_copia = self.copia()
    
        vertice_inicial = None
        for v in grafo_copia.obter_vertices():
            if len(grafo_copia.getArestasAdjacentes(v)) % 2 != 0:
                vertice_inicial = v
                break
        if vertice_inicial is None:
            vertice_inicial = grafo_copia.obter_vertices()[0]
    
        def fleury(v):
            for adjNome in grafo_copia.getArestasAdjacentes(v):
                adj = grafo_copia.obter_vertice(adjNome)
            
                if self.is_conexo_removendo(v, adj):
                    caminho.append((v.obter_nome(), adj.obter_nome()))
                    grafo_copia.remover_aresta(v, adj)
                    fleury(adj)
                    return

                caminho.append((v.obter_nome(), adj.obter_nome()))
                grafo_copia.remover_aresta(v, adj)
                fleury(adj)
                return

        fleury(vertice_inicial)
    
        return caminho

    def exportar_para_gexf(self, nome_arquivo: str):

        gexf = ET.Element("gexf", xmlns="http://www.gexf.net/1.2draft", version="1.2")
        graph = ET.SubElement(gexf, "graph", defaultedgetype="directed" if self.__direcionado else "undirected", mode="static")

        nodes = ET.SubElement(graph, "nodes")
        for vertice in self.__lista_de_vertices:
            ET.SubElement(nodes, "node", id=vertice.obter_nome(), label=vertice.obter_nome())

        edges = ET.SubElement(graph, "edges")
        for index, aresta in enumerate(self.__lista_de_arestas):
            edge_attribs = {
                "id": str(index),
                "source": aresta.obter_vertice_A().obter_nome(),
                "target": aresta.obter_vertice_B().obter_nome(),
            }
            if aresta.e_direcioanada():
                edge_attribs["type"] = "directed"
            ET.SubElement(edges, "edge", **edge_attribs)

        tree = ET.ElementTree(gexf)
        tree.write(nome_arquivo, encoding="utf-8", xml_declaration=True)