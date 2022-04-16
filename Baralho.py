# Baralho = coleçao de cartas (lista de cartas)
from time import sleep
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
        peso =  [1,2,3,4,5,6,7,8,9,10,11,12,13]

        for idx in range(len(naipe)):
            for num in range(len(numeracao)):
                self.__baralho.append(Carta(numeracao[num], naipe[idx], cor[idx], peso[num]))
    
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
        porcentagem = 0
        for i in range(5):
            print(f"Embaralhando o baralho: {porcentagem}%")
            porcentagem += 25
            #sleep(0.5)
        shuffle(self.__baralho)
        print("O Baralho foi embaralhado com sucesso!")
    
    def dividirBaralho(self):
        parteBaralho = []
        for carta in range(26):
            try:
                parteBaralho.append(self.__baralhoPilha.desempilhar())
            except IndexError:
                raise BaralhoException('O __baralho está vazio. Não há cartas para dividir')
        return parteBaralho
                
    def montar(self) -> Pilha:
        self.embaralhar()
        
        for carta in self.__baralho:
            self.__baralhoPilha.empilhar(carta)
            
        print("Baralho montado com sucesso!")
        
        return self.__baralhoPilha

    def __str__(self):
        saida = ''
        for carta in self.__baralho:
            saida += carta.__str__() + '\n' 
        return saida