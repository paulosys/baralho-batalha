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
    
    def configurar_jogo(self):
        self.set_jogadores()
        
        self.__baralho = self.__baralho.montar()
        
        decisao = input("Deseja ver as cartas do baralho? (S/N) ").upper()
        if decisao == 'S':
            self.__baralho.imprimir()
        
        self.entregar_cartas()
        
        input("Pressione ENTER para começar o jogo.")
        
        self.iniciar_jogo()
    
    def set_jogadores(self) -> None:
        print("\n======= Definindo Jogadores =======\n")
        self.__j1 = Jogador(input("Digite o nome do jogador 1: "))
        print(f'\nJogador 1 definido como: {self.__j1.get_nome()}\n')
        self.__j2 = Jogador(input("Digite o nome do jogador 2: "))
        print(f'\nJogador 2 definido como: {self.__j2.get_nome()}\n')
        print("======= Jogadores definidos com Sucesso! =======\n")
        
    def entregar_cartas(self) -> None:
        metade_baralho = 52 // 2
        jogadores = [self.__j1, self.__j2]
        input("Pressione ENTER para Entregar as cartas.")
        for jogador in jogadores:
            for i in range(3):
                print(f"\nEntregando as cartas para {jogador.get_nome()}...")
                sleep(0.5)
            for carta in range(metade_baralho):
                try:
                    jogador.set_deck(self.__baralho.desempilhar())
                except IndexError:
                    raise BaralhoException('O baralho está vazio. Não há cartas para dividir')
            print(f"\n======= Cartas entregues para {jogador.get_nome()} =======")
        
        decisao = input(f"\nDeseja ver as cartas dos jogadores? (S/N) ").upper()
        print("\n")
        if decisao == 'S':
            for jogador in jogadores:
                print(f"{jogador.get_nome()} tem {jogador.get_tamanho_deck()} cartas, seu deck:")
                jogador.imprimir_deck()
    
    def iniciar_jogo(self) -> None:
        while not self.__vencedor_jogo:
            self.duelo()
            self.__vencedor_jogo = self.verificar_vencedor_jogo()
            if self.__cont_rodadas > self.__limite_rodadas:
                print("Jogo Finalizando por execução de 100 rodadas, o vencedor será definido pelo maior número de cartas restantes.")
                break
            
        self.fim_jogo()
        

    def duelo(self):
        carta_j1, carta_j2 = self.get_cartas_jogadas()
        
        self.imprimir_duelo(carta_j1, carta_j2)
        
        self.comparar_cartas(carta_j1, carta_j2)
    
        print(f'==== {self.__vencedor_rodada.get_nome()} venceu a rodada! ====\n')
        
        for carta in self.__cartas_acumuladas:
            self.__vencedor_rodada.guardar_cartas(carta)
        
        print(f"{self.__vencedor_rodada.get_nome()} ganhou as {len(self.__cartas_acumuladas)} cartas que foram acumuladas:\n")
        for carta in self.__cartas_acumuladas:
            print(f"{carta} ", end=" \n") 
            
        self.__cartas_acumuladas.clear() # Limpa a lista de cartas acumuladas para a próxima rodada

        self.__cont_rodadas += 1
        
        self.__vencedor_rodada = None
        input("\nPressione ENTER para continuar o jogo.")    
      
    def get_cartas_jogadas(self):
        carta_jogador1 = self.__j1.jogar_carta()
        carta_jogador2 = self.__j2.jogar_carta()
        
        self.__cartas_acumuladas.append(carta_jogador1)
        self.__cartas_acumuladas.append(carta_jogador2)
        
        return carta_jogador1, carta_jogador2
    
    def imprimir_duelo(self, carta1: Carta, carta2: Carta):
        print(f'\n===== Rodada {self.__cont_rodadas} =====\n')
        print(f'({self.__j1.get_nome()}: {self.__j1.get_tamanho_deck()} cartas)', end='    ')
        print(f'| {carta1} | X | {carta2} |', end='    ')
        print(f'({self.__j2.get_nome()}: {self.__j2.get_tamanho_deck()} cartas)\n')
    
    def comparar_cartas(self, carta1: Carta, carta2: Carta):
        '''
        Define o vencedor da rodada de acordo com a maior carta. (peso)
        '''
        if carta1.get_peso > carta2.get_peso:
            self.__vencedor_rodada = self.__j1
        elif carta2.get_peso > carta1.get_peso:
            self.__vencedor_rodada = self.__j2
        else:
            self.rodada_empate()
            
    def rodada_empate(self):
        '''
        Se ocorrer um empate, o programa pede mais uma rodada, compara as cartas, até que um dos jogadores desempatem o jogo, se isso não ocorrer, o programa chama o método roda_empate() recursivamente
        '''
        print(f'Rodada {self.__cont_rodadas} empatada!\n')
        print(f"As cartas acumularão até um desempate, cartas acumuladas atualmente: \n")
            
        for carta in self.__cartas_acumuladas:
            print(carta)
        print()
        input("Pressione ENTER para continuar o empate.")
        
        carta_j1, carta_j2 = self.get_cartas_jogadas()
        
        self.imprimir_duelo(carta_j1, carta_j2)
        
        self.comparar_cartas(carta_j1, carta_j2)
    
    def verificar_vencedor_jogo(self):
        if self.__j1.get_tamanho_deck() == 0:   
            return self.__j2    
        elif self.__j2.get_tamanho_deck() == 0:
            return self.__j1
        return None  
    
    def fim_jogo(self):
        
        if(self.__vencedor_jogo is None):
            if self.__j1.get_tamanho_deck() > self.__j2.get_tamanho_deck():
                self.__vencedor_jogo = self.__j1
            else:
                self.__vencedor_jogo = self.__j2  
             
        print(f'\n===== Fim de Jogo! =====\n')
        print(f'({self.__j1.get_nome()}: {self.__j1.get_tamanho_deck()} cartas)')
        print(f'({self.__j2.get_nome()}: {self.__j2.get_tamanho_deck()} cartas)\n')
           
        print(f'{self.__vencedor_jogo.get_nome()} VENCEU O JOGO!\n')
        
        decisao = input("Jogo encerrado! Deseja jogar novamente? (S/N)").upper()
        
        while decisao != 'S' and decisao != 'N':
            decisao = input("\nOpção Inválida. Deseja jogar novamente? (S/N)").upper() 
        
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