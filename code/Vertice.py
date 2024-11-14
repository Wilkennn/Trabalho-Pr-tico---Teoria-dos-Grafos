class Vertice:
    def __init__(self, rotulacao: str, ponderacao: int = 0):
        if not rotulacao:
            raise ValueError("A rotulacao do vértice não pode ser vazia.")
        if not isinstance(ponderacao, int):
            raise ValueError("A ponderação deve ser um número inteiro.")

        self.__rotulacao = rotulacao
        self.__ponderacao = ponderacao

    def getNome(self):
        return self.__rotulacao

    def getPonderacao(self):
        return self.__ponderacao

    def __str__(self):
        return self.__rotulacao

    def __repr__(self):
        return f"(Vertice: {self.__rotulacao}, Ponderacao:{self.__ponderacao})"

    def __eq__(self, other):
        if isinstance(other, Vertice):
            return self.__rotulacao == other.getNome()
        return False

    def __lt__(self, other):
        if isinstance(other, Vertice):
            return self.getNome() < other.getNome()
        return NotImplemented

    def __hash__(self):
        return hash(self.__rotulacao)
