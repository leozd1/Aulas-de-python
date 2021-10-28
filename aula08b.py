#Exercicio 16
# Crie um programa que leia um número Real qualquer pelo teclado e 
# mostre na tela a sua porção Inteira.
'''
x = float(input("Digite um numero: "))
print("A porção inteira de {} é {}".format(x, int(x))) #As vezes não precisa importar modulos
'''
'''
import math #import math, tras todos os comandos da biblioteca math
num = float(input("Digite um numero: "))
print("A porção inteira de {} é {}".format(num, math.trunc(num)))
'''
'''
from math import floor #a from permite especificar qual comando trazer da biblioteca,
#use virgula para separar mais de um comando
n = float(input("Digite um numero: "))
print("A porção inteira de {} é {}".format(n,floor(n)))
'''
#Exercicio 17
# leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. 
# Calcule e mostre o comprimento da hipotenusa
#modelo matematico tradicional
'''
catosp = float(input("Digite o comprimento do cateto oposto: "))
catadj = float(input("Digite o comprimento do cateto adjacente: "))
hip = (catosp ** 2 + catadj ** 2 ) ** (1/2) 
print ("A hipotenusa é {:.2f}".format(hip))
'''
#modelo math
'''
import math
co = float(input("Digite o comprimento do cateto oposto: "))
ca = float(input("Digite o comprimento do cateto adjacente: "))
hi = math.hypot(co, ca)
print("A hipotenusa é {:.2f}".format(hi))
'''
#Exercicio 18
# Seno, Cosseno e Tangente
'''
from math import radians, cos, sin, tan
an = float(input("Digite o valor do angulo desejado? "))
sen = sin(radians(an))
cos = cos(radians(an))
tan = tan(radians(an))
print("O angulo de {:.2f} terá o: \nseno de: {:.2f} \ncosseno de {:.2f} \ntangente de {:.2f}".format(an, sen,cos,tan))
'''
#Exercicio 19
# Sorteio de numeros 
'''
import random
n1 = str(input("Digite o 1 nome: "))
n2 = str(input("Digite o 2 nome: "))
n3 = str(input("Digite o 3 nome: "))
n4 = str(input("Digite o 4 nome: "))
lista = [n1, n2, n3, n4] 
escolha = random.choice(lista)
print("="*20)
print("Nome escolhido é {}".format(escolha))
'''
#Exercicio 20
# Sorteio de ordem escolhida
'''
from random import shuffle
n1 = str(input("Digite o 1 nome: "))
n2 = str(input("Digite o 2 nome: "))
n3 = str(input("Digite o 3 nome: "))
n4 = str(input("Digite o 4 nome: "))
lista = [n1, n2, n3, n4]
shuffle(lista)
print(" A ordem de nomes é: ")
print(lista)
'''
#Exercicio 21
# Reproduzir MP3 ou musica
# Importando a biblioteca do pygame: python -m pip install pygame ou pip install pygame

import pygame
'''
pygame.init()
#pygame.mixer.init()
#pygame.mixer.music.load('overlap') #Yugioh Opp 5 OVERLAP - YGO Synchro BR.mp3
pygame.mixer.music.load('C:\\Users\\leonice.queiroz\\Documents\\overlap2')
pygame.mixer.music.play()
pygame.event.wait()
input('Ouça o som!\n Pressione "Enter" para parar a musica.')
'''
#O playsound parece funcionar melhor que o pygame.mixer.music

import playsound # importanto o playsound: python -m pip install playsound ou pip install playsound
pygame.init()
print('qual musica deseja tocar? ')
print("(1) Yugi oh \n(2)bRockman Zero")
menu = int(input('Opção:'))
if(menu == 1):
    m1 = playsound.playsound('overlap.mp3')
elif(menu == 2):
    m2 = playsound.playsound('RockmanZeroClover.mp3')
else:
    print("Só tenho duas musicas, tente denovo!")    
pygame.event.wait()
input('Ouça o som!\n Pressione "Enter" para parar a musica.')
