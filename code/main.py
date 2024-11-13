from Grafo import Grafo
from Vertice import Vertice

def opcao_sair():
    print("Encerrando o programa.")
    return False

def adicionar_vertices(grafo):
    vertices = input("Quantos vértices você deseja no seu grafo? ")
    count = 0
    
    while count < int(vertices):
        vertice_nome = input(f"Digite o nome do {count + 1}° vértice: ")
        
        hasPonderacao = input(f"Deseja definir ponderação ao {count + 1}° vértice? (S/N): ").strip().lower()
        
        if hasPonderacao == 'S' or hasPonderacao == 's':  
            ponderacao = input(f"Digite a ponderação do {count + 1}° vértice: ")
        else:
            ponderacao = 0

        grafo.addVertice(vertice_nome, ponderacao)  
        count += 1    

    return True

def imprimir(grafo):
    vertices = grafo.get_vertices()
    if vertices:
        print("Lista de vértices no grafo:", vertices)
    else:
        print("O grafo não possui vértices.")

def main():
    grafo = Grafo()

    opcoes = {
        '0': opcao_sair,
        '1': lambda: adicionar_vertices(grafo),
        '2': lambda: imprimir(grafo),  
    }

    while True:
        print("======= Programa de Grafos =======")
        print("Escolha uma opção:")
        print("0 - Sair")
        print("1 - Definir número de vértices")
        print("2 - Imprimir lista de vértices")
        print("3 - Adicionar Arestas")
        opcao = input("> ")
        
        if opcao in opcoes:
            if not opcoes[opcao]():  
                break
        else:
            print("Opção inválida. Por favor, tente outra opção.")

if __name__ == "__main__":
    main()
