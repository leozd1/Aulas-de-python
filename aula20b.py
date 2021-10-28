# Exercicio 96
# Faça um programa que tenha uma função chamada área(),
# que receba as dimensões de um terreno retangular
# (largura e comprimento) e mostre a área do terreno.
# Função da área
'''
def area (larg, comp):
    a = larg * comp
    print(f'A área do terreno de {larg} x {comp} mede {a} m²')

#programa principal
print('Controle de Terrenos')
print('-'*30)
l = float(input('LARGURA DO TERRENO (m): '))
c= float(input('COMPRIMENTO DO TERRENO (m): '))
area(l, c)
'''
# Exercicio 97
# Faça um programa que tenha uma função chamada escreva(),
# que receba um texto qualquer como parâmetro
# e mostre uma mensagem com tamanho adaptável.
# Ex:    
# escreva(‘Olá, Mundo!’)
# Saída:
# ~~~~~~~~~~~~ 
# Olá, Mundo!   
# ~~~~~~~~~~~~  
'''
def escreva (msn): # o paramentro sera a mensagem chamada
    tam = len(msn) + 4 # lerá o tamanho da escrita da mensagem mas 4 espaços
    print('\033[1;31m~\033[m'*tam)
    print(f'  {msn}') # pra centralizar, da 2 espaços
    print('\033[1;31m~\033[m'*tam)

#principal
escreva(input('Escreva ai qualquer coisa: '))
''' 
# Exercicio 98
# Faça um programa que tenha uma função chamada contador(),
# que receba três parâmetros: início, fim e passo.
# Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1    
# b) de 10 até 0, de 2 em 2      
# c) uma contagem personalizada
'''
from time import sleep
def escreva (msn): # pode ser colocado dentro de outra função, contando que fique no lugar do print
    tam = len(msn) + 4
    print('\033[1;32m~\033[m'*tam)
    print(f'  {msn}') 
    print('\033[1;32m~\033[m'*tam)

def contador(inicio, fim, passo):
    if passo < 0: # casso o passo seje negativo, transforma-o em positivo
        passo *= -1
    if passo == 0: # caso o passo seje igual a zero, conta como fosse 1
        passo = 1
    escreva(f'Contagem de {inicio} ate o {fim} de {passo} em {passo}') # parece que pode-se colocar uma função dentro de outra (¬_¬)
    
    if inicio < fim: # caso o inicio seja maior que o fim
        sleep(1.5)
        cont = inicio
        while cont <= fim:
            print(f'{cont}', end=' ', flush= True) # o flush(), caso de um Buff de tela( de pausa no programa e depois mostre tudo)
            sleep(0.5)
            cont += passo
        print('> FIM!')
    else:
        sleep(2) # só pra da tempo de ler o enunciado antes da contagem
        cont = inicio
        while cont >= fim: # caso o fim seje maior que o inicio
            print(f'  {cont}', end=' ') # So dei 2 espaço pra alinhar com a função escreva()
            sleep(0.5)
            cont -= passo
        print('> FIM')
    print('='*30)
# principal programa
contador(1,10,1)
contador(10,0,2)
escreva('Sua vez de escrever a forma de contar: ')
ini = int(input('Inicio: '))
fin = int(input('Fim:    '))
pas = int(input('Passo:  '))
contador(ini, fin, pas)
'''
# Exercicio 99
# Faça um programa que tenha uma função chamada maior(),
# que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
'''
from time import sleep
def escreva (msn): 
    tam = len(msn) + 4
    print('\033[1;32m~\033[m'*tam)
    print(f'  {msn}') 
    print('\033[1;32m~\033[m'*tam)
    
def maior(*num): # o * serve para desempacotar a quantidade varialvel de parametros recebidos pela função
    cont = maior = 0
    escreva(f'Analisando os valores... Aguarde...')
    for valor in num:
        print(f'{valor}', end=' ')
        sleep(0.5)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont +=1
    print() # quebra de linha 
    sleep(1)
    escreva(f'Foram informados {cont} valores ao todo.')
    sleep(1.5)
    print(f'O maior valor é {maior}.')
    
# programa principal
maior(4,2,8,3,1,0)
maior(6,2,8,0,)
maior(1,5)
maior(5)
'''
# Exercicico 100
# Faça um programa que tenha uma lista chamada números 
# e duas funções chamadas sorteia() e somaPar(). 
# A primeira função vai sortear 5 números
# e vai colocá-los dentro da lista
# e a segunda função vai mostrar a soma
# entre todos os valores pares sorteados pela função anterior.
'''
import random # para sortear os numeros
import emoji
from time import sleep
def escreva (msn): 
    tam = len(msn) + 4
    print('\033[1;36m~\033[m'*tam)
    print(f'  {msn}') 
    print('\033[1;36m~\033[m'*tam)
 
def sorteio(lista):
    escreva('Sorteando 5 numeros da lista: ')
    for cont in range(0,5):
        n = random.randint(1,10)
        lista.append(n)
        print(f'{n} ', end=' ')
        sleep(0.4)
    print('PRONTO!')
            
def somaPar(lista):
    soma = 0 
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    escreva(f'Somando os valores pares de {lista} temos: {soma}')

# programa
num = []
sorteio(num)
somaPar(num)
print(num) # ao que parece a função escreva, não funciona bem com listas ou similares
'''
