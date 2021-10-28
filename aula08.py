#Modulos (comandos import e from/import)
'''math : biblioteca matematica do python
ceil: realiza arrendodamento para cima do numero
floor: realiza arrendodamento para baixo do numero
trunc: chamado truncade, realiza a "truntagem" do numero, eliminando valores depois da virgula
pow: potenciacao do numero
sqrt: raiz quadrada do numero (tenta memorizar isso, plis)
factorial: fatorial do numero
Exemplo
'''

'''
import math

n = int(input('Digite um numeto: '))
raiz = math.sqrt(n)
print('*'*30)
print('A raiz de {} e igual a {:.2f}'.format(n,raiz))
print("A raiz de {} sera arrendondada para {}".format(n, math.ceil(raiz))) #ceil arrendonda para cima
print('='*30)
'''

#Diferencas na forma de importação, 
#Onde o import acima generaliza a chamada, sendo necessario especificar quem esta sendo chamado
#E no from permite especificar de ante mao, mas limita o uso do import

'''
from math import sqrt, floor

n = int(input('Digite um numero: '))
raiz = sqrt(n) #Raiz do numero
print('*'*30)
print('A raiz de {} e igual a {:.2f}'.format(n,raiz))
print("A raiz de {} sera arrendondada para {}".format(n, floor(raiz))) #floor arrendonda para baixo
print('='*30)
'''
'''
import random
num = random.random() #o random.random so gera numeros entre 0 a 1 em float
nu = random.randint(1, 10) #o randint deve ser limitado em (inicial, final)
print('='*30)
print(nu)
print('='*30)
'''
'''
Para importar o emoji para o terminal
Use o Terminal - powershell
comandos de instalacao: 1 - pip install emoji 
2 - pip install emoji --upgrade
'''
import emoji

print(emoji.emojize('Python is :shit:',use_aliases=True))