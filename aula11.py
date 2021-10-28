# Aula 11 (EXTRA)
# Adicionando Cores no terminal
#  Utilizando os códigos de escape sequence ANSI
# E código \033[m com todas as suas principais possibilidades.

# ANSI escape sequence
'''
para usar cores no terminal usa-se
\033[  m
e no lugar do espaço pode se colocar codigos (de 1 a te  3 codigos diferentes) separados por ponto e virgula (;)
onde cada cotido tem um comportamento diferente
style = comportamento do estilo
text = referente ao texto
back = referente ao background, cor de fundo

ex: \033[0;33;44m

  style                                      text                   back 
    0 = none (zero ou nada)                   30 = branco            40 = branco
    1 = bold (negrito)                        31 = vermelho          41 = vermelho
    4 = underline (sublinhado)                32 = verde             42 = verde 
    7 = negative   (inverter cores, )         33 = amarelo           43 = amarelo
                                              34 = azul              44 = azul
                                              35 = roxo              45 = roxo
                                              36 = azul claro        46 = azul claro
                                              37 = cinza             47 = cinza
'''
#exemplos de uso
print('\033[4;31;43m Olá Mundo\033[m') # negrito, vermelho e amarelo 
import emoji
print(emoji.emojize('Foda-se :dedo_do_meio:', language='pt', variant='emoji_type')) 
#OBS: o codigo \033[m atinge todos os prints senão for posto no fim do print
a = 3 
b = 5
print('Os valores são \033[32m{}\033[m e \033[36m{}\033[m.'.format(a, b))

z = 'Orificio Rugoso'
print('Vai tomar no {}{}{}!!!'.format('\033[1;35m', z, '\033[m' ))

#pode-se colocar em uma lista de cores
cru = 'Rsrsrsrsrsrsrsrsr'
cores = {'limpa': '\033[m',
         'amarelo': '\033[01;33m',
         'vermelho': '\033[04;31;40m',
         'cinza': '\033[7;37m'}
print(emoji.emojize('Vacilão :macaco_que_não_vê_nada: {}{}{}'.format(cores['cinza'], cru, cores['limpa']), language='pt'))

