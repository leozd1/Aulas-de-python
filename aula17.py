# Listas (Parte 1)
'''
 Resumo: As tuplas servem para guardas elementos, onde o computador reserva uma parte 
da memoria para criar uma variavel (estrutura) composta para armazenar essa
informação, onde cada elemento é salvo em uma key, tornando a tupla 'imutavel',
inpedindo o elemento ser alterado.
 
   As listas uma variavel composta que se utiliza de colchetes-[] para armazenar seus
elementos, que podem ser alterados (excluidos, trocados, etc) já que a listas é 'mutavel'.
 E mesmo sendo similar a tupla, as listas tem comportamento diferenciado ao usar comandos ao interagir
aos elementos.
  
 Sendo seus comandos de interação com elementos mais basicos:
'''
lanche = ['hamburguer', 'pizza', 'suco', 'pudim']
lanche.append('cookie') # permite adcionar novos elementos na lista
lanche.insert(0,'cachorro-quente') # permite adicionar um elemento em local a escolha, no caso na posição 0
                                   # no lugar do 'hamburguer', que se toma a posição 1.
del lanche[3] # apaga o elemento na posição 3
lanche.pop(3) # usado geralmente pra apagar o ultimo elemento, mas pode passar o paramentro(posição) do elemento desejado
lanche.remove('pizza') # removendo apenas o valor do elemento, no caso a 'pizza' 
# Obs.: os metodos del, .pop() e remove(), ao apagarem o elemento e seu valor, eles repociosionam os indices dos elementos restantes

# existe um meio de verificar se o elemento existe antes de realizar sua remoção.
if 'pizza' in lanche: # se 'pizza' existir/esta em lanche
    lanche.remove('pizza') # remova a 'pizza'

# é possivel criar listas com a range do for
valores = list(range(4,11)) # sendo que tem que declarar a função list() antes de usar a range()
print(valores)
# formas de ordenas as litas
valor = [2,8,6,9,7,4,1]
valor.sort() # permite arrumar a ordem em que os elementos aparecem
print(valor)
valor.sort(reverse=True) # ordena de forma revertida os elementos
print(valor)

len(valor) # revela o tamanho da lista, assim como a tupla
print(len(valor))

# exercico pratico
n = [5,9,1]
n[2] = 3
print(n)
n.append(7)
print(n)
n.sort()
print(n)
n.sort(reverse=True)
print(n)

print(len(n), 'elementos')
n.insert(2,8)
print(n)
n.pop()
print(n)
n.pop(2)
print(n)
n.remove(9)
print(n)
if 9 in n:
  n.remove(9)
else:
  print('não achei, ja foi removido')

num = [] # ou list(), tanto faz
num.append(5)
num.append(3)
num.append(4)
num.append(6)
print(num)
# pode-se usar um for para organizar
for v in num:
  print(f'{v}...',end='')
  
for c, v in enumerate(num): # mostra o indice e os elementos
  print(f'\nna posição {c} esta o valor {v}...')
# se mostrar so um dado do for, como for v in enumerate(num), mostra tudo junto
for v in enumerate(num):
  print(f'{v}...',end='')
''' 
x = list() 
for cont in range(0,3): # colocando dados do teclado em uma lista
  x.append(int(input('\nDigite um valor ')))
print(x)
'''
a = [2,8,4,6]
b = a
print('\nlista b ',b)
print('lista a ',a) # mostra que as listas são iguais
b[2] = 9 # ao alterar em uma lista, a outra que foi adicionada e alterada também, ja que a ligação entre elas
print('\nlista b ',b)
print('lista a ',a)
b = a[:] # b recebe todos os valores de a,
         # forma de "copiar" todos os valores, podendo alterar um, sem alterar o outro, rompendo a ligação
b[2] = 5
print('\nlista b ',b)
print('lista a ',a)
