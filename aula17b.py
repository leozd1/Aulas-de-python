# Exercicio 78
# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado
# e as suas respectivas posições na lista.
'''
from emoji import emojize
from time import sleep
x = list()
gran = 0
meno = 0
for i in range(0,5):
    x.append(int(input(f'Digite um valor na posição {i}: ')))
    if i == 0:
        gran = meno = x[i]
    else:
        if x[i] > gran:
            gran = x[i]
        if x[i] < meno:
            meno = x[i]
sleep(0.5)
print('=-'*30)
print(x)
print(f'O maior valor digitado foi {gran} nas posições ',end='')
for z, y in enumerate(x):
    if y == gran:
        print(f'{z}... ',end='')
print(f'\nO menor valor digitado foi {meno} nas posições ',end='')
for z, y in enumerate(x):
    if y == meno:
        print(f'{z}... ')
print(emojize(':rosto_de_palhaço:'*30, language='pt'))
'''
# Exercicio 79
# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
'''
from emoji import emojize
from time import sleep
num = list()
while True:
    n = int(input("Digite um numero: "))
    if n not in num:
        num.append(n)
        sleep(1)
        print(emojize(f'Valor adicionado com sucesso... :robot:'))
    else:
        print(emojize(f'Numero duplicado, tente devono: :smiling_face_with_sunglasses:'))
    r = str(input('Deseja continuar?[S/N] '))
    if r in 'Nn':
        break
print(emojize(f':círculo_vermelho:'*30, language='pt'))
num.sort()
print(emojize(f'Os numeros digitados foram: {num} \nVolte sempre!:smiling_face:'))
'''
# Exercicio 80
# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
# já na posição correta de inserção (sem usar o sort()).
# No final, mostre a lista ordenada na tela.
'''
lista = list()
for c in range(0, 5):
    n = int(input("Digite um numero: "))
    if c == 0 or n > lista[-1]: 
        lista.append(n)
        print('adicionado no final da lista')
    # elif n > lista[-1]: # se n for maior que o ultimo elemento da lista
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista.')
                break
            pos += 1
print('-='*30)
print(f'Os valores digitados foram: {lista}')
'''
# Exercicio 81
# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.
'''
x = list()
while True:
    x.append(int(input('Digite um "numero": ')))
    r = str(input('Deseja continuar [S/N]?')).upper()
    if r in 'Nn':
        break
print('=-'*30)
print(f'Você digitou {len(x)} numeros.\033[m')
x.sort(reverse=True)
print(f'O nmeros digitados em ordem decrescente são: \033[1;36m{x}\033[m')
if 5 in x:
    print(' O numero \033[1;32m5\033[m esta na lista')
else:
    print('Não há um numero \033[1;34m5\033[m na lista')
'''
# Exercicio 82
# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter
# apenas os valores pares e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.
'''
lista = []
pares = list()
impares = list()
while True:
    lista.append(int(input('Digite um numero: ')))
    resp = str(input("Continua? [S/N] "))
    if resp in 'Nn':
        break
for num, v in enumerate(lista):
    if v % 2 ==0:
        pares.append(v)
    else:
        impares.append(v)
print('=-'*30)
print(f'Você digitou: \033[1;36m{lista}\033[m')
print(f'Os numeros pares são: \033[1;34m{pares}\033[m')
print(f'Os numeros pares são: \033[1;32m{impares}\033[m')
'''
# Exercicio 83
# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está
# com os parênteses abertos e fechados na ordem correta.
exp = str(input("Digite sua expressão: "))
pilha = []
for simb in exp:
    if simb == '(': # se simb tiver parenteses abertos
        pilha.append('(') # eu adiciono na lista
    elif simb == ')': # Se simb tiver na parenteses fechados  
        if len(pilha) > 0: # leia a pilha, se for maior que 0 
            pilha.pop() # remove o ultimo item da lista
        else:
            pilha.append(')') # se não tiver nada, adciona na lista
            break # para aqui
if len(pilha) == 0:
    print("Sua expressão é válida")
else:
    print("Sua expressão está errada")
