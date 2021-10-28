#Aula 07 Operadores logicos, acho
"""
Ordem de precedencia aritmeticas
() = parenteses vem primeiro
** = exponenciação vem em segundo
*,/,//,% = multiplicação, divisão, divisão inteira e divisão do resto vem em terceiro
+, - = soma e subtração são os ultimos
"""
'''
nome = input('Qual o seu nome?: ')
print('='*20)
print('Prazer, {:=^40}!'.format(nome))
''' # pode-se se centralizar o print colocando variaveis no format
n1 = int(input("digite um valor: "))
n2 = int(input('digite outro valor: '))
s = n1 - n2
m = n1 * n2 
d = n1 / n2 
div = n1 // n2 
rest = n1 % n2 
exp = n1 ** n2 
print('='*30)
print("A soma do valores vale {}".format(n1+n2)) #expressoes so podem ser usadas dentro format se forem pequenas
print('A subtração e igual a {}, \nA multiplicação e igual a {}, \nA divisão e igual a {:.2f}, \nA divisão inteira e igual a {},'.format(s, m, d, div))
print('O resto da divisão e igual a {}, \nA exponenciação e igual a {}'.format(rest, exp))

