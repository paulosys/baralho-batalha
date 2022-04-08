from Baralho import *
from time import sleep

class Batalha:
    def __init__(self) -> None:
        self.__baralho = Baralho().entregarBaralho()
        self.__j1 = None
        self.__j2 = None
    
    def set_jogadores(self,j1, j2) -> None:
        self.__j1 = j1
        print(f'Jogador 1: {j1.get_nome()}')
        self.__j2 = j2
        print(f'Jogador 2: {j2.get_nome()}')
        
    def entregar_cartas(self) -> None:
        jogadores = [self.__j1, self.__j2]
        for jogador in jogadores:
            for i in range(3):
                print(f"Entregando cartas para o jogador {jogador.get_nome()}...")
                sleep(0.5)
            for j in range(26):
                try:
                    jogador.set_deck(self.__baralho.desempilhar())
                except IndexError:
                    raise BaralhoException('O __baralho está vazio. Não há cartas para dividir')
            print(f"Cartas entregues para o jogador {jogador.get_nome()}")