#Exercicio 36
#um programa para aprovar o empréstimo bancário para a compra de uma casa. 
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
'''
casa = float(input('Valor da casa: $\n'))
salario = float(input('Valor do salario do comprador: \n$'))
anos = int(input('Tempo do financiamento: \n'))
prestacao = casa /(anos *12)
minimo = salario *30 / 100
print('A casa no valor {:.2f} em {} anos'.format(casa, anos), end='')
print(' será no valor de {:.2f} a prestação'.format(prestacao))
if prestacao <= minimo:
    print('Emprestimo APROVADO!')
else:
    print('Emprestimo REPROVADO')
'''
#Exercicio 37
#Escreva um programa em Python que leia um número inteiro qualquer 
# e peça para o usuário escolher qual será a base de conversão: 
# 1 para binário, 2 para octal e 3 para hexadecimal.
'''
import emoji
cores = {'limpa': '\033[m',
         'azul': '\033[01;34;40m',
         'amarelo': '\033[01;33;40m',
         'vermelho': '\033[04;31m'}

num = int(input('Digite um numero: \n'))
print('Escolha uma das bases para conversão: 
         [1]Binario
         [2]Octal
         [3]Hexadecimal') # Coloque as 3 aspas no print, pois o texto e longo
         
menu = int(input('Opção: '))
if (menu == 1):
    print('{} em binario será {}{}{}'.format(num, cores['amarelo'], bin(num), cores['limpa']))
elif menu == 2:
    print('{} em octal será {}{}{}'.format(num, cores['azul'], oct(num), cores['limpa']))
elif menu == 3:
    print('{} em hexadecimal será {}{}{}'.format(num, cores['vermelho'], hex(num), cores['limpa']))
else:
    print(emoji.emojize('Opção errada, tenta de novo, mané! :dedo_do_meio:', language='pt'))
'''
# Exercicio 38
# Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
#– O primeiro valor é maior
#– O segundo valor é maior
#– Não existe valor maior, os dois são iguais
'''
n1 = int(input('Digite o primeiro numero: \n'))
n2 = int(input('Digite o segundo numero: \n'))
if n1 > n2:
    print(emoji.emojize('{} é \033[01;34;40m maior \033[m que {}, lamento :mulher_dando_de_ombros:'.format(n1,n2), language='pt'))
elif n1 < n2:
    print(emoji.emojize('{} é \033[01;34;40m menor \033[m que {}, foi mal :olhos:'.format(n1,n2), language='pt'))
else:
    print(emoji.emojize('{} é \033[01;33;40m igual \033[m que {}, srsrsr... \U0001f92d'.format(n1,n2), language='pt'))
'''
# Exercicio 39
# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, 
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''
from datetime import date
atual = date.today().year # qual o ano atual que esta usando o programa
nasc = int(input('Digite o ano de nascimento: '))
sexo = str(input('Qual o seu genero: '))
idade = atual - nasc
print('Os nascidos em \033[01;32;40m{}\033[m possui \033[01;33m{}\033[m em \033[01;34;40m{}\033[m'.format(nasc, idade, atual))
if sexo == 'F' or sexo == 'feminino':
    print(emoji.emojize('Alistamento não é obrigatório \U0001f485', language= 'pt'))
elif sexo == 'M' or sexo == 'masculino':
    if idade == 18:
        print(emoji.emoji('Você esta na idade do alistamento. :soldado:', language='pt'))
    elif idade < 18:
        saldo = 18 - idade
        print(emoji.emojize('Você ainda não pode se alistar. \U0001f609', language= 'pt'))
        print('Falta \033[01;31;40m{}\033[m anos para se formar'.format(saldo))
        temp = atual + saldo
        print('Volte em \033[01;36;40m{}\033[m.'.format(temp))
    elif idade > 18:
        print(emoji.emojize('Você passou da idade de alistar. \U0001f936'))
        saldo = idade -18
        print('Deveria ter se alistado há \033[01;35;40m{}\033[m anos.'.format(saldo))
else:
    print('Precisa de avaliação fisica.')
''' 
# Exercicio 40
# Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida.
'''
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1+n2)/2
print("1' nota é {:.1f} \n2' nota é {:.1f}".format(n1, n2))
print("então sua media é \033[01;36;40m{:.1f}\033[m".format(media))
if 7 > media >= 5: #pode-se usar esse metodo, ou o normal(media >=5 or media < 7)
    print(emoji.emojize('Esta em Recuperação, se vira! :esmalte_de_unha:', language= 'pt'))
elif media < 5:
    print(emoji.emojize('Esta REPROVADO, \033[01;35;40mhuhahahahaha, se lascou!\033[m \U0001f608'))
else:
    print(emoji.emojize('Esta APROVADO, rapa fora daqui!:yawning_face:'))
'''
# Exercicio 41
# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, 
# de acordo com a idade:
#– Até 9 anos: MIRIM
#– Até 14 anos: INFANTIL
#– Até 19 anos: JÚNIOR
#– Até 25 anos: SÊNIOR
#– Acima de 25 anos: MASTER
'''
from emoji import emojize #import a biblioteca de emojis
from datetime import date #import da biblioteca de calendario
ano = int(input("Digite o ano de nascimento: "))
atual = date.today().year #importe para trazer o ano atual 
idade = atual - ano
print('Você possui \033[01;33;40m{}\033[m anos.'.format(idade))
#Formas diferentes de apresentar as variações de idade
if idade <= 9:
    print(emojize('Esta na categoria: MIRIM. :bebê:', language= 'pt'))
elif 9 > idade <= 14: #recomendo usar essa
    print(emojize('Esta na categoria: INFANTIL :criança:', language= 'pt'))
elif  idade > 14 and idade <= 19:
    print(emojize('Esta na categoria: JÚNIOR :person:'))
elif idade <= 25: # idade > 19 and idade <= 25 (sendo essa a mais simples)
    print(emojize('Esta na categoria: SÊNIOR \U0001f9d4'))
else:
    print(emojize('Esta na categoria: MASTER :older_person:'))
'''
# Exercicio 42
# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#– EQUILÁTERO: todos os lados iguais
#– ISÓSCELES: dois lados iguais, um diferente
#– ESCALENO: todos os lados diferentes
'''
from emoji import emojize
print('=-='*20)
r1 = float(input('Digite um lado do triangulo: '))
r2 = float(input('Digite outro segmento do triagulo: '))
r3 = float(input('Dogite o ultomo segmento do triagulo: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print(emojize(':rosto_com_a_mão_sobre_a_boca:'*20, language= 'pt'))
    print('Os segmentos acima PODEM se tornar um triângulo', end=' ')
    if r1 == r2 == r3: # forma tradicional(r1 == r2 and r2==r3)
        print('\033[4;32mEQUILATERO\033[m')
    elif r1 != r2 !=r3 != r1: #forma tradicional (r1 != r2 and r2 != r3 and r1 != r3)
        print('\033[1;32mESCALENO\033[m')
    else:
        print('\033[1;32mISÓSCELES\033[3m')
else:
    print(emojize(':rosto_deprimido:', language= 'pt'))
    print('Os segmentos acima NÃO PODEM ser tornar um triângulo')
print('=='*20)
'''
# Exrcicio 43
# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, 
# calcule seu Índice de Massa Corporal (IMC) e mostre seu status, 
# de acordo com a tabela abaixo:
#– IMC abaixo de 18,5: Abaixo do Peso
#– Entre 18,5 e 25: Peso Ideal
#– 25 até 30: Sobrepeso
#– 30 até 40: Obesidade
#– Acima de 40: Obesidade Mórbida
'''
from emoji import emojize
print('=='*30)
peso = float(input('Qual seu peso (Kg): '))
altura = float(input("Qual a sua altura (m): "))
imc = peso / (altura ** 2) #(pow(altura))
print('O seu IMC é : {:.1f}'.format(imc))
if imc < 18.5:
    print(emojize('Você está abaixo do peso :papel:',language= 'pt'))
elif imc > 18.5 and imc < 25:
    print(emojize('Você está com peso ideal. thumbsup'))
elif 25 <= imc < 30:
    print(emojize('Você está com sobrepeso \U0001f62c'))
elif 30 <= imc < 40:
    print(emojize('Você esta com obesidade :rosto_gritando_de_medo:', language= 'pt'))
elif imc >= 40:
    print(emojize('Você está com Obesidade Morbida ghost'))
'''
# Exercicio 44
# Elabore um programa que calcule o valor a ser pago por um produto, 
# considerando o seu preço normal e condição de pagamento:
#– à vista dinheiro/cheque: 10% de desconto
#– à vista no cartão: 5% de desconto
#– em até 2x no cartão: preço formal 
#– 3x ou mais no cartão: 20% de juros
'''
print('==='*20)
valor = float(input('Qual valor gasto: R$'))
print(''Escolha a forma de pagamento:
      \033[1;33m[1]\033[m Á vista/debito/pix
      \033[1;33m[2]\033[m Cartão de credito avista (1x)
      \033[1;33m[3]\033[m Cartão de credito 2x
      \033[1;33m[4]\033[m Cartão de credito 3x ou mais
      '') #coloca as tres aspas aqui
opcao = int(input('Opção: '))
if opcao == 1:
    total = valor - (valor * 10/100)    
elif opcao == 2:
    total = valor - (valor * 5 / 100)
elif opcao == 3:
    total = valor
    parcela = total / 2
    print('Valor da compra parcelada em 2 x será \033[1;35mR${:.2f}\033[m'.format(parcela))
elif opcao == 4:
    total = valor + (valor * 20 / 100)
    totparcel = int(input('Quantas parcelas: '))
    parcela = total / totparcel
    print('Valor da compra parcelada em {}x será \033[1;35mR${:.2f}\033[m com juros.'.format(totparcel, parcela))
else:
    total = 0
    print("\033[4;31m Opção errada, tenta de novo! \033[m")
print('O valor pago de R${:.2f}, a vista será \033[1;32mR${:.2f}\033[m.'.format(valor,total))   
print('==='*20)
'''
# Exercicio 45
# Crie um programa que faça o computador jogar Jokenpô com você.
from emoji import emojize
from random import randint
from time import sleep
print('----------- Jo Ken Pô -----------')
print(emojize('---------:mão_levantada: -- :saudação_vulcana: -- :soco: ---------', language='pt'))
print('''      \033[1;36m[0]\033[m Pedra
      \033[1;36m[1]\033[m Papel
      \033[1;36m[2]\033[m Tesoura''')
itens= ('Pedra', 'Papel', 'Tesoura')
pc = randint(0,2)
jogador = int(input('Qual a sua jogada? '))
print('JO...')
sleep(1) # atraso de 1 segundo o proximo comando (no caso o print)
print('KEN...')
sleep(1)
print('PÔ!!!')
print('Você jogou \033[1;32m{}\033[m e eu joguei \033[1;33m{}\033[m'.format(itens[jogador], itens[pc]))
if pc == 0: # pc jogou pedra
    if jogador == 0:
        print(emojize('Empate :rosto_dormindo:', language='pt'))
    elif jogador == 1:
        print(emojize('Você venceu :mãos_para_cima:', language='pt'))
    elif jogador == 2:
        print(emojize('Você perdeu :bíceps:',language='pt'))
    else:
        print(emojize('\033[1;35mJogada errada, tenta denovo\033[m :polegar_para_baixo:', language = 'pt'))
    
elif pc == 1: # pc jogou papel
    if jogador == 0:
         print(emojize('Você perdeu :bíceps:',language='pt'))
    elif jogador == 1:
         print(emojize('Empate :rosto_bocejando:', language='pt'))
    elif jogador == 2:
         print(emojize('Você venceu :mãos_para_cima:', language='pt'))
    else:
        print(emojize('\033[1;35mJogada errada, tenta denovo\033[m :polegar_para_baixo:', language = 'pt'))
    
elif pc == 2: # pc jogou tesoura
    if jogador == 0:
         print(emojize('Você venceu :mãos_para_cima:', language='pt'))
    elif jogador == 1:
        print(emojize('Você perdeu :bíceps:',language='pt'))
    elif jogador == 2:
        print(emojize('Empate :cansado:', language='pt'))
    else:
        print(emojize('\033[1;35mJogada errada, tenta denovo\033[m :polegar_para_baixo:', language = 'pt'))
print('==='*20)