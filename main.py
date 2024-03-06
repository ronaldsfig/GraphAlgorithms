import sys
sys.path.insert(0, '/graphs')
from graphs.weightedGraph import WeightedGraph

casa_do_joao = 'J'
armazem = 'A'
pracinha = 'P'
quitanda = 'Q'
banca_de_jornal = 'B'
cancela = 'C'
escola = 'E'

edges = [
    ((casa_do_joao, armazem), 5),
    ((casa_do_joao, pracinha), 6),
    ((casa_do_joao, quitanda), 10),
    ((armazem, banca_de_jornal), 13),
    ((pracinha, quitanda), 3),
    ((pracinha, banca_de_jornal), 11),
    ((pracinha, cancela), 6),
    ((quitanda, banca_de_jornal), 6),
    ((quitanda, cancela), 4),
    ((banca_de_jornal, escola), 3),
    ((cancela, escola), 8),
]

weighted_graph = WeightedGraph(edges)

print(weighted_graph)
