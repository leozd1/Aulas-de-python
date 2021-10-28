# Exercicio 84
# Faça um programa que leia nome e peso de várias pessoas,
# guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.
'''
temp = [] # lista temporaria pra guardar as informações
princ = [] # lista principal
maior = menor = 0
while True:
    temp.append(str(input('nome: ')))
    temp.append(float(input('peso: ')))
    if len(princ) == 0 :
        maior = menor = temp[1] # como eu quero registrar o peso, coloco na variavel 1, ja que 0 é o nome
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    princ.append(temp[:]) # faz uma copia da lista temp
    temp.clear() # limpa depois a lista temporaria para não duplica-la
    resp = str(input('Quer continuar [S/N]? '))
    if resp in "Nn":
        break
print('=-'*40)
# print(f'Os dados foram: {princ}') # não ta no exercicio
print(f'Foram cadastrados {len(princ)} pessoas') # vai ler quantos dados foram cadastrados na lista
print(f'O maior peso foi {maior} kg: ', end='')
for p in princ: # mostra a lista de pessoas maiores
    if p[1] == maior:
        print(f'{p[0]}', end='')
print()
print(f'O menor peso foi {menor} kg.: ', end='')
for p in princ:
    if p[1] == menor:
       print(f'{p[0]}', end='')
print()
'''
# Exercicio 85
# Crie um programa onde o usuário possa digitar sete valores numéricos
# e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
# No final, mostre os valores pares e ímpares em ordem crescente.
'''
nu = [[], []] # sendo possivel criar previamente listas dentro da lista
valor = 0 # onde o valor iniciado
for c in range(1, 8): # o for mostra a quantidade solicitada pelo comando (sete valores)
    valor = int(input(f"Digite o {c}° valor: ")) # que ao ser lido
    if valor % 2 == 0: # fara a verificação dele (se ele é par ou impar)
        nu[0].append(valor) # e o adcionara a sua lista respectiva
    else:
        nu[1].append(valor)
print('-='*40)
nu[0].sort() # e o sort() o organizará a lista pedida
nu[1].sort()
print(f'Todos os valores: {nu}')
print(f"Os valores impares: {nu[1]}") # e a mostraremos adequadamente somente o que pedimos
print(f"Os valores pares: {nu[0]}")
# Preste atenção na logica do exercicio acima
'''
# Exercicio 86
# Crie um programa que declare uma matriz de dimensão 3×3
# e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.
'''
matriz = [[0,0,0],[0,0,0], [0,0,0]] # já sabendo a quantidade de valores, faço a matriz vazia, apenas com 0
                                    # declarando assim a matriz
for linha in range(0,3): # criando a linha da matriz, que vai de 0 a 2
    for coluna in range(0,3): # criando a coluna da matriz
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: ')) # onde sera jogado 
                                                                                        # na coluna e linha indicada
print('-='*40)
for l in range (0,3):
    for c in range (0,3):
        print(f'[{matriz[l][c]:^5}]', end='') # mostra a matriz, mas ao mostrar a linha, deixemos centralizado 
    print() # ao criar a coluna, o print quebra ela pra poder começar outra linha.
'''
# Exercicio 87
# Aprimore o desafio anterior, mostrando no final: 
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.
'''
matriz = [[0,0,0],[0,0,0],[0,0,0]]
somapar = maior = somacoluna = 0 # a soma dos pares, a soma das colunas e o maior valor precisam ser declarados
for linha in range (0,3):
    for coluna in range (0,3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: ')) # a inserção de valores igual ao
                                                                                         # exercicio anterior
print('\033[1;34m-=\033[m'*40)
for l in range (0,3):
    for c in range (0,3):
        print(f'[{matriz[l][c]:^5}]', end='') # mostra a matriz, mas ao mostrar a linha, deixemos centralizado 
        if matriz[l][c] % 2 ==0: # verifica se a matris tem algum par
            somapar += matriz[l][c]
    print() # ao criar a coluna, o print quebra ela pra poder começar outra linha.
print('\033[1;35m-=\033[m'*40)
print(f'A soma dos valores pares é: {somapar}') # mostra a soma dos pares
print('-'*30)
for lin in range (0, 3): # para fazer a soma da coluna, se faz um for da linha
    somacoluna += matriz[lin][2] # e como sabemos a base da coluna, so variamos a linha
                                 # cuidado ao declarar o tipo de linha (usa a do for)
print(f' A soma da 3° coluna é: {somacoluna}')
print('-'*30)
# usando a mesma logica, descobrimos a base da linha e variamos a coluna
# onde a base da linha é 1 (já que é a segunda linha), usamos o for pra contar a coluna
for col in range (0,3):
    if c == 0: # verificamos se é primeira coluna
        maior = matriz[1][c]
    elif matriz[1][c] > maior: # dai damos a sequencia da soma das colunas
        maior = matriz[1][c
print(f'O maior valor da segunda linha é: {maior}')
'''
# Exercicio 88
# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números
# entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
'''
from emoji import emojize
from random import randint
from time import sleep
lista = list() # a lista que sera randomizada
jogos = list() # lista da lista copiada

quant = int(input("Quantas vesez quer jogar? "))
totjogo = 1
while totjogo <= quant:
    cont=0 
    while True: # enquanto for verdadeiro
        num = randint(1, 60) # cria uma lista de aleatoria de 1 ate 60
        if num not in lista: # se o numero não estiver(repetido)
            lista.append(num)
            cont+=1
        if cont >= 6:
            break 
    lista.sort() # mostrando a lista em orde crescente
    jogos.append(lista[:]) # fara uma copia da lista de jogos
    lista.clear() # onde apaga a lista original depois de copiada
    totjogo +=1
print('\033[1;35m-=\033[m'*20)
print(emojize(f':saco_de_dinheiro:        {"NUMEROS DA MEGA SENA":=^20}        :saco_de_dinheiro:', language='pt'))
print('\033[1;35m-=\033[m'*20)
print(f'\033[1;34m{quant} NUMEROS SORTEADOS:\033[m')
for indice, lis in enumerate (jogos): # enumerate servira pra organizar a lista
    print(f'jogo: {indice +1}: {lis}') # onde mostrara uma lista composta em ordem
    sleep(2) # espera 2 segundos pra mostar os numeros
'''
# Exercicio 89
# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um
# e permita que o usuário possa mostrar as notas de cada aluno individualmente.
'''
from emoji import emojize
ficha = list() # ficha padrão para cada aluno
# informações dos alunos
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('1° nota: '))
    nota2 = float(input('2° nota: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar?[S/N] '))
    if resp in "Nn":
        break
print('\033[1;32m-=\033[m'*30)
print(f'{"N° ":<4}{"Nome ":<10}{"Media ":>8}') # Arrumação da lista?
print('\033[1;31m-\033[m'*30)
for indice, aluno in enumerate(ficha): # para cada indice e aluno enumerado da lista ficha
    print(f'{indice+1:<4}{aluno[0]:<10}{aluno[2]:>6.1f}') # onde posição(indice), nome do aluno(aluno[0]),
                                                        # e media (aluno[2]) com uma casa decimal
                                                        # arrumada em lista vertical, mas presta atenção nisso
while True:
    print('\033[1;36m-\033[m'*30)
    opc = int(input('Mostrar nota de qual aluno: (999, interronpe) ')) # opção de mostrar nota de alunos
    print('\033[1;33m-\033[m'*30)
    if opc == 999 :
        print(emojize('FINALIZANDO... \U0001f916', language='pt'))
        break
    if opc <= len(ficha)-1: # a opção escolhida menos um, ja que aluno começã com 0
        print(f'Notas de {ficha[opc][0]} são: {ficha[opc][1]}') # mostra as notas do nome do aluno[0] e suas notas[1]
print(emojize('Tenha um bom dia :rosto_risonho:', language='pt'))
print('\033[1;33m-\033[m'*30)
'''
