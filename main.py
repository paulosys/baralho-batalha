from Jogador import Jogador
from Batalha import Batalha

batalha = Batalha()

j1 = Jogador('Jogador 1')
j2 = Jogador('Jogador 2')

batalha.set_jogadores(j1,j2)

batalha.iniciar_jogo()