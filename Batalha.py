from Baralho import *
from time import sleep
from Jogador import Jogador

class Batalha:
    def __init__(self) -> None:
        self.__baralho = Baralho()
        self.__j1 = None
        self.__j2 = None
        self.__cont_rodadas = 1
        self.__limite_rodadas = 100
        self.__cartas_acumuladas = []
        self.__vencedor_rodada = None
        self.__vencedor_jogo = None
    
    def set_jogadores(self) -> None:
        print("\n======= Definindo Jogadores =======\n")
        self.__j1 = Jogador(input("Digite o nome do jogador 1: "))
        print(f'\nJogador 1 definido como: {self.__j1.get_nome()}\n')
        self.__j2 = Jogador(input("Digite o nome do jogador 2: "))
        print(f'\nJogador 2 definido como: {self.__j2.get_nome()}\n')
        print("======= Jogadores definidos com Sucesso! =======\n")
        
    def entregar_cartas(self) -> None:
        jogadores = [self.__j1, self.__j2]
        input("Pressione ENTER para Entregar as cartas.")
        print()
        for jogador in jogadores:
            for i in range(3):
                print(f"Entregando as cartas para {jogador.get_nome()}...\n")
                sleep(0.5)
            for j in range(26):
                try:
                    jogador.set_deck(self.__baralho.desempilhar())
                except IndexError:
                    raise BaralhoException('O baralho está vazio. Não há cartas para dividir')
            print(f"======= Cartas entregues para {jogador.get_nome()} ======= \n")
        
        decisao = input(f"Deseja ver as cartas dos jogadores? (S/N) ").upper()
        if decisao == 'S':
            print(f"\n{self.__j1.get_nome()} tem {self.__j1.get_tamanho_deck()} cartas, seu deck:")
            self.__j1.imprimir_deck()
            print(f"{self.__j2.get_nome()} tem {self.__j2.get_tamanho_deck()} cartas, seu deck:")
            self.__j2.imprimir_deck()
        
    def iniciar_jogo(self) -> None:
        self.set_jogadores()
        
        self.__baralho = self.__baralho.montar()
        
        decisao = input("Deseja ver as cartas do baralho? (S/N) ").upper()
        if decisao == 'S':
            self.__baralho.imprimir()
        
        self.entregar_cartas()
        
        input("Pressione ENTER para começar o jogo.")
        
        while not self.__vencedor_jogo:
            self.duelo()
            self.verificar_vencedor_jogo()
            if self.__cont_rodadas > self.__limite_rodadas:
                print("Jogo Finalizando por execução de 100 rodadas, o vencedor será definido pelo maior número de cartas restantes.")
                break
            
        self.fim_jogo()
            
    def verificar_vencedor_jogo(self):
        if self.__j1.get_tamanho_deck() == 0:   
            self.__vencedor_jogo = self.__j2    
        elif self.__j2.get_tamanho_deck() == 0:
            self.__vencedor_jogo = self.__j1            

    def duelo(self):
        self.get_cartas_jogadas()
        
        print(f'==== {self.__vencedor_rodada.get_nome()} venceu a rodada! ====\n')
        
        for carta in self.__cartas_acumuladas:
            self.__vencedor_rodada.guardar_cartas(carta)
        
        print(f"{self.__vencedor_rodada.get_nome()} ganhou as cartas que foram acumuladas:\n")
        for carta in self.__cartas_acumuladas:
            print(f"{carta} ", end=" \n") 
            
        self.__cartas_acumuladas.clear()

        self.__cont_rodadas += 1
        
        self.__vencedor_rodada = None
        input("\nPressione ENTER para continuar o jogo.")
      
    def get_cartas_jogadas(self):
        carta_jogador1 = self.__j1.jogar_carta()
        carta_jogador2 = self.__j2.jogar_carta()
        
        self.__cartas_acumuladas.append(carta_jogador1)
        self.__cartas_acumuladas.append(carta_jogador2)
        
        self.imprimir_duelo(carta_jogador1, carta_jogador2)
        
        self.__vencedor_rodada = self.comparar_cartas(carta_jogador1, carta_jogador2)
    
    def imprimir_duelo(self, carta1, carta2):
        print(f'\n===== Rodada {self.__cont_rodadas} =====\n')
        print(f'({self.__j1.get_nome()}: {self.__j1.get_tamanho_deck()} cartas)' ,end='    ')
        print(f'| {carta1} | X | {carta2} |', end='    ')
        print(f'({self.__j2.get_nome()}: {self.__j2.get_tamanho_deck()} cartas)\n')
    
    def comparar_cartas(self, carta1, carta2):
        if carta1.peso > carta2.peso:
            return self.__j1
        elif carta2.peso > carta1.peso:
            return self.__j2
        else:
            return self.rodada_empate()
            
    def rodada_empate(self):
        
        while self.__vencedor_rodada is None:
            print(f'Rodada {self.__cont_rodadas} empatada!\n')
            print(f"Quem desempatar ganhará essas cartas: \n")
            
            for carta in self.__cartas_acumuladas:
                print( carta)
            print()
            
            input("Pressione ENTER para continuar o empate.")
            self.get_cartas_jogadas()
        
        return self.__vencedor_rodada
    
    def fim_jogo(self):
        
        if(self.__vencedor_jogo is None):
            if self.__j1.get_tamanho_deck() > self.__j2.get_tamanho_deck():
                self.__vencedor_jogo = self.__j1
            else:
                self.__vencedor_jogo = self.__j2
             
        print(f'\n===== Fim de Jogo! =====\n')
        print(f'({self.__j1.get_nome()}: {self.__j1.get_tamanho_deck()} cartas)')
        print(f'({self.__j2.get_nome()}: {self.__j2.get_tamanho_deck()} cartas)\n')
           
        print(f'{self.__vencedor_jogo.get_nome()} VENCEU O JOGO!')
        
        decisao = input("Jogo encerrado! Deseja jogar novamente? (S/N)").upper()
        
        while decisao != 'S' and decisao != 'N':
            print()
            decisao = input("Opção Inválida. Deseja jogar novamente? (S/N)").upper() 
        
        if decisao == 'S':
            self.resetar_jogo()
            
        else:
           print("\n==== Obrigado por jogar! ====")
    
    def resetar_jogo(self):
        self.__cont_rodadas = 1
        self.__cartas_acumuladas = []
        self.__vencedor_rodada = None
        self.__vencedor_jogo = None
        self.__baralho.limpar_pilha()
        self.__baralho = Baralho()
        self.__j1.limpar_deck()
        self.__j2.limpar_deck()
        self.iniciar_jogo()