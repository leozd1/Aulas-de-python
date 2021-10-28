#Exercicio 05
#antecessor e sucessor
'''
x = int(input('digite um numero: '))
print('O antecessor de {} é {} e seu sucessor {}.'.format(x, (x-1),(x+1)))
'''

#Exercicio 06
#Dobro, tripo e raiz quadrada
'''
n = int(input('Digite um numero: '))
d = n * 2
t = n * 3
r = n **(1/2) #ou sqrt(n) ou pow(n,(1/2))
print('O dobro de {} é {},'.format(n,d))
print('O tripo de {} e {},'.format(n, t))
print('E a raiz quadrada de {} é {:.2f}'.format(n, r))
'''
#Exercicio 07
#Media Aritmetica
'''
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
m= (n1+n2)/2
print("A media das notas {:.1f} e {:.1f} será {:.2f}.".format(n1, n2, m))
'''
#Exercicio 08
#Conversão de valores
'''
m = float(input("Digite uma medida em metros: "))
cm = m * 100
mm = m * 1000
print('O valor de {:.1f} metros é {:.1f}cm e {:.1f}mm'.format(m, cm, mm))
'''
#Exercicio 09
#Tabuada
'''
nu = int(input('Digite um numero para a tabuada: '))
print('='*20)
print('{} x {} = {}'.format(nu, 1, nu*1)) #pode-se colocar expressoes apenas para se mostrar resultados
print('{} x {} = {}'.format(nu, 2, nu*2))
print('{} x {} = {}'.format(nu, 3, nu*3))
print('{} x {} = {}'.format(nu, 4, nu*4))
print('{} x {} = {}'.format(nu, 5, nu*5))
print('{} x {} = {}'.format(nu, 6, nu*6))
print('{} x {} = {}'.format(nu, 7, nu*7))
print('{} x {} = {}'.format(nu, 8, nu*8))
print('{} x {} = {}'.format(nu, 9, nu*9))
print('{} x {:2} = {}'.format(nu, 10, nu*10)) #pode-se colocar espaço no format colocando dois pontos
print('='*20)
'''
#Exercicio 10
#Conversor de moedas ou valores
'''
real = float(input('digite um valor em real: '))
dolar = real/5.39
print('-'*20)
print('O valor de {} reais em dolares é {:.2f}'.format(real, dolar))
'''
#Exercicio 11
#Medição de área para pintura
'''
larg = float(input("Digite a largura da parede: "))
alt = float(input('Digite a altura da parede: '))
area = larg * alt
tinta= area/2
print("sua parede de {}m x {}m tem a área de {}m², será necessário {} litros de tinta".format(larg, alt, area, tinta))
'''
#Exercicio 12
#Descontos e porcentagens
'''
prod = float(input("digite o valor do produto: "))
desc = prod - (prod * 5/ 100)
valor = prod * 5 / 100
print('-'*25)
print('O produto que custava R${}, na promoção de 5% de desconto vale R${}, desconto de R${}'.format(prod, desc, valor))
'''
#Exercicio 13
#Salario aumento
'''
sal = float(input("Digite o valor do salário: "))
novo = sal + (sal * 15/100)
val = sal * 15 /100
print("-"*25)
print('O salário de R${}, terá aumento de {}, e passará a ser de R${}'.format(sal, val, novo))
'''
#Exercicio 14
#Converção de temperatura de graus Celsius em Fahrenheit. 
'''
C = float(input('Digite a temperara em Celcius: '))
F = ((9*C)/5)+32
print("="*25)
print('{}C°, em Fahrenheit é {}F°'.format(C,F))
print('*'*30)
'''
#Exercicio 15
#Aluguel de carros; sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
dias = int(input('Quantos dias alugaste o carro?: '))
km = float(input('Quantos kilometros rodados?: '))
pago = (dias * 60) + (km * 0.15)
print('='*30)
print('O total a pagar é R${:.2f}'.format(pago))
print('*'*30)