# Exercicio 66
# Crie um programa que leia números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999,
# que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).
'''
print('~~'*30)
n = s = 0
while n != 999:
    n = int(input('Digite um número (999 para parar): '))
    s += n
s -= 999 # gambiarra usada para tirar o 999
print(f'A soma dos valores digitados foi {s}')
'''
'''
n= s = cont = 0
while True:
    n = int(input('Digite um número (999 para parar): '))
    if n == 999: # antes de somar os numeros, verifica se o numero e igual ao 999
        break
    cont += 1 # Não concidera o flag(loop) na somatoria
    s += n
print(f'A soma dos {cont} valores digitados foi {s}')
print('Acabou.')
'''
# Exercicio 67
# Faça um programa que mostre a tabuada de vários números, um de cada vez,
# para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo. 
'''
while True:
    n = int(input('Qual tabuada deseja ver? '))
    print('-'*40)
    if n < 0: # colocado ai, pois verifica depois da leitura do numero (preste atenção na logica)
        break
    for c in range (1, 11): # for é melhor para tabuadas 
        print(f'\033[1;31m{n}\033[m x \033[1;32m{c}\033[m = \033[4;35m{n * c}\033[m') # n para numero, c pra contador, numero x contador
    print('\033[1;36m~\033[m'*40)
print('Acabou')
'''
# Exercicio 68
# Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo. 
'''
print(f'\033[1;36m~~\033[m'*30)
from random import randint
v = 0
while True:
    jog = int(input('Digite um valor: '))
    pc = randint(0, 11)
    total = jog + pc
    tipo = ' '
    while tipo not in 'PI': # tipo não for P ou I, ele repete as pergunta
        tipo = str(input('deseja ser par ou Impar: [P/I]')).strip().upper()[0] # jogou tudo pra maiusculo e so considera a primeira letra    
    print(f'Você jogou {jog} e o computador {pc}, num total de {total} de vezes. ', end= '')
    print('Deu par' if total % 2 == 0 else "Deu impar")
    if tipo  == 'P':
        if total % 2 == 0:
            print('\033[1;32m Voce venceu!\033[m')
            v += 1
        else: 
            print('\033[1;31m Voce perdeu\033[m!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('\033[1;32m Voce venceu\033[1;m!')
            v +=1
        else:
            print('\033[1;31m Voce Perdeu\033[m!')
            break
    print('Vamos jogar novamente...')
print(f'\033[1;36mGAME OVER!!!\033[m Você venceu \033[1;34m{v}\033[m vezes')
print(f'\033[1;36m~~\033[m'*30)
'''
# Exercicio 69
# Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
# No final, mostre: 
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos. 
'''
from emoji import emojize
print(f'\033[1;36m~~\033[m'*30)
res = 'S'
soma = M = F = 0
while res in 'S':
    print('\033[1;34m==\033[m'*20)
    print('CADASTRO PESSOA')
    print('\033[1;34m==\033[m'*20)
    idade = int(input("Digite a idade: "))
    sexo = str(input("Digite o sexo da pessoa:[F/M] ")).upper().strip()[0]
    if sexo == "M":
        M += 1
    elif sexo == 'F':
        if idade <= 20:
            F += 1
    if idade >= 18:
        soma += 1
    res = str(input(emojize('Deseja continuar?[S/N] :rosto_bocejando:', language='pt'))).upper().strip()[0]
print(f'Total de pessoas maiores de 18 é {soma}')
print(emojize(f'Total de homens é \033[1;34m{M}\033[m :man:'))
print(emojize(f'Total de mulheres menores de 20 anos é \033[1;35m{F}\033[m :woman:'))
'''
# Resposta do exercicio
'''
from emoji import emojize
print(f'\033[1;36m~~\033[m'*30)
tot18 = M = F = 0
while True: # tente usar com o break para parar o while infinito (true)
    idade = int(input("Digite a idade: "))
    sexo = ' '
    while sexo not in 'FM': # se não for o FM ele ira repetir a pergunta
        sexo = str(input("Digite o sexo da pessoa:[F/M] ")).upper().strip()[0]
    if idade >= 10:
        tot18 += 1
    if sexo == "M":
        M += 1
    elif sexo == 'F' and idade < 20: # não esqueça as logicas 
        F += 1
    res = ' ' # inicializador
    while res not in 'SN': # se não for o resposta certa ele ira repetir a pergunta
        res = str(input(emojize('Deseja continuar?[S/N] :rosto_bocejando:', language='pt'))).upper().strip()[0]
    if res == 'N': # o if do break tem que esta fora da identação do while
            break 
print('\033[1;34m**\033[m'*20)
print(f'Total de pessoas maiores de 18 é {tot18}')
print(emojize(f'Total de homens é \033[1;34m{M}\033[m :man:'))
print(emojize(f'Total de mulheres menores de 20 anos é \033[1;35m{F}\033[m :woman:'))
print(f'\033[1;36m~~\033[m'*30)
'''
# Exercicio 70
# Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não.
# No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.
'''
from emoji import emojize
tot = caro = menor = cont = 0
barato = ' '
print('\033[1;34m**\033[m'*20)
print(emojize(':saco_de_dinheiro:{:^30}:saco_de_dinheiro:'.format('SUPER BARATAO'), language = 'pt'))
print('\033[1;34m**\033[m'*20)
while True:
    print('\033[1;34m--\033[m'*20)
    prod = str(input('Digite o nome do produto: '))
    valor = float(input('Digite o valor: '))
    cont += 1 # ao ler o nomedo produto, ele sera contado
    tot += valor
    if valor >= 1000:
        caro +=1
    if cont == 1 or valor < menor:
        menor = valor
        barato = prod
    #else: blocos parecidos podem ser simplificados
    #    if valor < menor:
    #        menor = valor
    #        barato = prod
    res = ' '
    while res not in 'SN':
        res = str(input(emojize('Deseja continuar?[S/N] :rosto_bocejando:', language='pt'))).upper().strip()[0]
    if res == 'N': # o if do break tem que esta fora da identação do while
            break         
print('\033[1;31m==\033[m'*20)
print(f'Total de gastos: R${tot:.2f}')
print(f'Total de produtos maiores de R$1.000,00: {caro}')
print(f'O menor preco é R${menor:.2f} do(a) {barato}')
print('\033[1;31m==\033[m'*20)
'''
# Exercicio 71
# Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
# e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS:
# Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$2.
from emoji import emojize
print('\033[1;31;40m==\033[m'*20)
print(emojize('\033[1;34;40m:saco_de_dinheiro:{:^35}:saco_de_dinheiro:\033[m'.format('CAIXA ELETRONICO'), language='pt'))
print('\033[1;31;40m==\033[m'*20)
valor = int(input(emojize('Quanto você quer sacar?:rosto_com_cifrões: \nR$', language='pt')))
total = valor
cedula = 50 # a maior cedula a ser considerada
cedulatot = 0 # total dde cedulas a ser sacado
while True:
    if total >= cedula: # se total de cedulas for maior que as cedulas
        total -= cedula #  se retira do total a quantidade de cedulas
        cedulatot +=1 # e se soma a quantidade de cedulas totais
    else: # se não tiver cedulas sufucientes 
        if cedulatot > 0:
            print(f'Total de {cedulatot} cédulas de R${cedula}')
        if cedula == 50: # a cedula que for igual a 50 
            cedula = 20 # ela vira 20
        elif cedula == 20: # e se não tiver 20
            cedula = 10 # ela vira 10
        elif cedula == 10: # assim por diante 
            cedula = 1
        cedulatot = 0 # se acabar as cedulas, para
        if total == 0:
            break
print('\033[1;34m--\033[m'*20)
print(emojize('Tenha um bom dia! :rosto_de_palhaço: \nVolte sempre! :dedo_do_meio:', language='pt'))
print('\033[1;34m--\033[m'*20)