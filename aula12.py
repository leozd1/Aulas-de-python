# Aula 12
# Condições Aninhadas
# Explorando comandos if.. elif.. else
'''
Toda estrutura deverá começar com um ou vários if (se), 
poderá possuir um ou vários elif (senão se),
mas so poderá possuir um else (senão), sendo o seu uso opcional.
Onde poderá usar varios elif, mas somente iniciando com if
'''
#Exemplos:
import emoji
from emoji.core import emojize
cores = {'limpa': '\033[m',
         'negrito': '\033[1;34m',
         'amarelo': '\033[01;33m',
         'vermelho': '\033[04;31m',
         'cinza': '\033[7;37m'}

nome = str(input('Digite seu nome: \n'))

if nome == 'Renato':
    print('Que nome bonito!')
elif nome == "Pedro" or nome == 'Maria' or nome == "João":
    print(emoji.emojize('Que nome comum! :\U0001f92a:', language='pt'))
elif nome in 'ana carla rosicleia amanda':
    print('Hummm... nome de mulher')
else:
    print('Nada interessante!')
print(emoji.emojize('Tenha um bom dia {}{}{}, :dedo_do_meio:'.format(cores['negrito'],nome,cores['limpa']),language='pt'))
