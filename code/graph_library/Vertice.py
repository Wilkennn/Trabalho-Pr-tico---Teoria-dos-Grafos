class Vertice:
    def __init__(self, rotulacao: str, ponderacao: int = 0):
        if not rotulacao:
            raise ValueError("A rotulacao do vértice não pode ser vazia.")
        if not isinstance(ponderacao, int):
            raise ValueError("A ponderação deve ser um número inteiro.")

        self.__rotulacao = rotulacao
        self.__ponderacao = ponderacao
        self.__tempo_termino = None;
        self.__tempo_descoberta = None;
        self.__vertice_pai = None;
    
    def definir_tempo_termino(self, tempo_termino: int) -> None:
        self.__tempo_termino = tempo_termino

    def obter_tempo_termino(self) -> int:
        return self.__tempo_termino
    
    def set_tempo_descoberta(self, tempo_descoberta: int) -> None:
        self.__tempo_descoberta = tempo_descoberta
    
    def obter__tempo_descoberta(self) -> int:
        return self.__tempo_descoberta
    
    def set_vertice_pai(self, vertice_pai: 'Vertice') -> None:
        self.__vertice_pai = vertice_pai

    def obter_vertice_pai(self) -> 'Vertice':
        return self.__vertice_pai
    
    def obter_nome(self):
        return self.__rotulacao

    def obter_ponderacao(self):
        return self.__ponderacao

    def __str__(self):
        return self.__rotulacao

    def __repr__(self):
        return f"(Vertice: {self.__rotulacao}, Ponderacao:{self.__ponderacao})"

    def __eq__(self, other):
        if isinstance(other, Vertice):
            return self.__rotulacao == other.obter_nome()
        return False

    def __lt__(self, other):
        if isinstance(other, Vertice):
            return self.obter_nome() < other.obter_nome()
        return NotImplemented

    def __hash__(self):
        return hash(self.__rotulacao)
