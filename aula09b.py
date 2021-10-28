#Exercício 22
# Crie um programa que leia o nome completo de uma pessoa e mostre:
#– O nome com todas as letras maiúsculas e minúsculas.
#– Quantas letras ao todo (sem considerar espaços).
#– Quantas letras tem o primeiro nome.
'''
nome = str(input('Digite seu nome: ')).strip()
print('analisando nome...')
print('='*20)
print('Seu nome em maiusculo fica {}.'.format(nome.upper()))
print('Seu nome em minusculo fica {}.'.format(nome.lower()))
print('O nome todo tem {} letras.' .format(len(nome)-nome.count(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e tem {} letras'.format(separa[0], len(separa[0])))
'''
#Exercicio 23
# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
'''
nu = int(input('digite um numero: '))
u = nu //1 % 10
d = nu //10 % 10
c = nu // 100 % 10
m = nu // 1000 %10
print('='*20)
print('analisando numero {}...'.format(nu))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
'''

#Exercicio 24
# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome “SANTO”
'''
cid = str(input('Qual a cidade que você nasceu? ')).strip()
print('='*20)
print('sua cidade tem Santo no nome?')
print(cid[:5].upper() == 'SANTO')
'''

#Exercicio 25
# Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.
'''
nome = str(input('Qual seu nome completo?')).strip()
print('='*20)
print('Seu nome tem silva? {}'.format("silva" in nome.lower()))
'''

#Exercicio 26
# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, 
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
'''
frase = str(input("Digite uma frase: ")).lower().strip()
print('='*30)
print('A letra A apareceu {} vezes'.format(frase.count('a')))
print('A letra A apareceu na posição {}'.format(frase.find('a')+1))
print('A letra A apareceu na posição {} uma ultima vez.'.format(frase.rfind('a')+1))
'''

#Exercicio 27
# Faça um programa que leia o nome completo de uma pessoa, 
# mostrando em seguida o primeiro e o último nome separadamente. 
nome = str(input("Digite nome: ")).strip()
n = nome.split()
print('='*30)
print('Prazer em te conhecer, ')
print('Seu primerio nome é {}'.format(n[0]))
print('Seu ultimo nome é {}'.format(n[len(n)-1]))