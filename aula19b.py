# Exercicio 90
# Faça um programa que leia nome e média de um aluno,
# guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.
'''
aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}:'))
if aluno['media'] >=7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['media'] < 7 :
    aluno['situação'] = "Recuperação"
else:
    aluno['situação'] = "Reprovado"
print('\033[1;33m-\033[m'*30)
for k, v in aluno.items():
    print(f'- {k} é igual a {v}')
print('\033[1;36m-\033[m'*30)
'''
# Exercico 91
# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário em Python.
# No final, coloque esse dicionário em ordem,
# sabendo que o vencedor tirou o maior número no dado.
'''
import random
from time import sleep
from operator import itemgetter # ordena os valores apartir da posição especifica, chave ou valor (0,1) eu acho!
jogo = {'jogador1': random.randint(1,6),
        'jogador2': random.randint(1,6),
        'jogador3': random.randint(1,6),
        'jogador4': random.randint(1,6)}
ranking = {}
print('\033[1;32m=-\033[m'*30)
print('Os Sorteados são:')
print('\033[1;32m-\033[m'*30)
for k, v in jogo.items():
    print(f'O jogador {k} tirou {v} no dado.')
    sleep(1)
print('\033[1;32m-\033[m'*30)
ranking = sorted(jogo.items(), key = itemgetter(1), reverse = True) # reserse mostra do maior ao menor, se for True 
print("======= Ranking dos Jogadores =======")
print(ranking) # por se apresentar como uma lista, 
for i, v in enumerate(ranking): # sera tratada como tal
    print(f'{i+1}° lugar: {v[0]} com {v[1]}') 
    sleep(0.5)
print('\033[1;32m=-\033[m'*30)
'''
# Exercicio 92
# Crie um programa que leia nome, ano de nascimento e carteira de trabalho
# e cadastre-o (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá
# também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
'''
from datetime import datetime # importando a data do atual do pc da biblioteca do tempo corrente
dados = dict()
print('\033[1;31m=-\033[m'*30)
dados['nome'] = str(input('Digite o nome: '))
nasc = int(input('Digite o ano de nacimento: ')) # nao precisa esta no dicionario
dados['idade'] = datetime.now().year - nasc # datetime.now().year pega somente o ano do pc
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contrato'] = int(input('Ano de contrato: '))
    dados['salario'] = float(input('Valor do salário: R$'))
    # ano pra se aposentar = idade + ((ano da contratação + 35) - ano do pc) 
    dados['aposentar'] = dados['idade'] + ((dados['contrato'] + 35) - datetime.now().year)
print('\033[1;37m=-\033[m'*30)        
print(dados)
for k, v in dados.items():
    print(f' - {k} = {v}')
'''

# Exercicio 93
# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário,
# incluindo o total de gols feitos durante o campeonato.
'''
print('\033[1;37m=-\033[m'*30)
jogador = {} # ou dict[]
partidas = [] # ou list()
jogador['nome'] = str(input('Nome do Jogador: '))
total = int(input(f'Partidas jogadas por {jogador["nome"]}: '))
for c in range(0, total):
    partidas.append(int(input(f'Quantos gols na {c+1}° partida: ')))
jogador['gols'] = partidas[:] # gols recebe uma copia de partidas [:]
jogador['total'] = sum(partidas) # somado os numeros de gols de partida
print('\033[1;34m=-\033[m'*30)
print(jogador)
print('\033[1;35m=-\033[m'*30)
for k, v in jogador.items():
    print(f'{k} = {v}')
print('\033[1;36m=-\033[m'*30)
print(f'O {jogador["nome"]} fez {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador['gols']): # infomações da lista que ta dentro do jogador['gols]
    print(f'Na {i+1}° partida fez {v} gols.')
print(f'Total de gols feitos: {jogador["total"]}')
'''
# Exercicio 94
# Crie um programa que leia nome, sexo e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
# No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média
'''
from emoji import emojize
pessoa = dict()
povo = list()
soma = media = 0 # soma e media das idades 
print('\033[1;32m=-\033[m'*30)
while True: # laço infinito
    pessoa.clear() # antes de preencher o dicionario novamente, deve-se limpar os valores
    pessoa['nome'] = str(input('Digite o nome: '))
    while True:    
        pessoa['sexo'] = str(input('Digire o genero [M/F]: ')).upper()[0] # apenas a primeira letra maiuscula
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Apenas M ou F')
    pessoa['idade'] = int(input('Digite a idade: '))
    soma += pessoa['idade']
    povo.append(pessoa.copy()) # deve-se copiar o dicionário para a lista antes de usar
    while True: # forma bonitinha de reiniciar a lista do dicionario
        resp = str(input("Continua? [S/N] ")).upper()[0]
        if resp in 'SN':
            break
        print('Responda apenas S ou N!')
    if resp == "N":
        break
print('\033[1;37m=-\033[m'*30)
print(pessoa)
print(povo)
print('\033[1;33m=-\033[m'*30)
print(f'A) Ao todo temos {len(povo)} pessoas cadastradas.') # forma de saber quantoas cadastros na lista
media = soma / len(povo)
print(f'B) A idade media dessas pessoas é {media:5.2f} anos.') # media com 5 casas e 2 digitos
print("C) Mulheres cadastradas foram", end=' ')
for p in povo:
    if p['sexo'] == 'F': # ou if p['sexo] in 'Ff:
        print(f'{p["nome"]}', end=', ')
print() # um print vazio pra quebra a linha ㄟ( ▔, ▔ )ㄏ
print(f'D) as pessoas com idade acima da média é: ')
for p in povo: # e feito a media da lista
    if p['idade'] >= media:
        print('   ', end='') # seila?
        for k , v in p.items(): # ja que o p['idade] pertence a um dicionário
            print(f'{k} = {v}; ', end='')
        print() # um print vazio pra quebra a linha ㄟ( ▔, ▔ )ㄏ
print(emojize(':waving_hand: << ENCERRADO >> \U0001F44B'))
print('\033[1;31m=-\033[m'*30)
'''
# Exrcicio 95
# Aprimore o desafio 93 para que ele funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
'''jogador = {}
partidas = []
time = list()
while True:
    jogador.clear() # a cada laço novo, novos valores são inseridos em novo registro do dicionario
    jogador['nome'] = str(input('Nome do jogador: '))
    total = int(input('Quantas partidas jogadas: '))
    partidas.clear() # limpar os valores da partida para não repetir-los
    for cont in range(0, total):
        partidas.append(int(input(f'   Quantos gols na {cont+1}° partida: ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy()) # a lista time adiciona uma copia das informações do dicionario
                                # jogador antes de ser reiniciado o loop
    while True: # o loop infinito serve para manter a responsta certa
        resp = str(input(' Quer continuar?[S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print(' Apenas \033[1;32m S \033[m ou \033[1;31m N \033[m!')
    if resp == 'N': # break finito do loop infinito
        break
     
print('\033[1;31m=-\033[m'*30)
print('COD ', end='') # codigo do cabeçalho
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('\033[1;31m=-\033[m'*30)
for i, jog in enumerate(time):
    print(f'{i+1:>2} ', end='')
    for dado in jog.values():
        print(f'{str(dado):<15} ', end='') # Espaço entre as colunas de valores
    print() #um print vazio pra quebra a linha ㄟ( ▔, ▔ )ㄏ
print('\033[1;35m=-\033[m'*30)
while True: # laço para escolher o jogador a mostrar
    busca = int(input('Mostras informações de qual jogador? (999 para parar): '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f' ERRO! jogador não existe com codigo {busca}!')
    else:
        print(f'-- Jogador {time[busca]["nome"]}: ')
        for i, gol in enumerate(time[busca]['gols']):
            print(f'  No {i+1}° jogo fez {gol} gols')
    print('\033[1;35m=-\033[m'*30)
print(' <<  ATÉ MAIS >>')
print('\033[1;36m=-\033[m'*30)
print(jogador)
print('\033[1;32m=-\033[m'*30)
'''
# mostragem de reultados original do exercicio 93
'''
for k, v in jogador.items():
    print(f'{k} = {v}')
print('\033[1;33m=-\033[m'*30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas')
for i, v in enumerate(jogador['gols']):
    print(f'   Na {i+1}° partida, fez {v} gols.')
print(f'Sendo um total de {jogador["total"]} gols.')
print('\033[1;34m=-\033[m'*30)'''
