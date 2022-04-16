from PilhaEncadeada import Pilha

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
    
    def set_deck(self, carta) -> None:
        self.__deck.empilhar(carta)
        self.__tamanho_deck = self.__deck.tamanho()
    
    def guardar_cartas(self, carta):
        self.__deck.empilhar_embaixo(carta)
        self.__tamanho_deck += 1
        
    def mostrar_cartas_embaixo(self):
        self.__deck.imprimir_embaixo()
    
    def get_deck(self) -> Pilha:
        return self.__deck.imprimir()
    
    def get_tamanho_deck(self) -> int:
        return self.__tamanho_deck
    
    def jogar_carta(self):
        if self.get_cartas_jogaveis() > 0:
            self.__tamanho_deck -= 1
            return self.__deck.desempilhar()
        
        self.__deck.redefinir_pilha()
        
        if self.get_cartas_jogaveis() > 0:
            self.__tamanho_deck -= 1
            return self.__deck.desempilhar()
    
    def limpar_deck(self):
        self.__deck.limpar_pilha()
    
    def get_cartas_jogaveis(self):
        return self.__deck.tamanho()