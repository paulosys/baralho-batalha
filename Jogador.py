from Carta import Carta
from PilhaEncadeada import *
class JogadorException(Exception):
    def __init__(self,mensagem,metodo=''):
        super().__init__(mensagem)
        self.metodo = metodo

class Jogador:
    def __init__(self, nome) -> None:
        self.__nome = nome
        self.__tamanho_deck = 0
        self.__deck = Pilha()
        
    def get_nome(self) -> str:
        return self.__nome
    
    def get_deck(self) -> Pilha:
        return self.__deck.imprimir()
    
    def set_deck(self, carta) -> None:
        self.__deck.empilhar(carta)
        self.__tamanho_deck = self.__deck.tamanho()
    
    def get_tamanho_deck(self) -> int:
        return self.__tamanho_deck
    
    def guardar_cartas(self, carta):
        self.__deck.enfileirar_embaixo(carta)
        self.__tamanho_deck += 1
    
    def jogar_carta(self) -> Carta:
        try:
            carta = self.__deck.desempilhar()
            self.__tamanho_deck -= 1
        except IndexError:
            raise JogadorException("O jogador não tem cartas para jogar!", "jogar_carta")
            
        return carta
    
    def imprimir_deck(self):
        self.__deck.imprimir()

    def limpar_deck(self):
        self.__deck.limpar_pilha()
        self.__tamanho_deck = 0