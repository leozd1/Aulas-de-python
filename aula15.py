# Interrompendo Estruturas de repetições (while)
# Vamos aprender como utilizar a instrução break e os loopings infinitos a favor das nossas estratégias de código.
# É muito importante saber usar o break no Python, já que em alguns casos precisamos interromper um laço no meio do caminho.
# Além disso, vamos aprender como trabalhar com as novas fstrings do Python.
'''
Exemplo:
portugol                                python
enquanto Verdadeiro:                    while True:
    se tiver chão,                      if chão:
        passo                               passo
    se tiver buraco,                    if buraco:
        pula                                pula
    se tiver moeda,                     if moeda:
        pega                                pega
    se troféu,                          if troféu:
        pula                                pula
        interrompa                          break
pega(fim)                             pega
'''
# Exemplo pratico:
'''
cont = 1
while cont <= 10: # Se cont<=10 for trocado por True, o laço será permanente (eterno, ate o fim da memória)
    print(cont, '...', end= '')
    cont +=1
print('Acabou')
'''
# Exemplo pratico 1:
'''
n = 0
while n != 999: # Se o numero for diferente do 999, o laço sera eterno, o 999 sera um flag (um sinal de parada)
    n= int(input("Digite um numero: ")) 
'''
# Exemplo 2:
'''
n = cont = 0
while cont < 5: # se contador for menor que 5, para o laço
    n= int(input("Digite um numero: ")) 
    cont += 1 # serve como contador de repetição do laço
'''
# Exemplo 3:
'''
n = s = 0
while n != 999:
    n= int(input("Digite um numero: "))
    s += n
s-=999 # Gambiarra, para tirar o 999 da somatoria
print('A soma dos numeros sera {}'.format(s))
'''
# Exemplo 4:
'''
n = s = 0
while True: # loop infinito por causa do True
    n= int(input("Digite um numero: "))
    if n == 99: # se o n for 99, dara um break (parada) no laço
        break 
    s += n
# print('A soma dos numeros sera {}'.format(s)) # ou 
print(f"A soma dos numeros sera {s}")
'''

# fstrings do Python
# fstrings = forma de escrever comandos
'''
print('A soma dos numeros sera {}'.format(s)) ou 
print(f"A soma dos numeros sera {s}")
'''
# Exemplo 5:
nome = 'Juse'
idade = 33
print(f'O {nome} tem {idade} anos.') # ou 
print('O {} tem {} anos.'.format(nome, idade)) # ou 
print('O %s tem %d anos.' % (nome, idade)) # usado no python 2 (não mais usado)

# Exemplo 6:
'''
nome = 'Juse'
idade = 33
salario = 998.3
print(f'O {nome:-<20} tem {idade:->10} anos, e ganha {salario:.2f} reais.')
'''
# Alinhamentos:
'''
{nome:-<20} : alinhado a esquerda em20 casas
{nome:->20} : alinhado a direita em 20 casas
{nome:^20} : centralizado em 20 casas
{nome:-^20} : alinhado em 20 casas tracejadas
'''