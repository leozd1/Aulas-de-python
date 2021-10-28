# Exercicio 72
# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
'''
from emoji import emojize
print(f'\033[1;36m~~\033[m'*30)
res = 's' # inicializador
cont = ('zero','um', 'dois', 'três', 'quatro', 'cinco',
        'seis','sete','oito','nove','dez','onze', 'doze', 'treze',
        'quatorze','quinze', 'dezeseis','dezesete','dezoito', 'dezenove','vinte')
while res in 'Ss': # se não for o resposta certa ele ira repetir a pergunta
    while True:
        n = int(input("Digite um numero de 0 a 20: \n"))
        if 0 <= n <= 20:
            break
        print(emojize('tente novamente :rosto_de_palhaço:', language= 'pt'), end=' \n')
    res = str(input(emojize('Deseja continuar?[S/N] :rosto_bocejando:\n', language='pt'))).upper().strip()[0]
print(f'Você digitou o numero \033[1;30;47m{cont[n]}\033[m')       
print(f'\033[1;36m~~\033[m'*30)
'''
# OBS.: a resposta acima foi feita com desafio  
# Exercicio 73
# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação.
# Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.
'''
times = ('América-MG','Athletico','Atlético-GO','Atlético-MG','Bahia','Bragantino','Ceará','Chapecoense',
         'Corinthians','Cuiabá','Fortaleza','Flamengo','Fluminense','Grêmio', 'Internacional','Juventude',
         'Palmeiras', 'Santos','São Paulo','Sport')
print('-='*30)
print(f'Lista de times: {times}')
print('-='*30)
print(f'Os 05 primeiros colocados são {times[0:5]}')
print('-='*30)
print(f'Os ultimos 4 foram {times[-4:]}')
print('-='*30)
print(f'times em ordem alfabetica é: \n{sorted(times)}')
print('-='*30)
print('O Chapecoense esta em {}° posição'.format(times.index('Chapecoense'))) # atentar pra formatação, pois o excesso de aspas('') atrapalha
                                                                              # pode usar o .format() ou aspas duplas("")
'''
# Exercicio 74
# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados
# e também indique o menor e o maior valor que estão na tupla.
'''
from random import randint
n  = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
print('O valores sorteados são: ')
for num in n:
    print(f'{num}',end=' ')
print(f'\nO Maior numero é \033[1;36m{max(n)}\033[m') # metodo(especifico para tuplas) max() que permite verifica o maior valor da tupla
print(f'O menor numero é \033[1;34m{min(n)}\033[m') # o mesmo, so que verifica o menor valor
'''
# Exercicio 75
# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
# No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.
'''
n = (int(input('Digite um numero: ')),
    int(input('Digite mais um numero: ')),
    int(input('Digite mais outro numero: ')),
    int(input('Digite ultimo numero: ')))
print(f'Você digitou os numeros: {n}')
print(f'O numero 9 apareceu {n.count(9)} vez')
if 3 in n: # for é usado para corrigir um erro de logica (o que acontece se não tiver o valor digitado?)
    print(f'o numero 3 foi digitado na posição {n.index(3)+1}º') # .index()+1 verifica o index(posição) do valor
else:
    print('o numero 3 não foi digitado')
print(f'Os numero pares digitados foram: ',end='')
for nu in n: # infelizmente não existe outra forma de verificar numeros pares
    if nu % 2 == 0:
        print(nu, end=' ')
'''
# Exercicio 76
# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços,
# na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.
'''
from time import sleep
from emoji import emojize
lista = ('batata', 3.4,
         'tomate', 4.50,
         'alho', 22.3,
         'alface', 3.35,
         'couve', 4.45,
         'pepino', 4,
         'pimentão', 2.25)
print('='*40)
print(emojize(f'\033[1;35;40m:saco_de_dinheiro:{"SACOLÃO EM PROMOÇÃO":^35}:saco_de_dinheiro:\033[m', language='pt'))
print('='*40) # coloca aspas duplas dentro das aspas simples para reconhecer os caracteres
for lis in range (0, len(lista)): # o len() é usado um for para organizar a listagem
    sleep(0.5) # só coloquei pra dar efeito "eletrônico"
    if lis % 2 == 0: # percebe-se que os nomes sao pares ( começando com [0]), e os preços são impares
        print(f'{lista[lis]:.<30}',end='') # formata-se a lista com pontos a 30 caracteres
    else:
        print(f'\033[1;32;40mR$ {lista[lis]:>.2f}\033[m') # não esqueça das casas decimais para preços (.2f)
print('-'*40)
'''
# Exercicico 77
# Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
'''
print('-'*40)
palavras = (str(input('Digite suas palavras, sem acento: ')),
            str(input('Digite mais palavras, sem acento: ')),
            str(input('Digite outra palavras, sem acento: ')),
            str(input('Digite ultimas palavras, sem acento: ')))
print('-'*40)
for p in palavras: # 'para cada p em palavras, mostre as palavras p maiusculas
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p: # onde cada letra em p, mostre as letras em minuscula
        if letra.lower() in 'aeiou': # para sulucionar o caso dos acentos, é so adicionar letras com acento no in do if.
            print(letra.lower(), end=' ') # o .lower() pode ser colocaro no if, mas ele fica melhor no print
print('-'*40)
'''