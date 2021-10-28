# Exercicio 107
# Crie um módulo chamado moeda.py que tenha as funções incorporadas
# aumentar(),
# diminuir(),
# dobro() e
# metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções.
'''
Dica: No exercicio ficou tudo dentro de uma pasta, o modulo e o programa principal em arquivos separados.
Coloque os modulos dos exercicios dentro da pasta aula22Pacote
o modulo moeda107.py > aula22Pacote


# Programa Principal
from aula22Pacote.moeda107 import metade, dobro, aumentar, diminuir
# da pasta.modulo importe a função - 
# ou
# from aula22Pacote import moeda107 - terá que expecificar a função (moeda107.diminuir(p))
# devendo estar na mesma pasta, poderia dar um import so do modulo
# mas cuidado ao usar "from pasta import modulo", pois pode causar conflito

p = float(input('Digite um preço: \nR$ '))
print('\033[0;33m==\033[m'*20)
print(f'A metade de R${p:.2f} é R${metade(p):.2f}')
print('\033[0;36m==\033[m'*20)
print(f'O dobro de R%{p:.2f} é R${dobro(p):.2f}')
print('\033[0;37m==\033[m'*20)

print(f'O preço a 10% de aumento, será R${aumentar(p, 10):.2f}') # o valor da taxa é fixa
print('\033[0;34m==\033[m'*20)
print(f'O preço com 50% de desconto, será R${diminuir(p, 50):.2f}')
print('\033[0;34m==\033[m'*20)
'''

# Exercicio 108
# Adapte o código do desafio #107,
# criando uma função adicional chamada moeda()
# que consiga mostrar os números como um valor monetário formatado.
'''
from aula22Pacote import moeda107

p = float(input('Digite um preço: \nR$ '))
 
print('\033[0;33m==\033[m'*20)
print(f'A metade de {moeda107.moeda(p)} é {moeda107.moeda(moeda107.metade(p))}') # parte do exercicio 108
print('\033[0;36m==\033[m'*20)
print(f'O dobro de {moeda107.moeda(p)} é {moeda107.moeda(moeda107.dobro(p))}') # parte do exercico 107
print('\033[0;37m==\033[m'*20)

print(f'O preço a 10% de aumento, será {moeda107.moeda(moeda107.aumentar(p, 10))}') # o valor da taxa é fixa
print('\033[0;34m==\033[m'*20)
print(f'O preço com 50% de desconto, será {moeda107.moeda(moeda107.diminuir(p, 50))}')
print('\033[0;34m==\033[m'*20)
'''

# Exercicio 109
# Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais,
# informando se o valor retornado por elas vai ser ou não formatado pela função moeda(),
# desenvolvida no desafio 108.
'''
Resumindo, mexe no modulo do exercicio 108 pra ficar bonito

from aula22Pacote import moeda107 as moedita # as transforma uma palavra em outra,
                                             # util em caso de palavras repetidas
p = float(input('Digite um preço: \nR$ '))
 
print('\033[0;33m==\033[m'*20) # pode-se tirar a chamada do modulo do função em excesso
print(f'A metade de {moedita.moeda(p)} é {moedita.metade(p, True)}') # parte do exercicio 108
print('\033[0;36m==\033[m'*20)
print(f'O dobro de {moedita.moeda(p)} é {moedita.dobro(p)}') # parte do exercico 107
print('\033[0;37m==\033[m'*20) # por não especificar se é false ou true, ele considera como false, por ta vazio

print(f'O preço a 10% de aumento, será {moedita.aumentar(p, 10, True)}') # o valor da taxa é fixa
print('\033[0;34m==\033[m'*20) # 'so retorne res se formato for False, senão retorne moeda(res), ou seja, bonitinho'
print(f'O preço com 50% de desconto, será {moedita.diminuir(p, 50)}') # só atente para as formas de retorno formatada
print('\033[0;34m==\033[m'*20) # na hora de retirar os excesso do pacote de modulos das funções
'''

# Exercicio 110
# Adicione o módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(),
# que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.
'''
Continue mexendo no modulo moeda107

from aula22Pacote import exer110 as moeda # as transforma uma palavra em outra,
                                          # util em caso de palavras repetidas
p = float(input('Digite um preço: \nR$ '))
moeda.resumo(p)
'''
# Exercicio 111
# Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado.
# Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote
# e mantenha tudo funcionando.
'''
basicamente colocar o modulo com as funções em uma pasta(pacote) dentro de outra pasta(pacote)
e chamar ele das seguites formas, atraves do arquivo __init__.py:
from aula22Pacote.utilidadesCeV import moeda
from aula22Pacote.utilidadesCeV import moeda, dado (caso precise importar os dois pacotes)
import aula22Pacote.utilidadesCeV (mas ai precisa escrever todo o caminho no programa principal)
    aula22Pacote.utilidadesCeV.moeda.resumo(p)

from aula22Pacote.utilidadesCeV import moeda # sendo esse mais simples e usado o chamado
                                             # da pasta aula, dentro de utilidade, importe moeda
p = float(input('Digite um preço: \nR$ '))
moeda.resumo(p)
'''

# Exercicio 112
# Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado.
# Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função imputa(),
# mas com uma validação de dados para aceitar apenas valores que seja monetários.

from aula22Pacote.utilidadesCeV import moeda # sendo esse mais simples e usado o chamado
                                             # da pasta aula, dentro de utilidade, importe moeda
from aula22Pacote.utilidadesCeV import dado

p = dado.escreva("Digite um valor: \nR$ ")
moeda.resumo(p, 10, 10)