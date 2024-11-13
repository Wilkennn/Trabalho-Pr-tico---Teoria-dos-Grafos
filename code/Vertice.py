class Vertice:
    def __init__(self, rotulacao, ponderacao=None):
        self.__rotulacao  = rotulacao
        self.__ponderacao = ponderacao
    
    def getPonderacao(self):
        return self.__ponderacao

    def __str__(self):
        return self.__rotulacao

    def __repr__(self):
        return f"Vertice({self.__nome})"

    def __eq__(self, outro):
        if isinstance(outro, Vertice):
            return self.__nome == outro.getNome()
        return False

    def __hash__(self):
        # Permite que vértices sejam usados como chave em dicionários ou em conjuntos (sets)
        return hash(self.__nome)
