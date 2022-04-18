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
        cor =   ["vermelho","azul", "azul","vermelho"]
        numeracao = ["As","2","3","4","5","6","7","8","9","10","Valete","Dama","Rei"]
        peso =  [1,2,3,4,5,6,7,8,9,10,11,12,13]

        for idx in range(len(naipe)):
            for num in range(len(numeracao)):
                self.__baralho.append(Carta(numeracao[num], naipe[idx], cor[idx], peso[num]))
    
    def __len__(self) -> int:
        return len(self.__baralho)

    def temCarta(self) -> bool:
        return True if len(self.__baralho) > 0 else False
    
    def retirarCarta(self) -> Carta:
        try:
            return self.__baralho.pop()
        except IndexError :
            raise BaralhoException('O __baralho está vazio. Não há cartas para retirar')
                
    def montar(self) -> Pilha:
        print("======= Preparando Baralho =======\n")
        self.embaralhar()
        for carta in self.__baralho:
            self.__baralhoPilha.empilhar(carta)
        print("======= Baralho Montado Com Sucesso! =======\n")
        return self.__baralhoPilha
    
    def embaralhar(self):
        porcentagem = 0
        input("Pressione ENTER para embaralhar as cartas")
        print()
        for i in range(5):
            print(f"Embaralhando as Cartas: {porcentagem}%")
            porcentagem += 25
            sleep(0.5)
        shuffle(self.__baralho) ## Método do random para embaralhar uma lista
        print("\n======= Cartas Embaralhadas Com Sucesso! =======\n")
        
    def dividirBaralho(self):
        parteBaralho = []
        for carta in range(26):
            try:
                parteBaralho.append(self.__baralhoPilha.desempilhar())
            except IndexError:
                raise BaralhoException('O baralho está vazio.')
        return parteBaralho

    def __str__(self) -> str:
        saida = ''
        for carta in self.__baralho:
            saida += carta.__str__() + '\n' 
        return saida