# Exercicio 46
# Faça um programa que mostre na tela uma contagem regressiva para 
# o estouro de fogos de artifício, indo de 10 até 0, 
# com uma pausa de 1 segundo entre eles.
'''
import os, time
from emoji import emojize
print(emojize('**************:brilhos: \033[4;32m Hora dos fogos\033[m :brilhos:**************',language = 'pt'))
for x in range (10, -1, -1):
    print(x)
    time.sleep(0.5)
    
# Animação de fogos de artificio   
os.system('cls') # linus - 'clear'
filenames = ["fogo1.txt", "fogo2.txt", "fogo3.txt", "fogo4.txt","fogo5.txt"]
frames = []
def animation (filenames, delay= 0.5, repeat = 10):
    for name in filenames:
        with open(name, 'r', encoding='utf8') as f:
            frames.append(f.readlines())
    for i in range (3):
        for frame in frames:
            print(''.join(frame))
            time.sleep(0.5)
            os.system('cls')
animation(filenames, delay= 0.2, repeat= 2)        
print(emojize('Eeeeeeeee!!!!... \U0001f64c'))
'''
# Exercicio 47
# Crie um programa que mostre na tela todos os números pares que estão 
# no intervalo entre 1 e 50. 
'''
print('***'*10)
for x in range(0, 51): # esse realiza a repetição completa
    if x % 2 ==0:
        print(x, end=' ')
#ou pode -se ser feito dessa forma
print('--'*20)
for i in range(2, 51, 2): # sendo essa preferencial, pois usa metade de repetições necessario
    print(i, end=' ')
'''
# Exercicio 48
# Faça um programa que calcule a soma entre todos os números que 
# são múltiplos de três e que se encontram no intervalo de 1 até 500.
'''
print('**'*20)
s = 0
count = 0
for i in range(1, 501, 2):
    if i %3 == 0:
        count = count + 1
        s +=i # ou s = s+ i
print('A soma de todos os \033[1;36m{}\033[m valores, multiplos de 3, ate 500, é \033[1;33m{}\033[m'.format(count, s))
'''
# Exercicio 49
# Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher,
# só que agora utilizando um laço for.
'''
print('=='*20)
num = int(input('Digite um numero: \n'))
for i in range (1, 11):
    print("{} x {:2} = {}".format(num, i , num*i))
print('=='*20)
'''
# Exercicio 50
# Desenvolva um programa que leia seis números inteiros
# e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o.
'''
print('=='*20)
s = 0
count = 0
for x in range(1,7):
    n = int(input('Digite {} numero: \n'.format(x)))
    if n % 2 == 0:
        s = s + n
        count += 1
    else:
        print('O numero não é par, não pode ser somado')
print('A soma dos {} numeros pares sera {}'.format(count, s))
'''
# Exercicio 51
# Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.
'''
print('=='*20)
print('=============== \033[1;31mPROGRESSÃO ARITMETICA\033[m ===============')
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
decimo = primeiro + (10 - 1 ) * razao # formula o enezimo termo da PA
for c in range(primeiro, decimo + razao, razao):
    print('{}'.format(c), end=' → ')
print('fim')
print('=='*20)
'''
# Exercicio 52
# Faça um programa que leia um número inteiro
# e diga se ele é ou não um número primo.
'''
print('=='*20)
n = int(input('Digite um numero: '))
tot = 0
for i in range (1, n+1):
    if n % i == 0:
        print('\033[m', end=' ')
        tot +=1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(i), end=' ')
print('\n{} foi divisivel {} vezes'.format(n, tot))
if tot == 2:
    print('Então ele é PRIMO')
else:
    print('Então ele NÃO É PRIMO')
print('=='*20)
'''
# Exercicio 53
# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
# desconsiderando os espaços. Exemplos de palíndromos:
# APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.
'''
frase = str(input('Digite uma frase: \n')).strip().upper() 
# strip()-Conta quantos caracteres possui, sem os espaços extras
# upper()-Torna todas as letras em maiusculas
palavras = frase.split()
# split()-Divide os espaços entre palavras, criando assim uma lista de palavras, um vetor
junto = ''.join(palavras)
# Join()- Une as palavras transformando os espaços em outros caracteres, ou ignorando o mesmo
inverso = ''
for letra in range (len(junto) - 1, -1, -1): # Ira ler todas as letras menos uma, lendo a primeira letra, voltando uma letra
    inverso += junto[letra]
# ou pode ser feito assim
invertido = junto [::-1] # no lugar do for
print(inverso)
if inverso == junto:
    print('Temos um palíndromo')
else:
    print('Não é um palíndromo')
'''
# Exercicio 54
# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
'''
from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for p in range (1, 8):
    nasc = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(p)))
    idade = atual - nasc
    if idade >= 21:
        totmaior +=1
    else: 
        totmenor +=1
print('Foram {} pessoas\033[31m maiores\033[m de idade'.format(totmaior))
print('Foram {} pessoas\033[36m menores\033[m de idade'.format(totmenor))
'''
# Exercicio 55
# Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.
'''
menor = 0
maior = 0
for i in range (1, 6):
    peso = float(input('digite o {}° peso: '.format(i)))
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso é \033[33m{}kg\033[m, e o menor peso é \033[34m{}kg\033[m'.format(maior, menor))
'''
# Exercicio 56
# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre:
# a média de idade do grupo,
# qual é o nome do homem mais velho e
# quantas mulheres têm menos de 20 anos.
somaidade = 0
mediaidade = 0
maioridade = 0
nomevelho = ''
totmulher20 = 0
for p in range (1, 5):
    print('------- {}° pessoa -------'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [F/M]: ')).strip() 
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridade = idade
        nomevelho  = nome
    if sexo in 'Mm' and idade > maioridade:
        maioridade = idade 
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
mediaidade = somaidade / 4 
print('='*20)
print('A media de idade do grupo de pessoas é {} anos'.format(mediaidade))
print('O homem mais velho do grupo tem {} anos, e se chama {}'.format(maioridade, nomevelho))
print('Total de mulheres menores de 20 anos é {}'.format(totmulher20))
