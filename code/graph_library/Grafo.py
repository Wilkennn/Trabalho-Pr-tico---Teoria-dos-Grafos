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

    def obter_lista_adjacencia(self):
        return self.__lista_de_adjacentes;

    def copia(self):
        copia = Grafo()

        for vertice in self.obter_vertices():
            copia.adicionar_vertice(vertice.obter_nome(), vertice.obter_ponderacao())

        for aresta in self.obter_todas_arestas():
            copia.adicionar_aresta(
                aresta.obter_vertice_A().obter_nome(),
                aresta.obter_vertice_B().obter_nome(),
                aresta.obter_ponderacao(),
                aresta.obter_rotulacao(),
                aresta.e_direcionada()
            )

        return copia

    def inverter(self):
        reverso = Grafo()

        # Adiciona os vértices ao grafo reverso
        for vertice in self.obter_vertices():
            reverso.adicionar_vertice(vertice.obter_nome(), vertice.obter_ponderacao())

        # Inicia as listas de adjacência, predecessores e sucessores para o grafo reverso
        reverso.__lista_de_adjacentes = {vertice.obter_nome(): [] for vertice in self.obter_vertices()}
        reverso.__predecessores = {vertice.obter_nome(): [] for vertice in self.obter_vertices()}
        reverso.__sucessores = {vertice.obter_nome(): [] for vertice in self.obter_vertices()}

        # Adiciona as arestas e inverte as listas de adjacência, predecessores e sucessores
        for aresta in self.obter_todas_arestas():
            if aresta.e_direcionada():
                # Inverte a direção da aresta
                reverso.adicionar_aresta(
                    aresta.obter_vertice_B().obter_nome(),
                    aresta.obter_vertice_A().obter_nome(),
                    aresta.obter_ponderacao(),
                    aresta.obter_rotulacao(),
                    aresta.e_direcionada()
                )
                # Atualiza as listas de adjacência, predecessores e sucessores para a inversão
                reverso.__lista_de_adjacentes[aresta.obter_vertice_B().obter_nome()].append(aresta.obter_vertice_A())
                reverso.__predecessores[aresta.obter_vertice_A().obter_nome()].append(aresta.obter_vertice_B())
                reverso.__sucessores[aresta.obter_vertice_B().obter_nome()].append(aresta.obter_vertice_A())
            else:
                # Se a aresta não é direcionada, ela é inserida nos dois sentidos
                reverso.adicionar_aresta(
                    aresta.obter_vertice_A().obter_nome(),
                    aresta.obter_vertice_B().obter_nome(),
                    aresta.obter_ponderacao(),
                    aresta.obter_rotulacao(),
                    aresta.e_direcionada()
                )
                reverso.adicionar_aresta(
                    aresta.obter_vertice_B().obter_nome(),
                    aresta.obter_vertice_A().obter_nome(),
                    aresta.obter_ponderacao(),
                    aresta.obter_rotulacao(),
                    aresta.e_direcionada()
                )

                # Atualiza as listas de adjacência, predecessores e sucessores para arestas não direcionadas
                reverso.__lista_de_adjacentes[aresta.obter_vertice_A().obter_nome()].append(aresta.obter_vertice_B())
                reverso.__lista_de_adjacentes[aresta.obter_vertice_B().obter_nome()].append(aresta.obter_vertice_A())
                reverso.__predecessores[aresta.obter_vertice_B().obter_nome()].append(aresta.obter_vertice_A())
                reverso.__sucessores[aresta.obter_vertice_A().obter_nome()].append(aresta.obter_vertice_B())

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

    def obter_arestas_ajacentes_ao_vertice(self, vertice):
        arestas_adjacentes = []

        for aresta in self.__lista_de_arestas:
            # Verifica se o vértice A ou B da aresta é igual ao vértice passado como argumento
            if aresta.obter_vertice_A() == vertice or aresta.obter_vertice_B() == vertice:
                arestas_adjacentes.append(aresta)

        return arestas_adjacentes

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
            direcionada = aresta.e_direcionada()

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
                self.__lista_de_adjacentes.setdefault(verticeA, []).append(vB)
                self.__predecessores.setdefault(verticeB, []).append(vA)
                self.__sucessores.setdefault(verticeA, []).append(vB)
                
                self.__direcionado = True

                print(f"Aresta direcionada entre '{verticeA}' e '{verticeB}' adicionada com sucesso.")
            else:
                # print("Aresta direcionada já existe. Aresta não adicionada.")
                return False

        else:
            if not any(
                (a.obter_vertice_A() == vA and a.obter_vertice_B() == vB) or
                (a.obter_vertice_A() == vB and a.obter_vertice_B() == vA) for a in self.__lista_de_arestas
            ):
                self.__lista_de_arestas.append(aresta)
                self.__lista_de_adjacentes.setdefault(verticeA, []).append(vB)
                self.__lista_de_adjacentes.setdefault(verticeB, []).append(vA)
                self.__predecessores.setdefault(verticeB, []).append(vA)
                self.__predecessores.setdefault(verticeA, []).append(vB)
                self.__sucessores.setdefault(verticeA, []).append(vB)
                self.__sucessores.setdefault(verticeB, []).append(vA)

                self.__direcionado = False

                print(f"Aresta não direcionada entre '{verticeA}' e '{verticeB}' adicionada com sucesso.")
            else:
                # print("Aresta não direcionada já existe. Aresta não adicionada.")
                return False

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

        # if arestas_removidas:
        #     print(f"Aresta entre '{verticeA}' e '{verticeB}' removida com sucesso.")
        # else:
        #     print("Falha ao remover a aresta ou a aresta não existe.")

        return True

    def buscar_aresta(self, verticeA: str, verticeB: str):

        for aresta in self.__lista_de_arestas:
            direcionada = aresta.e_direcionada()

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

        # print(f"Vértice '{rotulacao}' removido com sucesso.")
        return True

    def esta_vazio(self) -> bool:
        return self.obter_numero_vertices()== 0

    def e_completo(self):
        
        total_vertices = self.obter_numero_vertices()
        total_arestas  = self.obter_numero_arestas()

        num_maximo_arestas = 0
        if not self.__direcionado:
            num_maximo_arestas = (total_vertices * (total_vertices - 1)) // 2
        else:
            num_maximo_arestas = total_vertices * (total_vertices - 1)
            
        if total_arestas != num_maximo_arestas:
            return False
        
        for vertice in self.__lista_de_vertices:
            for adj in self.__lista_de_adjacentes[vertice.obter_nome()]:
                if adj != vertice:
                    if vertice not in self.__lista_de_adjacentes[adj.obter_nome()]:
                        print(f"Faltando aresta: {adj} -> {vertice}")
                        return False

        return True

    def gerar_matriz_incidencia(self) -> List[List[int]]:
        num_vertices = self.obter_numero_vertices()
        num_arestas = self.obter_numero_arestas()

        matriz_incidencia = [[0 for _ in range(num_arestas)] for _ in range(num_vertices)]

        vertice_to_index = {vertice.obter_nome(): index for index, vertice in enumerate(self.__lista_de_vertices)}

        for index_aresta, aresta in enumerate(self.__lista_de_arestas):
            verticeA = aresta.obter_vertice_A().obter_nome()
            verticeB = aresta.obter_vertice_B().obter_nome()
            direcionada = aresta.e_direcionada()

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

        matriz_adjacencia = [[0] * num_vertices for _ in range(num_vertices)]

        vertice_to_index = {vertice.obter_nome(): index for index, vertice in enumerate(self.__lista_de_vertices)}

        for aresta in self.__lista_de_arestas:
            verticeA = aresta.obter_vertice_A().obter_nome()
            verticeB = aresta.obter_vertice_B().obter_nome()
            direcionada = aresta.e_direcionada()

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

            if not aresta.e_direcionada():
                lista_adjacencia[verticeB].append(verticeA)

        return lista_adjacencia

    def exibir_lista_adjacencia(self) -> None:
        lista_adjacencia = self.gerar_lista_adjacencia()

        print("Lista de Adjacência:")
        for vertice, adjacentes in lista_adjacencia.items():
            adjacentes_formatados = ", ".join(adjacentes)
            print(f"{vertice}: {adjacentes_formatados}")

    def busca_em_profundidade(self, start=None):

        if start is None:
            if not self.__lista_de_vertices:
                print("O grafo não possui vértices.")
                return []
            start = self.__lista_de_vertices[0]

        if start.obter_nome() not in self.__lista_de_adjacentes:
            print(f"O vértice '{start.obter_nome()}' não existe no grafo.")
            return []

        for v in self.__lista_de_vertices:
            v.set_tempo_termino(None)
            v.set_tempo_descoberta(None)
            v.set_vertice_pai(None)

        t = 0
        visitados = set()

        def busca_profundidade_recursiva(v):
            nonlocal t
            visitados.add(v)
            v.set_tempo_descoberta(t)
            t += 1

            for adj in self.__lista_de_adjacentes[v.obter_nome()]:
                if adj and adj.obter_tempo_descoberta() is None:
                    adj.set_vertice_pai(v)
                    busca_profundidade_recursiva(adj)

            v.set_tempo_termino(t)
            t += 1

        start.set_tempo_descoberta(t)
        t += 1
        busca_profundidade_recursiva(start)

        for v in self.__lista_de_vertices:
                if v.obter_tempo_descoberta() is None:
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
                    pai_nome = v.obter_vertice_pai().obter_nome() if v.obter_vertice_pai() else "Nenhum"
                    print(f"{pai_nome:<10}", end=" ")
                elif atributo == 'Tempo Descoberta':
                    print(f"{v.obter_tempo_descoberta() or 'N/A':<10}", end=" ")
                elif atributo == 'Tempo Término':
                    print(f"{v.obter_tempo_termino():<10}", end=" ")

            print()

    def algoritmo_de_kosaraju(self):
        if self.esta_vazio():
            print("O grafo está vazio. Adicione vértices e arestas antes de executar o algoritmo.")
            return []

        self.busca_em_profundidade()

        self.__lista_de_vertices.sort(
            key=lambda v: v.obter_tempo_termino() if v.obter_tempo_termino() is not None else float('-inf'),
            reverse=True
        )

        grafo_reverso = self.inverter()

        grafo_reverso.busca_em_profundidade()

        visitados = grafo_reverso.busca_em_profundidade()

        count = 0
        for vertice in visitados:
            pai = vertice.obter_vertice_pai()
            if pai is None:
                count+=1

        return count

    def transformar_em_nao_direcionado(self):

        if not self.__direcionado:
            return self

        grafo_nao_direcionado = self.copia();

        for vertice in self.obter_vertices():
            grafo_nao_direcionado.adicionar_vertice(vertice.obter_nome(), vertice.obter_ponderacao())

        for aresta in self.obter_todas_arestas():
            verticeA = aresta.obter_vertice_A()
            verticeB = aresta.obter_vertice_B()
            ponderacao = aresta.obter_ponderacao()
            rotulacao = aresta.obter_rotulacao()

            grafo_nao_direcionado.adicionar_aresta(
                verticeA.obter_nome(), verticeB.obter_nome(), ponderacao, rotulacao, direcionada=False
            )

            grafo_nao_direcionado.__lista_de_adjacentes.setdefault(verticeA.obter_nome(), []).append(verticeB)
            grafo_nao_direcionado.__lista_de_adjacentes.setdefault(verticeB.obter_nome(), []).append(verticeA)

            grafo_nao_direcionado.__predecessores.setdefault(verticeA.obter_nome(), []).append(verticeB)
            grafo_nao_direcionado.__predecessores.setdefault(verticeB.obter_nome(), []).append(verticeA)
            grafo_nao_direcionado.__sucessores.setdefault(verticeA.obter_nome(), []).append(verticeB)
            grafo_nao_direcionado.__sucessores.setdefault(verticeB.obter_nome(), []).append(verticeA)

        return grafo_nao_direcionado
    
    def verificar_fortemente_conexo(self):
        if self.esta_vazio():
            return False

        numero_componentes = self.algoritmo_de_kosaraju()

        return numero_componentes == 1

    def verificar_semi_fortemente_conexo(self):
        if self.esta_vazio():
            return False

        visitados = self.busca_em_profundidade()

        return len(visitados) == self.obter_numero_vertices()

    def verificar_simplesmente_conexo(self):
        if self.esta_vazio():
            return False

        grafo_nao_direcionado = self.transformar_em_nao_direcionado()

        visitados = grafo_nao_direcionado.busca_em_profundidade()

        return len(visitados) == grafo_nao_direcionado.obter_numero_vertices()

    def identificar_conectividade(self):
        if self.__direcionado:
            if self.verificar_fortemente_conexo():
                print("O grafo é fortemente conexo.")
            elif self.verificar_semi_fortemente_conexo():
                print("O grafo é semi-fortemente conexo.")
            else:
                print("O grafo não é fortemente nem semi-fortemente conexo.")
        else:
            if self.verificar_simplesmente_conexo():
                print("O grafo é simplesmente conexo.")
            else:
                print("O grafo não é conexo.")

        return self.verificar_fortemente_conexo() or self.verificar_semi_fortemente_conexo() or self.verificar_simplesmente_conexo()

    def identificar_pontes_tarjan(self):
        visitados = set()
        low = {}
        descobertas = {}
        pontes = []
        t = 0

        for v in self.__lista_de_vertices:
            low[v.obter_nome()] = float('inf')
            descobertas[v.obter_nome()] = -1

        def dfs_pontes(v):
            nonlocal t
            visitados.add(v.obter_nome())
            descobertas[v.obter_nome()] = low[v.obter_nome()] = t
            t += 1
            for adj in self.__lista_de_adjacentes[v.obter_nome()]:

                if adj.obter_nome() not in visitados:
                    adj.set_vertice_pai(v)
                    dfs_pontes(adj)

                    low[v.obter_nome()] = min(low[v.obter_nome()], low[adj.obter_nome()])

                    if low[adj.obter_nome()] > descobertas[v.obter_nome()]:
                        pontes.append((v.obter_nome(), adj.obter_nome()))

                elif adj.obter_nome() != (v.obter_vertice_pai().obter_nome() if v.obter_vertice_pai() else None):
                    low[v.obter_nome()] = min(low[v.obter_nome()], descobertas[adj.obter_nome()])

        for v in self.__lista_de_vertices:
            if v.obter_nome() not in visitados:
                dfs_pontes(v)

        pontes.reverse()
        print("Tarjam", pontes)
        return pontes

    def identificar_pontes_naive(self):
        pontes = []
        for aresta in self.__lista_de_arestas:
            verticeA = aresta.obter_vertice_A().obter_nome()
            verticeB = aresta.obter_vertice_B().obter_nome()
            ponderacao = aresta.obter_ponderacao()
            rotulacao = aresta.obter_rotulacao()
            direcionada = aresta.e_direcionada()

            self.remover_aresta(verticeA, verticeB)

            if self.identificar_conectividade() == "não conexo":
                pontes.append((verticeA, verticeB))

            self.adicionar_aresta(verticeA, verticeB, ponderacao, rotulacao, direcionada)

        print("Naive", pontes)
        return pontes

    def identificar_articulacoes(self):
        tempo = 0
        articulacoes = set()
        visitados = set()
        tempos_descoberta = {}
        tempos_low = {}
        pais = {}
        filhos = {}

        for v in self.__lista_de_vertices:
            nome = v.obter_nome()
            tempos_descoberta[nome] = -1
            tempos_low[nome] = -1
            pais[nome] = None
            filhos[nome] = 0

        def dfs_articulacao(u):
            nonlocal tempo
            nome_u = u.obter_nome()
            visitados.add(nome_u)
            tempos_descoberta[nome_u] = tempos_low[nome_u] = tempo
            tempo += 1
            filhos[nome_u] = 0

            for v in self.__lista_de_adjacentes[nome_u]:
                nome_v = v.obter_nome()
                if nome_v not in visitados:
                    pais[nome_v] = nome_u
                    filhos[nome_u] += 1
                    dfs_articulacao(v)

                    tempos_low[nome_u] = min(tempos_low[nome_u], tempos_low[nome_v])

                    if pais[nome_u] is None and filhos[nome_u] > 1:  # Raiz com mais de um filho
                        articulacoes.add(u)

                    if pais[nome_u] is not None and tempos_low[nome_v] >= tempos_descoberta[nome_u]:  # Caso geral
                        articulacoes.add(u)

                elif nome_v != pais[nome_u]:  # Caso de retorno (v é um ancestral, mas não o pai de u)
                    tempos_low[nome_u] = min(tempos_low[nome_u], tempos_descoberta[nome_v])

        for vertice in self.__lista_de_vertices:
            nome_vertice = vertice.obter_nome()
            if nome_vertice not in visitados:
                dfs_articulacao(vertice)

        return articulacoes

    def euleriano(self):

        if self.__direcionado:
            
            conectividade = self.identificar_conectividade()

            if not conectividade:
                print("Grafo não é conexo. Não é euleriano.")
                return False

            for v in self.__lista_de_vertices:
                in_degree = len(self.__predecessores.get(v.obter_nome(), []))
                out_degree = len(self.__sucessores.get(v.obter_nome(), []))

                if in_degree != out_degree:
                    return False

            print("O grafo é euleriano!")
            return True
        
        elif not self.__direcionado:

            conectividade_nao_direcionado = self.identificar_conectividade()

            if not conectividade_nao_direcionado:
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
        if not self.euleriano():
            print("O grafo não é euleriano.")
            return None

        caminho = []

        grafo_copia = self.copia()

        vertice_inicial = None
        for v in grafo_copia.obter_vertices():
            if len(grafo_copia.obter_arestas_ajacentes_ao_vertice(v)) % 2 != 0:
                vertice_inicial = v
                break
            
        if vertice_inicial is None:
            vertice_inicial = grafo_copia.obter_vertices()[0]

        def fleury(v):
            for aresta in grafo_copia.obter_arestas_ajacentes_ao_vertice(v):

                adj = aresta.obter_vertice_B() if aresta.obter_vertice_A() == v else aresta.ob

                if self.is_conexo_removendo(v, adj):
                    caminho.append((v.obter_nome(), adj))
                    grafo_copia.remover_aresta(v, adj)
                    fleury(adj)
                    return

                caminho.append((v.obter_nome(), adj))
                grafo_copia.remover_aresta(v, adj)
                fleury(adj)
                return

        fleury(vertice_inicial)

        return caminho

    def is_conexo_removendo(self, v1, v2):
        grafo_copia = self.copia()

        grafo_copia.remover_aresta(v1, v2)

        return grafo_copia.identificar_conectividade()

    def exportar_para_gexf(self, nome_arquivo: str):

        gexf = ET.Element("gexf", xmlns="http://www.gexf.net/1.2draft", version="1.2")
        graph = ET.SubElement(gexf, "graph", defaultedobterype="directed" if self.__direcionado else "undirected", mode="static")

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
            print(edge_attribs)
            if aresta.e_direcionada():
                edge_attribs["type"] = "directed"
            ET.SubElement(edges, "edge", **edge_attribs)

        tree = ET.ElementTree(gexf)
        tree.write(nome_arquivo, encoding="utf-8", xml_declaration=True)

    @staticmethod
    def importar_de_gexf(nome_arquivo: str) -> 'Grafo':
        try:
            grafo = Grafo()

            tree = ET.parse(nome_arquivo)
            root = tree.obterroot()

            namespace = {"gexf": "http://www.gexf.net/1.2draft"}

            graph = root.find("gexf:graph", namespace)
            direcionado = graph.obter("defaultedobterype", "undirected") == "directed"
            grafo.__direcionado = direcionado

            nodes = graph.find("gexf:nodes", namespace)
            for node in nodes.findall("gexf:node", namespace):
                id_vertice = node.obter("id")
                rotulacao = node.obter("label", id_vertice)
                grafo.adicionar_vertice(rotulacao)

            edges = graph.find("gexf:edges", namespace)
            for edge in edges.findall("gexf:edge", namespace):
                source_id = edge.obter("source")
                target_id = edge.obter("target")
                ponderacao = float(edge.obter("weight", 1))
                rotulacao = edge.obter("label", "")
                direcionada = direcionado or edge.obter("type", "undirected") == "directed"

                grafo.adicionar_aresta(source_id, target_id, ponderacao, rotulacao, direcionada)

            print(f"Grafo importado com sucesso de {nome_arquivo}")
            return grafo

        except Exception as e:
            print(f"Erro ao importar o grafo: {e}")
            return None