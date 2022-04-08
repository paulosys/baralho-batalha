from Jogador import Jogador
from Batalha import Batalha

batalha = Batalha()

j1 = Jogador('Jogador 1')
j2 = Jogador('Jogador 2')

batalha.set_jogadores(j1,j2)

batalha.entregar_cartas()

j1.get_deck()
j2.get_deck()