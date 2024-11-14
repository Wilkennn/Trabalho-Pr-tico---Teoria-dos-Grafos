from Grafo import Grafo
from Aresta import Aresta
from Vertice import Vertice


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

        if any(str(vertice) == vertice_nome for vertice in grafo.getVertices()):
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

        if grafo.addVertice(vertice_nome, ponderacao):
            count += 1

    return True

def remover_vertice(grafo):
    nome_vertice = input("Qual vértice você deseja excluir do seu grafo? ").strip()

    while not nome_vertice or not nome_vertice.isalnum():
        print("O nome do vértice não pode ser vazio e deve ser alfanumérico.")
        nome_vertice = input("Qual vértice você deseja excluir do seu grafo? ").strip()

    if not any(str(vertice) == nome_vertice for vertice in grafo.getVertices()):
        print(f"O vértice '{nome_vertice}' não existe no grafo.")
        return True

    confirmar = input(f"Tem certeza que deseja remover o vértice '{nome_vertice}'? (S/N): ").strip().lower()
    if confirmar != 's':
        print("Remoção cancelada.")
        return True

    grafo.removeVertice(nome_vertice)
    print(f"Vértice '{nome_vertice}' removido com sucesso.")
    return True

def imprimir(grafo):
    vertices = grafo.getVertices()
    Nvertices = grafo.getNumVertices()
    arestas = grafo.getAllArestas()
    adjascentes = grafo.getAdj()
    sucessores = grafo.getSucessores()
    predecessores = grafo.getPredecessores()

    if vertices:
        print(f"Lista de vértices no grafo com {Nvertices} encontrados (nome, ponderação):", vertices)
        
    else:
        print("O grafo não possui vértices.")

    for aresta in arestas:
        print(aresta)     

    print(f"{adjascentes}")
    print(f"{predecessores}")
    print(f"{sucessores}")

    return True    

def adicionar_aresta(grafo):
    if grafo.getNumVertices() < 2:
        print("É necessário ter pelo menos dois vértices para adicionar uma aresta.")
        return False
    
    verticeA = input("Digite o nome do primeiro vértice: ").strip()
    verticeB = input("Digite o nome do segundo vértice: ").strip()

    if not any(verticeA == v.getNome() for v in grafo.getVertices()) or not any(verticeB == v.getNome() for v in grafo.getVertices()):
        print("Um ou ambos os vértices não existem no grafo.")
        return False  # Voltar para evitar adicionar a aresta

    tipo_aresta = input("A aresta será direcionada? (S/N): ").strip().lower()

    if tipo_aresta == 's':
        direcionada = True
    else:
        direcionada = False

    ponderacao = input("Digite a ponderação da aresta (opcional, digite 0 para nenhuma): ").strip()

    try:
        ponderacao = int(ponderacao)
    except ValueError:
        print("Valor inválido para ponderação. Considerando ponderação 0.")
        ponderacao = 0

    rotulacao = input("Digite o rótulo da aresta (opcional): ").strip()

    grafo.addAresta(verticeA, verticeB, ponderacao, rotulacao, direcionada)
    return True

def remover_arestas(grafo):
    verticeA = input("Digite o nome do primeiro vértice da aresta a ser removida: ").strip()
    verticeB = input("Digite o nome do segundo vértice da aresta a ser removida: ").strip()

    if not any(verticeA == v.getNome() for v in grafo.getVertices()) or not any(verticeB == v.getNome() for v in grafo.getVertices()):
        print("Um ou ambos os vértices não existem no grafo.")
        return True

    aresta_existente = False
    for aresta in grafo.getAllArestas():
        if (aresta.getVerticeA().getNome() == verticeA and aresta.getVerticeB().getNome() == verticeB) or (aresta.getVerticeA().getNome() == verticeB and aresta.getVerticeB().getNome() == verticeA):
            aresta_existente = True
            break


    if not aresta_existente:
        print(f"A aresta entre '{verticeA}' e '{verticeB}' não existe.")
        return True

    grafo.removeAresta(verticeA, verticeB)  
    print(f"Aresta entre '{verticeA}' e '{verticeB}' removida com sucesso.")
    return True

def checarAdjV(grafo):

    verticeA = input("Digite o nome do primeiro vértice: ").strip()
    verticeB = input("Digite o nome do segundo vértice: ").strip()

    grafo.areAdjV(verticeA, verticeB)

    return True

def checarAdjA(grafo): 
    # Recebe os vértices para a primeira aresta
    verticeA1 = input("Digite o nome do primeiro vértice da primeira aresta: ").strip()
    verticeB1 = input("Digite o nome do segundo vértice da primeira aresta: ").strip()

    # Recebe os vértices para a segunda aresta
    verticeA2 = input("Digite o nome do primeiro vértice da segunda aresta: ").strip()
    verticeB2 = input("Digite o nome do segundo vértice da segunda aresta: ").strip()

    # Busca os objetos de vértice correspondentes aos nomes fornecidos
    vA1 = next((v for v in grafo.getVertices() if v.getNome() == verticeA1), None)
    vB1 = next((v for v in grafo.getVertices() if v.getNome() == verticeB1), None)
    vA2 = next((v for v in grafo.getVertices() if v.getNome() == verticeA2), None)
    vB2 = next((v for v in grafo.getVertices() if v.getNome() == verticeB2), None)

    # Verifica se os vértices existem no grafo
    if not all([vA1, vB1, vA2, vB2]):
        print("Um ou mais vértices não foram encontrados.")
        return False

    # Cria as arestas (supondo ponderação e rotulagem como parâmetros para exemplo)
    aresta1 = Aresta(vA1, vB1, ponderacao=0, rotulacao="Aresta1", direcionada=False)
    aresta2 = Aresta(vA2, vB2, ponderacao=0, rotulacao="Aresta2", direcionada=False)

    # Checa a adjacência entre as arestas
    grafo.areAdjA(aresta1, aresta2)

    return True

def searchAresta(grafo):

    vA = input("Digite o nome do primeiro vértice da aresta: ").strip()
    vB = input("Digite o nome do segundo vértice da aresta: ").strip()    

    grafo.searchAresta(vA, vB)

    return True

def numVerAr(grafo):

    vertices = grafo.getNumVertices()
    arestas = grafo.getNumArestas()

    print(f"Número de vértices: {vertices}")
    print(f"Número de arestas: {arestas}")

    return True

def iscompleto(grafo):

    grafo.iscompleto()
    
    return True

def isempty(grafo):

    vazio = grafo.isEmpty()
    
    if vazio:
        print("Grafo está vazio")
    else:
        print("Grafo não está vazio")
    
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
        '11': lambda: imprimir(grafo)    
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
        opcao = input(("\033[1;31m>\033[0m " ))
        print("")
        
        if opcao in opcoes:
            if not opcoes[opcao]():  
                break
        else:
            print("Opção inválida. Por favor, tente outra opção.")


if __name__ == "__main__":
    main()