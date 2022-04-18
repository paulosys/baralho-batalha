class Carta:

    def __init__(self, numero, naipe, cor, peso):
        self.__numero = numero
        self.__naipe = naipe
        self.__cor = cor
        self.peso = peso

    @property
    def naipe(self):
        return self.__naipe

    @property
    def numero(self):
        return self.__numero
    
    @property
    def cor(self):
        return self.__cor
    
    def __str__(self): # todas as informacoes da carta
        if self.__cor == "azul":
            return  "\033[1;31m" + f'{self.__numero} de {self.__naipe}' + "\033[0;0m"
        
        return  "\033[1;34m" + f'{self.__numero} de {self.__naipe}' + "\033[0;0m"