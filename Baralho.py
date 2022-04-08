# Baralho = coleçao de cartas (lista de cartas)
from Carta import Carta
from PilhaEncadeada import Pilha
from random import shuffle

class BaralhoException(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class Baralho:
    def __init__(self):
        self.__baralhoPilha = Pilha()
        self.__baralho = list()
        naipe = ["Ouro","Espada","Paus","Copas"]
        cor =   ["vermelho","preto", "preto","vermelho"]
        numeracao = ["As","2","3","4","5","6","7","8","9","10","Valete","Dama","Rei"]

        for idx in range(len(naipe)):
            for id in numeracao:
                self.__baralho.append(Carta(id, naipe[idx], cor[idx]))
        
        self.embaralhar()
        
        for carta in self.__baralho:
            self.__baralhoPilha.empilhar(carta)
    
    def __len__(self):
        return len(self.__baralho)

    def temCarta(self):
        if len(self.__baralho) > 0:
            return True
        else:
            return False
    
    def retirarCarta(self)->Carta:
        try:
            return self.__baralho.pop()
        except IndexError :
            raise BaralhoException('O __baralho está vazio. Não há cartas para retirar')
            
    def embaralhar(self):
        shuffle(self.__baralho)
    
    def dividirBaralho(self):
        parteBaralho = []
        for carta in range(26):
            try:
                parteBaralho.append(self.__baralhoPilha.desempilhar())
            except IndexError:
                raise BaralhoException('O __baralho está vazio. Não há cartas para dividir')
        return parteBaralho
                
    def entregarBaralho(self):
        return self.__baralhoPilha

    def __str__(self):
        saida = ''
        for carta in self.__baralho:
            saida += carta.__str__() + '\n' 
        return saida