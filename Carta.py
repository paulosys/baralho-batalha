class Carta:

    def __init__(self, numero, naipe, cor, peso):
        self.__numero = numero
        self.__naipe = naipe
        self.peso = peso

    @property
    def naipe(self):
        return self.__naipe

    @property
    def numero(self):
        return self.__numero
    
   
    
    def __str__(self): # todas as informacoes da carta
        return f'{self.__numero} de {self.__naipe}'