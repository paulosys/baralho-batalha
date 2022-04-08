from PilhaEncadeada import Pilha

class JogadorException(Exception):
    def __init__(self,mensagem,metodo=''):
        super().__init__(mensagem)
        self.metodo = metodo

class Jogador:
    def __init__(self, nome) -> None:
        self.__nome = nome
        self.__deck = Pilha()
        
    def get_nome(self) -> str:
        return self.__nome
    
    def set_deck(self, carta) -> None:
        self.__deck.empilhar(carta)
        
    def get_deck(self) -> Pilha:
        return self.__deck.imprimir()
        
