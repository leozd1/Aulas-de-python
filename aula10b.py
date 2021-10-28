# Exercicio 28
# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. 
# O programa deverá escrever na tela se o usuário venceu ou perdeu
'''
from random import randint
#import time
from time import sleep # faz o pc esperar, ou dormir, por alguns segundos, antes de continuar
import emoji

pc = randint(0, 5)
print('-=-'*30)
print('Pensei em um numero entre 0 e 5, tente descobrir: ')
num = int(input('digite um numero: ')) 
print('Processando...')
sleep(3)
if num == pc:
    print(emoji.emojize('Acertou miseravi :rosto_abraçando:!  \nvocê: {} \nPC: {}'.format(num, pc),variant= 'emoji_type' ,language='pt'))
else:
    print(emoji.emojize('Errou, John Snow! :face_with_hand_over_mouth: \nvocê: {} \nPC: {}'.format(num, pc), variant= 'emoji_type'))
print('-=-'*30)
'''
# Exercicio 29
#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, 
# mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
'''
import emoji
vel = float(input('Qual a velocidade do carro: '))
if vel > 80:
    print('você foi multado!')
    multa = (vel-80) *7
    print('Valor da multa R$ {:.2f}'.format(multa))
else:
    print(emoji.emojize('Você é um otimo motorista, merece um doce! :pirulito:', language='pt', variant='emoji_type'))
print(emoji.emojize('Tenha um bom dia e dirija com segurança! :carro:', language='pt', variant= 'emoji_type'))
print('-=-'*30)
'''
#Exercicio 30
#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
'''
print('-=-'*30)
num = int(input('Digite um numero: '))
res = num % 2

if res == 1: 
    print('{} é ímpar'.format(num))
else:
    print('{} é par'.format(num))
print('=='*30)
'''
#Exercicio 31
#Desenvolva um programa que pergunte a distância de uma viagem em Km. 
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km 
# e R$0,45 parta viagens mais longas.
'''
dist = float(input('Qual a distâmcia da viagem? '))
if dist <= 200:
    preço = dist * 0.5
else:
    preço = dist * 0.45
print("O valor da passagem sera R${:.2f} para uma viagem de {}km".format(preço, dist))
'''
#Exercicio 32
#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
'''
#import datetime 
from datetime import date #importa biblioteca datetime (calendario)
ano = int(input('Qual ano analisar? \nAperte ZERO para ano atual \n'))
if ano == 0:
    ano = date.today().year # date.today().year (na data de hoje, use o ano)
if ano % 4 == 0 and ano != 100 == 0 or ano % 400 == 0:
    print('{} é ano bissexto'.format(ano))
else:
    print('{} não é bissexto'.format(ano))
'''
#Exercicio 33
#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
'''
x = int(input('Digite o primeiro numero: '))
y = int(input('Digite o segundo numero: '))
z = int(input('digite o terceiro numero: '))
# teste do maior
if x > y and x > z:
    maior = x
if y > x and y > z:
    maior = y
if z > x and z > y:
    maior = z
# ou pode simplificar dessa forma:
# teste do maior
menor = x
if y < x and y < z:
    menor = y
if z < x and z < y:
    menor = z
print('\nMaior valor digitado é: {} \nMenor valor digitado é {}'.format(maior, menor))
'''
#Exercicio 34
#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
# Para salários superiores a R$1250,00, 
# calcule um aumento de 10%. 
# Para os inferiores ou iguais, o aumento é de 15%.
'''
sal = float(input('Qual o salário do funcionário? '))

if sal <= 1250:
    novo = sal + (sal * 15/100) 
else:
    novo = sal + (sal *10 / 100)
    
print('Ao funcionario que ganhava {}, passa a ganhar {}'.format(sal, novo))
'''
#Exercicio 35
# Desenvolva um programa que leia o comprimento de três retas
# e diga ao usuário se elas podem ou não formar um triângulo.
print('=-='*20)
r1 = float(input('Digite o primeiro segmento: '))
r2 = float(input('Digite o segundo segmento: '))
r3 = float(input('Digite o terceiro segmento: \n'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM se tornar um triângulo')
else: 
    print('Os segmentos acima NÃO PODEM ser tornar um triângulo')