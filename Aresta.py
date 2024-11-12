class Aresta:
    def __init__(self, verticeA, verticeB, ponderacao, rotulacao, direcionado=False):
        self.__verticeA = verticeA
        self.__verticeB = verticeB
        self.__rotulacao  = rotulacao
        self.__ponderacao = ponderacao
        self.__direcionado = direcionado

    def getVerticeA(self):
        return self.__verticeA

    def getVerticeB(self):
        return self.__verticeB
    
    def getRotulacao(self):
        return self.__rotulacao
    
    def getPonderacao(self):
        return self.__ponderacao

    def __str__(self):
        if self.__direcionado:
            return f"{self.__verticeA} -> {self.__verticeB}"
        else:
            return f"{min(self.__verticeA, self.__verticeB)} - {max(self.__verticeA, self.__verticeB)}"

    def __eq__(self, other):
        if isinstance(other, Aresta):
            if self.__direcionado:
                return (self.__verticeA == other.__verticeA and self.__verticeB == other.__verticeB)
            else:
                # Para grafos não direcionados, considera (A, B) igual a (B, A)
                return {self.__verticeA, self.__verticeB} == {other.__verticeA, other.__verticeB}
        return False
