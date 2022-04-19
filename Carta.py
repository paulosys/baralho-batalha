class Carta:

    def __init__(self, numero, naipe, cor, peso):
        self.__numero = numero
        self.__naipe = naipe
        self.__cor = cor
        self.__peso = peso

    @property
    def get_naipe(self):
        return self.__naipe

    @property
    def get_numero(self):
        return self.__numero
    
    @property
    def get_cor(self):
        return self.__cor
    
    @property
    def get_peso(self):
        return self.__peso
    
    def __str__(self): # todas as informacoes da carta
        if self.__cor == "azul":
            return  "\033[1;31m" + f'{self.get_numero} de {self.get_naipe}' + "\033[0;0m"
        return  "\033[1;34m" + f'{self.get_numero} de {self.get_naipe}' + "\033[0;0m"