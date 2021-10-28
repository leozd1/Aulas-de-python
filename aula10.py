# Aula 10
# Estruturas condicionais simples e compostas (if..else)

# Estrutura Sequencial 
'''
'Ela segue uma estrutura em sequencia, de cima para baixo, sem pulos de etapas
'''
# Estrutura Condicional
'''
Segue uma sequencia que pode aderir um desvio a estrutura original, 
possibilitando escolhas de rotas na sequencia, onde a escolha de uma rota desabilita a outra.'
'Criando assim fluxo, ou rotas, dinstintos, como os fluxos se..senão, onde haverá o fluxo verdadeiro (se..),
e o fluxo falso (senão..). 
Ex: Se algo acontece.., senão acontece algo
Se algo:               if algo:
    bloco exemplo        bloco exemplo
Senão algo:            else algo:
    bloco exemplo          bloco exemplo

Onde a a estrutura simple será usado o 'if', e a estrutura composta será usado o 'else'
'''

#Exemplo 01: 
import emoji
'''
tempo = int(input('Quantos anos tem seu carro? '))
print('='*30)
if tempo <= 3:
    print('Seu carro tá novo.')
else:
    print('Precisa trocar de carro')
print(emoji.emojize('--Bom Dia, seu :shit:--',use_aliases=True))
'''
#Exemplo 02, condição simplificada:
'''
tempo = int(input('Quantos anos tem seu carro? '))
print('='*30)
print('carro novo' if tempo <= 3 else 'carro velho')  # usado em situação simples, evite usar
print(emoji.emojize('--Bom Dia, seu :shit:--',use_aliases=True))
'''
# Exemplo 03:
'''
nome = str(input('Qual é seu nome? '))
if nome == 'Gustavo':
    print("Que nome Bonito")
else:
    print(emoji.emojize('que nome :shit:',use_aliases= True))
print(emoji.emojize('Tenha um bom dia {}! :smile:'.format(nome), use_aliases= True))
'''
#Exemplo 04:
'''
n1 = float(input('digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) /2
print('='*30)
print('sua media foi {:.1f}'.format(m))
if m >=7:
    print(emoji.emojize("Aprovado :smile:",  use_aliases= True))
else:
    print(emoji.emojize("Reprovado, estude mais seu :shit:", use_aliases= True))
'''
#Exemplo 05:
n1 = float(input('digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) /2
print('='*30)
print('sua media foi {:.1f}'.format(m))
print('Parabens' if m >= 7 else 'Reprovado') #forma simplificada, evite