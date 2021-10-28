#  Funções (Parte 2)
'''
Topicos aplicados nessa aula de Funções

- Interect Help: A Ajuda Interativa, tambem chamado de help(), é uma função interna do python, 
usado geralmente para descrever alguma funcionalidade ou comando do python ao se colocar no nome 
que deseja na entrada de referência (os parenteses da função), onde descreve e da dicas de casa 
função ou funcionalidade repassa a ele.
'''
# Exemplo: 
help(print) # descreve em detalhes a função print(), com direito a dicas

help(len) # descreve brevemente a função len()

'''
Existen outro comando similar a função help(), o doc interno do comando, ou o print(._ _doc_ _),
que "imprimi" os documentos dos comandos das funcionalidades, não da mesma maneira que o help(), mas é usado 
como complementar de informações.
'''
print(input.__doc__) # descreve de maneira mais detalhada a funcionalidade do input()
help(input) # descreve o mesmo, pórem apresenta dicas e exemplos breve de usos

'''
- docstrings: É uma String de documentação das funcionalidades das funções, podendo ser usadas
pelas funções criadas pelo usuário. Diferente do help() que só da uma breve descrição da função.

A docstring deve ser feita depois da definição da função, do def(), usando as aaspas duplas 3 vezes("""),
na entrada e saida, descrevendo assim a utilidade da função desejada, sendo que o paramentro
deve seguir a descrição do exemplo abaixo, com o :param (descrição do parametro) e o :return (retorno).
Para ai sim depois, pode-se dar um help() na função criada pelo usuário

Dica: evite acentos e formatações especiais, não reconhece os caracteres.
'''
# exemplo:
# função
def contador(inicio, fim, passo):
    """
    → Faz a contagem de com passos, mostrando na tela o resultado
    :param inicio: inicio da contgem # param, e de paramentro
    :param fim: fim d acontagem
    :param passo: passo, ou pulo da contagem
    :return: sem retorno (de informações)
    """
    c = inicio
    while c <= fim:
        print(f'{c}', end=' ')
        c += passo
    print('FIM!')

# programa principal    
contador(1,10,2)

help(contador) # sem a docstring, descreve somente o nome da função e o nome dos paramentos, ou seja, nada (-_-!) 

'''
- Argumentos opcionais: Usado geralmente como alternativa para falta de paramentos repassados as funções, os paramentos
opcionais permite subustituir as variaveis faltantes não declaradas por outro valor caso estes faltem na declaração da
função, podendo ser aplicado a todos os paramentos.

Erro apresentado caso falte o paramentro a ser declarado:
TypeError: somar() missing 1 required positional argument: 'c'
'''
def somar(a=0,b=0,c=0):
    """
    > Faz a somatoria dos valores, mostrando na tela o resultado
    :param a: primeiro valor
    :param b: segundo valor
    :param c: terceiro valor
    :return: sem retorno (de informacoes)
    """
    s = a + b + c
    print(f'A soma dos valores é {s}')

somar (1,2,3)
somar(1,2)
somar()
somar(b=2, a=6) # posso trocar os paramentros de lugar
'''
- Escopo de Variaveis: Sendo o escopo do local onde a varialvel vai existir ou não, reconhecido como 
escopo local ou escopo global, as variaveis declaradas passam a ser usadas em areas especificas do programa,
sendo global as variavel declaradas no corpo, ou escopo, principal do programa, podendo ser usada em todo o programa, 
sem restrições, ou local, se declaradas dentro de areas limitadas, como as areas da função, dando erro caso
as variaveis locais sejem declaradas fora da sua area, escopo.

Obs: Atente na hora da declaração das variaveis no escopo, ppois caso nomeie (declare) uma variavel global dentro do
do escopo local, ela passa a ser local também, perdendo assim seus atributos globais.

Mas caso use declaração "global" dentro do escopo local, ele pede que se use a variavel global como global,
mantendo os atributos gobais da variaveis.
'''
def teste():
    global n
    #n= 6
    x = 8 # por ser declarada somente dentro da função, é reconhecido como escopo local
    print(f'na função teste, n vale {n}')
    print(f'na função teste, x vale {x}')
# programa principal
n = 2 # conhecido como variavel de escopo global, ele pode ser aplicado em todo programa
print(f'no progrma principal, n vale {n}')
teste()

'''
- Retorno de resultados: Podendo ou não retornar os valores declarados no escopo local, geralmente usados nas 
funções, retornando apenas os resultados das variaveis, atraves da declaração local return, precisando ser recebido
por alguma variavel no programa principal, permitindo manipular o resultado do retorno pelo programa como quiser.
E podendo retornar qualquer coisa também, como Strings, floats, tuplas, ate listas.
'''
def soma(a=0, b=0, c =0): # passando os argumentos como opcionais
    s = a + b + c
    return s
    
r1 = soma(3,5,7)
r2 = soma(2,4)
r3 = soma(8)
print('\033[1;32m~\033[m'*40)
print(f'os resultados retornados da função foram: {r1}, {r2}, {r3}')

# exercicios praticos
# 1:
def fatorial(num = 1): # caso não informe um numero, ele vale 1
    f = 1 # variavel local (so existe dentro da função)
    for c in range( num, 0, -1):
        f *= c
    return f
    
# programa principal
n = int(input("Digite um numero: "))
print('\033[1;35m~\033[m'*40)
print(f'O fatorial de {n} é {fatorial(n)}') # pode-se manipular a função com retorno
f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial(2)
print(f'Os resultados são {f1}, {f2}, {f3}')
print('\033[1;35m~\033[m'*40)

# 2:
def ParOuImpar(nu=0):
    if n %2 == 0:
        return True # podendo o return "retornar" qualquer coisa
    else:
        return False
x = int(input('Digite um numero: '))
print('\033[1;34m~\033[m'*40)
print(ParOuImpar(x))
if ParOuImpar(x): # podendo ser declarado dessa forma o return da função
    print('É par') # ja que posso manipula-lo da forma que quiser.
else:
    print('É impar')
print('\033[1;34m~\033[m'*40)