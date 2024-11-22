from graph_library.Vertice import Vertice

class Aresta:
    def __init__(self, verticeA, verticeB, ponderacao, rotulacao, direcionada=False):
        self.__verticeA = verticeA
        self.__verticeB = verticeB
        self.__ponderacao = ponderacao
        self.__rotulacao = rotulacao
        self.__direcionada = direcionada

    def obter_vertice_A(self):
        return self.__verticeA
    
    def obter_vertice_B(self):
        return self.__verticeB
    
    def obter_rotulacao(self):
        return self.__rotulacao
    
    def obter_ponderacao(self):
        return self.__ponderacao
    
    def e_direcionada(self):
        return self.__direcionada

    def __str__(self):
        verticeA_str = str(self.__verticeA)
        verticeB_str = str(self.__verticeB)
        rotulacao_str = str(self.__rotulacao)

        if self.__direcionada:
            return f"{verticeA_str} -> {verticeB_str} (Ponderação: {self.__ponderacao}, Rótulo: {rotulacao_str})"
        else:
            return f"{min(verticeA_str, verticeB_str)} - {max(verticeA_str, verticeB_str)} (Ponderação: {self.__ponderacao}, Rótulo: {rotulacao_str})"

    def __lt__(self, other):
        if isinstance(other, Vertice):
            return self.__nome < other.getNome()
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Aresta):
            if self.__direcionada or other.__direcionada:
                return (self.__verticeA == other.__verticeA and self.__verticeB == other.__verticeB and
                        self.__direcionada == other.__direcionada)
            else:
                return {self.__verticeA, self.__verticeB} == {other.__verticeA, other.__verticeB}
        return False
