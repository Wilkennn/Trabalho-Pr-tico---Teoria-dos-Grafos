from graph_library.Grafo import Grafo
from graph_library.Aresta import Aresta
from graph_library.Vertice import Vertice


def opcao_sair():
    print("\033[1;31mSaindo do programa... Até logo!\033[0m")
    exit()

def adicionar_vertices(grafo):
    while True:
        try:
            qtdvertices = int(input("Quantos vértices você deseja no seu grafo? "))
            if qtdvertices <= 0:
                print("A quantidade de vértices deve ser um número positivo.")
                continue
            break
        except ValueError:
            print("Por favor, insira um número válido.")

    count = 0

    while count < qtdvertices:
        vertice_nome = input(f"Digite o nome do {count + 1}° vértice: ").strip()

        while not vertice_nome or not vertice_nome.isalnum():
            print("O nome do vértice não pode ser vazio e deve ser alfanumérico.")
            vertice_nome = input(f"Digite o nome do {count + 1}° vértice: ").strip()

        if any(str(vertice) == vertice_nome for vertice in grafo.obter_vertices()):
            print(f"O vértice '{vertice_nome}' já existe no grafo. Tente outro nome.")
            continue

        hasPonderacao = input(f"Deseja definir ponderação ao {count + 1}° vértice? (S/N): ").strip().lower()

        if hasPonderacao == 's':
            while True:
                try:
                    ponderacao = int(input(f"Digite a ponderação do {count + 1}° vértice: "))
                    if ponderacao < 0:
                        print("A ponderação não pode ser negativa. Tente novamente.")
                        continue
                    break
                except ValueError:
                    print("Por favor, insira um número válido para a ponderação.")
        else:
            ponderacao = 0

        if grafo.adicionar_vertice(vertice_nome, ponderacao):
            count += 1
        
            if ponderacao != 0:
                print(f"Vértice '{vertice_nome}' com ponderação {ponderacao} adicionado ao grafo.")
            else:
                print(f"Vértice '{vertice_nome}' adicionado ao grafo.")

    return True

def remover_vertice(grafo):
    nome_vertice = input("Qual vértice você deseja excluir do seu grafo? ").strip()

    while not nome_vertice or not nome_vertice.isalnum():
        print("O nome do vértice não pode ser vazio e deve ser alfanumérico.")
        nome_vertice = input("Qual vértice você deseja excluir do seu grafo? ").strip()

    if not any(str(vertice) == nome_vertice for vertice in grafo.obter_vertices()):
        print(f"O vértice '{nome_vertice}' não existe no grafo.")
        return True

    confirmar = input(f"Tem certeza que deseja remover o vértice '{nome_vertice}'? (S/N): ").strip().lower()
    if confirmar != 's':
        print("Remoção cancelada.")
        return True

    if grafo.remover_vertice(nome_vertice):
        print(f"Vértice '{nome_vertice}' removido com sucesso.")
    else:
        print(f"Falha ao tentar remover o vértice '{nome_vertice}'.")

    return True

def imprimir(grafo):
    vertices = grafo.obter_vertices()
    Nvertices = grafo.obter_numero_vertices()
    arestas = grafo.obter_todas_arestas()
    adjascentes = grafo.obter_adj()
    sucessores = grafo.obter_sucessores()
    predecessores = grafo.obter_predecessores()

    if vertices:
        print(f"Lista de vértices no grafo com {Nvertices} encontrados (nome, ponderação):", vertices)
        
    else:
        print("O grafo não possui vértices.")

    for aresta in arestas:
        print(aresta)

    print(f"Lista de adjacentes: {adjascentes}")
    print(f"Lista de predecessores: {predecessores}")
    print(f"Lista de sucessores: {sucessores}")

    return True

def adicionar_aresta(grafo):
    if grafo.obter_numero_vertices() < 2:
        print("É necessário ter pelo menos dois vértices para adicionar uma aresta.")
        return True

    while True:
        try:
            qtd_arestas = int(input("Quantas arestas você deseja no seu grafo? "))
            if qtd_arestas <= 0:
                print("A quantidade de arestas deve ser um número positivo.")
                continue
            break
        except ValueError:
            print("Por favor, insira um número válido.")

    count = 0

    while count < qtd_arestas:
        print(f"Preencha as informações da {count + 1}° aresta:")
        
        while True:
            verticeA = input("Digite o nome do primeiro vértice: ").strip()
            verticeB = input("Digite o nome do segundo vértice: ").strip()

            if any(verticeA == v.obter_nome() for v in grafo.obter_vertices()) and \
               any(verticeB == v.obter_nome() for v in grafo.obter_vertices()):
                break  

            print("Um ou ambos os vértices não existem no grafo. Tente novamente.")

        tipo_aresta = input("A aresta será direcionada? (S/N): ").strip().lower()

        direcionada = tipo_aresta == 's'

        ponderacao = input("Digite a ponderação da aresta (opcional, digite 0 para nenhuma): ").strip()

        try:
            ponderacao = int(ponderacao)
        except ValueError:
            print("Valor inválido para ponderação. Considerando ponderação 0.")
            ponderacao = 0

        rotulacao = input("Digite o rótulo da aresta (opcional): ").strip()

        if grafo.adicionar_aresta(verticeA, verticeB, ponderacao, rotulacao, direcionada):
            count += 1
        else:
            print("Falha ao adicionar a aresta. Tente novamente.")

    return True

def remover_arestas(grafo):
    verticeA = input("Digite o nome do primeiro vértice da aresta a ser removida: ").strip()
    verticeB = input("Digite o nome do segundo vértice da aresta a ser removida: ").strip()

    if not any(verticeA == v.obter_nome() for v in grafo.obter_vertices()) or not any(verticeB == v.obter_nome() for v in grafo.obter_vertices()):
        print("Um ou ambos os vértices não existem no grafo.")
        return True

    aresta_existente = False
    for aresta in grafo.obter_todas_arestas():
        if (aresta.obter_vertice_A().obter_nome() == verticeA and aresta.obter_vertice_B().obter_nome() == verticeB) or (aresta.obter_vertice_A().obter_nome() == verticeB and aresta.obter_vertice_B().obter_nome() == verticeA):
            aresta_existente = True
            break

    if not aresta_existente:
        print(f"A aresta entre '{verticeA}' e '{verticeB}' não existe.")
        return True

    grafo.remover_aresta(verticeA, verticeB)  
    print(f"Aresta entre '{verticeA}' e '{verticeB}' removida com sucesso.")
    return True

def checarAdjV(grafo):
    verticeA = input("Digite o nome do primeiro vértice: ").strip()
    verticeB = input("Digite o nome do segundo vértice: ").strip()

    sao_adjacentes = grafo.sao_adj_v(verticeA, verticeB)
    
    if sao_adjacentes:
        print(f"Os vértices '{verticeA}' e '{verticeB}' são adjacentes.")
    else:
        print(f"'{verticeA}' e '{verticeB}' NÃO são adjacentes.")

    return True

def checarAdjA(grafo):
    verticeA1 = input("Digite o nome do primeiro vértice da primeira aresta: ").strip()
    verticeB1 = input("Digite o nome do segundo vértice da primeira aresta: ").strip()

    verticeA2 = input("Digite o nome do primeiro vértice da segunda aresta: ").strip()
    verticeB2 = input("Digite o nome do segundo vértice da segunda aresta: ").strip()

    vA1 = next((v for v in grafo.obter_vertices() if v.obter_nome() == verticeA1), None)
    vB1 = next((v for v in grafo.obter_vertices() if v.obter_nome() == verticeB1), None)
    vA2 = next((v for v in grafo.obter_vertices() if v.obter_nome() == verticeA2), None)
    vB2 = next((v for v in grafo.obter_vertices() if v.obter_nome() == verticeB2), None)

    if not all([vA1, vB1, vA2, vB2]):
        print("Um ou mais vértices não foram encontrados.")
        return False

    aresta1 = Aresta(vA1, vB1, ponderacao=0, rotulacao="Aresta1", direcionada=False)
    aresta2 = Aresta(vA2, vB2, ponderacao=0, rotulacao="Aresta2", direcionada=False)

    sao_adjacentes = grafo.sao_adj_a(aresta1, aresta2)

    if sao_adjacentes:
        print(f"As arestas com vértices ('{verticeA1}', '{verticeB1}') e ('{verticeA2}', '{verticeB2}') são adjacentes.")
    else:
        print(f"As arestas com vértices ('{verticeA1}', '{verticeB1}') e ('{verticeA2}', '{verticeB2}') NÃO são adjacentes.")
    
    return True

def searchAresta(grafo):
    vA = input("Digite o nome do primeiro vértice da aresta: ").strip()
    vB = input("Digite o nome do segundo vértice da aresta: ").strip()

    existe = grafo.buscar_aresta(vA, vB)

    if existe:
        print(f"A aresta entre '{vA}' e '{vB}' foi encontrada.")
    else:
        print(f"A aresta entre '{vA}' e '{vB}' não existe.")
    
    return True

def numVerAr(grafo):

    vertices = grafo.obter_numero_vertices()
    arestas = grafo.obter_numero_arestas()

    print(f"Número de vértices: {vertices}")
    print(f"Número de arestas: {arestas}")

    return True

def iscompleto(grafo):

    grafo.e_completo()
    
    return True

def isempty(grafo):

    vazio = grafo.esta_vazio()
    
    if vazio:
        print("Grafo está vazio")
    else:
        print("Grafo não está vazio")
    
    return True

def matriz_incidencia(grafo):
    
    vazio = grafo.esta_vazio();

    if vazio:
        print("O grafo está vazio, adicione antes de exibir a matriz de incidencia!")
        return True
    
    grafo.exibir_matriz_incidencia()
    return True
    
def matriz_adjacencia(grafo):
    vazio = grafo.esta_vazio();

    if vazio:
        print("O grafo está vazio, adicione antes de exibir a matriz de adjacência!")
        return True
    
    grafo.exibir_matriz_adjacencia()
    return True

def lista_adjacencia(grafo):

    vazio = grafo.esta_vazio();

    if vazio:
        print("O grafo está vazio, adicione antes de exibir a Lista de adjacência!")
        return True
    
    grafo.exibir_lista_adjacencia()
    return True

def busca_profundidade(grafo):
    # Verifica se o grafo está vazio
    if grafo.esta_vazio():
        print("O grafo está vazio, adicione antes de exibir a busca em profundidade!")
        return True
    
    vertice_raiz_nome = input("Digite o nome do primeiro vértice: ").strip()

    vertice_raiz = None
    for v in grafo.obter_vertices():
        if v.obter_nome() == vertice_raiz_nome:
            vertice_raiz = v
            break

    if vertice_raiz is None:
        print("O vértice não existe no grafo.")
        return True

    
    visitados = set()
  
    grafo.busca_em_profundidade(visitados, start=vertice_raiz)

    grafo.exibir_resultado_busca_em_profundidade()
    
    return True

def identificarPontes_Articu(grafo):
    pontes = grafo.identificar_pontes_tarjan()
    arti = grafo.identificar_articulacoes()
    p2 = grafo.identificar_pontes_naive()
    grafo.euleriano()

    print("Pontes Tarjan: ", pontes)
    print("Pontes Naive : ", p2)
    print("Articulações: ", arti)

    return True

def kosaraju(grafo):
    
    count = grafo.algoritmo_de_kosaraju()
    print("Quantidade de componentes fortemente conexos:" , count)
    return True

def verificar_conectividade(grafo):
    
    conectividade = grafo.identificar_conectividade()
    print(conectividade)
    return True

def gerar_aleatorio(grafo):
    grafo = Grafo.gerar_grafo_aleatorio()
    
    return True

def main():
    grafo = Grafo()

    opcoes = {
        '0': opcao_sair,
        '1': lambda: adicionar_vertices(grafo),
        '2': lambda: remover_vertice(grafo),
        '3': lambda: adicionar_aresta(grafo),
        '4': lambda: remover_arestas(grafo),
        '5': lambda: checarAdjV(grafo),
        '6': lambda: checarAdjA(grafo),
        '7': lambda: searchAresta(grafo),
        '8': lambda: numVerAr(grafo),
        '9': lambda: isempty(grafo),
        '10': lambda: iscompleto(grafo),
        '11' : lambda: imprimir(grafo),
        '12' :lambda: matriz_incidencia(grafo),
        '13' :lambda: matriz_adjacencia(grafo),
        '14' :lambda: lista_adjacencia(grafo),
        '15' :lambda: busca_profundidade(grafo),
        '16' :lambda: identificarPontes_Articu(grafo),
        '17' :lambda: kosaraju(grafo),
        '18' :lambda: verificar_conectividade(grafo),
        '19' :lambda: gerar_aleatorio(grafo)
    }

    while True:
        print("")
        print("\033[1;31m======= Programa de Grafos =======\033[0m")
        print("Escolha uma opção:")
        print("0 - Sair")
        print("1 - Adicionar vértices")
        print("2 - Remover vértice")
        print("3 - Adicionar Aresta")
        print("4 - Remover Aresta")
        print("5 - Chegar Adjacência entre Vértices")
        print("6 - Chegar Adjacência entre Arestas")
        print("7 - Verificar existência de Aresta")
        print("8 - Contagem de vértices e arestas")
        print("9 - Verificar se o grafo está vazio")
        print("10 - Verificar se o grafo está completo")
        print("11 - Imprimir lista de vértices")
        print("12 - Gerar Matriz Incidência")
        print("13 - Gerar Matriz Adjacência")
        print("14 - Gerar Lista Adjacência")
        print("15 - Executar Busca em Profundidade")
        print("16 - Identificar Pontes e Articulações")
        print("17 - Visualizar quantidade de componentes fortemente conexos")
        print("18 - Verificar conectividade")
        print("19 - Gerar grafo aleatório")
        opcao = input(("\033[1;31m>\033[0m " ))
        print("")
        
        if opcao in opcoes:
            if not opcoes[opcao]():
                break
        else:
            print("Opção inválida. Por favor, tente outra opção.")


if __name__ == "__main__":
    main()