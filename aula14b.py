# Exercicio 57
# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.
'''
r = str(input('Escolha um sexo [F/M/G]: ')).strip().upper()[0]
while r not in 'FfMnGg':    
    r = str(input('digite a opção correta! '))
print('Opção escolhida foi {}'.format(r))
'''
# Exercicio 58
# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar,
# mostrando no final quantos palpites foram necessários para vencer.
'''
from random import randint
#import time
from time import sleep # faz o pc esperar, ou dormir, por alguns segundos, antes de continuar
import emoji
pc = randint(0, 5)
print('-=-'*30)
print('Pensei em um numero entre 0 e 5, tente descobrir. ')
acertou = False
palpites = 0
while not acertou: enquanto não acertou, pois se acertar o num sai do laço
    num = int(input('digite um numero: ')) 
    palpites +=1
    print('Processando...')
    sleep(3)
    if num == pc: #se o num for igual ao pc
        acertou = True
    else: #senão, se não acertar continua dando palpites
        if num < pc: # se num for menor que pc
            print(emoji.emojize('Mais :indicador_apontando_para_cima:... tente novamente', language = 'pt'))
        elif num > pc: # senão se num for maior que pc
            print(emoji.emojize('Menos :dorso_da_mão_com_dedo_indicador_apontando_para_baixo:... Tente novamente, talvez acerte', language ='pt'))
# Se acertou
print(emoji.emojize('Acertou miseravi :rosto_abraçando:!  \nvocê: {} \nPC: {}'.format(num, pc),variant= 'emoji_type' ,language='pt'))
print('Acertou com {} palpites'.format(palpites))
print('-=-'*30)
'''
# Exercicio 59
# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso. 
'''
import emoji
from time import sleep
print("="*30)
n1 = int(input('Digite 1° numero: '))
n2 = int(input('Digite 2° numero: '))
opcao = 0
while opcao != 5:    
    print('==========MENU==========')
    print('[1] SOMAR'+
        '\n[2]MULTIPLICAR'+
        '\n[3]MAIOR NUMERO'+
        '\n[4]DIGITAR NOVOS NUMEROS'+
        '\n[5]SAIR DO PROGRAMA')
    opcao = int(input('Digite uma opção: '))
    if opcao == 1:
        s = n1 + n2
        print('A soma \033[01;31m{}\033[m e de \033[01;36m{}\033[m é \033[01;33m{}\033[m'.format(n1, n2, s))
    elif opcao == 2:
        r = n1 * n2
        print('A multiplicação de \033[01;31m{}\033[m com \033[01;36m{}\033[m é \033[01;33m{}\033[m'.format(n1, n2, r))
    elif opcao == 3:
        if n1 > n2:
            m = n1
        else:
            m = n2
        print("O maior numero é \033[01;33m{}\033[m".format(m))
    elif opcao == 4:
        print('digite os numeros novamente. ')
        n1 = int(input('Digite 1° numero: '))
        n2 = int(input('Digite 2° numero: '))
    elif opcao == 5:
        print('finalizando...')
        sleep(3)
    else:
        print(emoji.emojize('Opção invalida...Tente denovo :rosto_pensativo:', language = 'pt'))
print(emoji.emojize('fim do programa...Acabou :dedo_do_meio:', language = 'pt', variant= 'emoji_type'))
'''
# Exercicio 60
# Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Exemplo:
# 5! = 5 x 4 x 3 x 2 x 1 = 120
'''
from math import factorial
print('='*30)
n = int(input('digite um numero para ser fatorado: '))
# f = factorial(n) # forma com a biblioteca math
f = 1
c = n
print('Calculando {}! = '.format(n), end='')
while c >0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = '.format(f), end = '')
    f *= c # para substituir o fatorial
    c-=1
print('O resultado sera: {}'.format(f))
'''
# Exercicio 61
# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.
'''
print('='*30)
print('====== GERADOR DE PA =========')
primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
while cont < 10:
    print('{} >'.format(termo), end=' ')
    cont += 1
    termo += razao
print('fim')
print('='*30)
'''
# Exercicio 62
# Melhore o DESAFIO 61,
# perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos. 
'''
print('='*30)
print('====== GERADOR DE PA =========')
primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais!= 0:
    total = total + mais
    while cont <= total:
        print('{} >'.format(termo), end=' ')
        cont += 1
        termo += razao
    print('pausa')
    mais = int(input('Quantos termos a mais a mostrar? '))
print('fim')
print('Progressão com {} termos mostrados'.format(total))
print('='*30)
'''
# Exercicio 63
# Escreva um programa que leia um número N inteiro qualquer
# e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.
# Exemplo:
# 0 – 1 – 1 – 2 – 3 – 5 – 8 
'''
print('~'*30)
n = int(input('Quantos termos deseja mostrar? '))
t1 = 0 #serao os primeiros termos mostrados
t2 = 1
cont = 3 # o contador inicia no terceiro termo
print('*'*30)
print("{} - {}".format(t1, t2), end='')
while cont <= n:
    t3 = t1 + t2 # o terceiro termo é a soma dos dois outros
    print(' - {}'.format(t3), end='')
    t1 = t2 # aqui pulamos os termos para proxima "casa",
    t2 = t3 # criando um novo terceiro
    cont += 1 # contador para manter controle
print(' > fim')
print('~'*30)
'''
# Exercicio 64
#  Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados
# e qual foi a soma entre eles (desconsiderando o flag).
'''
print('~'*30)
# x = 0 # inicializador da logica
# cont = 0 # contador
# soma = 0 # soma
x = cont = soma = 0 # resumo das variaveis com o mesmo inicio 
x = int(input('digite um numero [digite 999 para parar]:  ')) # comando fica de fora do while para poder retirar o flag(999), 
while x != 999: # só vai parar quando 999 for digitado    
    soma += x
    cont += 1
    x = int(input('digite um numero [digite 999 para parar]:  ')) # já que ele fica no fim do while
print("Você digitou {} números e soma deles é {}.".format(cont, soma)) # podendo ser feito .format(cont -1, soma - 999)
print('fim')
print('~'*30)
# não recomendado pois é uma gambiarra pra improvisar uma solução
'''
# Exercicio 65
# Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
'''
print('\033[1;32m~\033[m'*30)
res = 's'
soma = quant = media = 0 # pra ter a media dos valores, precisa somar e dividir pela quantidade
maior = menor = 0 # usa essa forma se todos receberem 0
while res in 'Ss':
    n = int(input('Digite um numero: '))
    soma += n
    quant += 1
    if quant == 1 :
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n        
    res = str(input("Quer continuar?[S/N] ")).upper().strip()[0]
media = soma / quant
print('Foram \033[1;36m{}\033[m numeros digitados, a media dos fumeros digitados é \033[1;32m{:.2f}\033[m'.format(quant, media))
print('Maior numero é \033[1;31m{}\033[m e o menor é \033[1;34m{}\033[m'.format(maior, menor))
print('Fim')
print('\033[1;32m~\033[m' *33)
'''