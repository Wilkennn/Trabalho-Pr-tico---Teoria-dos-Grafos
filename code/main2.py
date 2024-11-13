from Grafo import Grafo

def menu():
    print("Escolha uma opção:")
    print("1. Criar um novo grafo")
    print("2. Adicionar vértices")
    print("3. Adicionar arestas")
    print("4. Sair")
    escolha = input("Digite o número da opção desejada: ")
    return escolha


def criar_grafo():
    direcionado = input("O grafo é direcionado? (s/n): ").strip().lower() == 's'
    
    grafo = Grafo(isDirecionado=direcionado)
    print("Grafo criado com sucesso!")
    
    return grafo


def adicionar_vertices(grafo):
    vertices = input("Quantos vértices você deseja adicionar ao seu grafo? ")
    
    for count in range(int(vertices)):
        nome = input(f"Digite o nome do {count + 1}° vértice: ")
        grafo.add_vertice(nome)
    
    print("Vértices adicionados com sucesso!")
    return True


def adicionar_arestas(grafo):
    arestas = input("Quantas arestas você deseja adicionar ao seu grafo? ")

    for count in range(int(arestas)):
        origem = input(f"Digite o vértice de origem da {count + 1}° aresta: ")
        destino = input(f"Digite o vértice de destino da {count + 1}° aresta: ")

        peso = None
        if grafo.is_ponderado():
            peso = input(f"Digite o peso da {count + 1}° aresta: ")

        grafo.add_aresta(origem, destino, peso)
    
    print("Arestas adicionadas com sucesso!")
    return True


def main():
    grafo = None
    
    while True:
        escolha = menu()
        
        if escolha == "1":
            grafo = criar_grafo()
        
        elif escolha == "2":
            if grafo:
                adicionar_vertices(grafo)
            else:
                print("Crie um grafo primeiro!")
        
        elif escolha == "3":
            if grafo:
                adicionar_arestas(grafo)
            else:
                print("Crie um grafo primeiro!")
        
        elif escolha == "4":
            print("Saindo do programa...")
            break
        
        else:
            print("Opção inválida. Tente novamente.")


# Executa o programa
main()
