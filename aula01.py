print('fudido, salve antes de xingar!')
msm = input('digite o nome: ')
print('É um prazer te conhecer {}!'.format(msm))

print(""" Para escrever um texto longo, 
pode-se usar as três aspas que ele mostra,
sem problemas, só não esqueça de colocar 
as três aspas no final, claro né!""")

print('{:10}'.format('oi'))  # pode-se colocar espaço no format colocando dois pontos
print('{:>10}'.format('oi')) # alinha-se a direita do espaço
print('{:<10}'.format('oi')) # alinha-se a direita do espaço
print('{:^10}'.format('oi')) # alinha-se ao centro do espaço

'''
atalhos do windows
alt + 92 = \
Alt + 26 = →
Alt + 27 = ←
Alt+16= ►
Alt+17= ◄
Alt+124= |
Alt+171=½
Alt+248= °
Alt+251= ¹
Alt+253= ²
Alt+252= ³

# Alinhamentos:
{nome:-<20} : alinhado a esquerda em 20 casas
{nome:->20} : alinhado a direita em 20 casas
{nome:^20} : centralizado em 20 casas
{nome:-^20} : alinhado em 20 casas tracejadas

As variveis compostas podem ser ter parenteses-(), chaves-[], colchetes-{}, ou nem isso
 Sendo:
 Tuplas= () 
 Listas = [] ou list()
 Dicionário = {} ou dict()
 
Caracteres coloridos
 ex: \033[0;33;44m -(nada; amarelo; azul) ou \033[m -(no fim, pra não afetar o resto do texto)

  style                                      text                   back 
    0 = none (zero ou nada)                   30 = branco            40 = branco
    1 = bold (negrito)                        31 = vermelho          41 = vermelho
    4 = underline (sublinhado)                32 = verde             42 = verde 
    7 = negative (inverter cores)             33 = amarelo           43 = amarelo
                                              34 = azul              44 = azul
                                              35 = roxo              45 = roxo
                                              36 = azul claro        46 = azul claro
                                              37 = cinza             47 = cinza

Biblioteca de Emotions 
from emoji import emojize #import a biblioteca de emojis
print(emojize(':bebê:', language= 'pt'))
ou
import emoji
print(emoji.emojize('Foda-se :dedo_do_meio:', language='pt', variant='emoji_type')) 

'''