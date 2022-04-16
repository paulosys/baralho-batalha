from Baralho import *
from time import sleep
from Jogador import Jogador

class Batalha:
    def __init__(self) -> None:
        self.__baralho = Baralho()
        self.__j1 = None
        self.__j2 = None
        self.__rodada = 1
        self.__cartas_acumuladas = []
        self.__vencedor_rodada = None
        self.__vencedor_jogo = None
    
    def set_jogadores(self,j1: Jogador, j2: Jogador) -> None:
        self.__j1 = j1
        print(f'Jogador 1: {j1.get_nome()}')
        self.__j2 = j2
        print(f'Jogador 2: {j2.get_nome()}')
        
    def iniciar_jogo(self) -> None:
        self.__baralho = self.__baralho.montar()
        self.entregar_cartas()
        while (not self.__vencedor_jogo) and (self.__rodada <= 10):
            self.jogar()
            
        self.fim_jogo()
            
    def fim_jogo(self):
        
        if(self.__vencedor_jogo is None):
            if self.__j1.get_tamanho_deck() > self.__j2.get_tamanho_deck():
                self.__vencedor_jogo = self.__j1
            else:
                self.__vencedor_jogo = self.__j2
                
        print(f'O vencedor do jogo foi {self.__vencedor_jogo.get_nome()}!')
        
        decisao = input("Jogo encerrado! Deseja jogar novamente? (S/N)").upper()
        
        if decisao == 'S':
            self.__rodada = 1
            self.__cartas_acumuladas = []
            self.__vencedor_rodada = None
            self.__vencedor_jogo = None
            self.__baralho.limpar_pilha()
            self.__baralho = Baralho()
            self.__j1.limpar_deck()
            self.__j2.limpar_deck()
            
            self.__j1.mostrar_cartas_embaixo()
            self.__j2.mostrar_cartas_embaixo()
            
            self.iniciar_jogo()
        else:
            print("Obrigado por jogar!")
        
    def jogar(self):
        
        carta_jogador1 = self.__j1.jogar_carta()
        carta_jogador2 = self.__j2.jogar_carta()
        
        self.__cartas_acumuladas.append(carta_jogador1)
        self.__cartas_acumuladas.append(carta_jogador2)
        
        print(f'===== Rodada {self.__rodada} =====')
        print(f'({self.__j1.get_tamanho_deck()} cartas) {self.__j1.get_nome()}: ' ,end='    ')
        print(f'{carta_jogador1} x {carta_jogador2}', end='    ')
        print(f'({self.__j2.get_tamanho_deck()} cartas) {self.__j2.get_nome()}: ')
        
        self.__vencedor_rodada = self.comparar_cartas(carta_jogador1, carta_jogador2)
        
        print(f'{self.__vencedor_rodada.get_nome()} venceu a rodada!')
        
        for carta in self.__cartas_acumuladas:
            self.__vencedor_rodada.guardar_cartas(carta)
        
        print(f"O jogador {self.__vencedor_rodada.get_nome()} ganhou essas cartas: ", end=" ")
        for carta in self.__cartas_acumuladas:
            print(carta, end=" ") 
            
        self.__cartas_acumuladas.clear()

        self.__rodada += 1
        
        self.__vencedor_rodada = None
        input("Pressione ENTER para continuar")
        
    def comparar_cartas(self, carta1, carta2):
        if carta1.peso > carta2.peso:
            return self.__j1
        elif carta2.peso > carta1.peso:
            return self.__j2
        else:
            return self.rodada_empate()
            
    def rodada_empate(self):
        cont_rodada_empate = 1
        while self.__vencedor_rodada is None:
            print(f"Rodada empatada {cont_rodada_empate}!")
            input("Pressione ENTER para continuar")
            
            carta_jogador1 = self.__j1.jogar_carta()
            carta_jogador2 = self.__j2.jogar_carta()
            
            print(f'({self.__j1.get_tamanho_deck()} cartas) {self.__j1.get_nome()}: ' ,end='    ')
            print(f'{carta_jogador1} x {carta_jogador2}', end='    ')
            print(f'({self.__j2.get_tamanho_deck()} cartas) {self.__j2.get_nome()}: ')
            
            self.__cartas_acumuladas.append(carta_jogador1)
            self.__cartas_acumuladas.append(carta_jogador2)
            
            print(f"O jogador que desempatar ganhará essas cartas: ", end=" ")
            for carta in self.__cartas_acumuladas:
                print(carta)
            
            self.__vencedor_rodada = self.comparar_cartas(carta_jogador1, carta_jogador2)
        
        return self.__vencedor_rodada

    def entregar_cartas(self) -> None:
        jogadores = [self.__j1, self.__j2]
        for jogador in jogadores:
            for i in range(3):
                print(f"Entregando cartas para o jogador {jogador.get_nome()}...")
                #sleep(0.5)
            for j in range(26):
                try:
                    jogador.set_deck(self.__baralho.desempilhar())
                except IndexError:
                    raise BaralhoException('O __baralho está vazio. Não há cartas para dividir')
            print(f"Cartas entregues para o jogador {jogador.get_nome()}")