# Listas (Parte 2)
'''
As listas, que são variáveis compostas, que permite adicionar outras listas dentro,
já que a sua estrutura basica é mutavel.
'''
# Exemplos
dados= list() # forma da lista, ou = []
'''
Essa é uma estrutura basica de uma lista
'Pedro'   25
-------/------/
  0       1    
''' 
dados.append('Pedro')
dados.append(25)

print(dados[0]) # mostra o dado 0 da lista, no caso o 'Pedro'
print(dados[1]) # o mesmo, mostra o dado 1 da lista, no caso o 25
'''
Podendo adicionar (dar um append) em outra estrutura de lista,
criando uma copia de uma lista dentro de outra lista, uma lista composta
'''
pessoas = list()
pessoas.append(dados[:]) # pessoas.append([:],copia de dados), cirando assim uma lista composta
'''
Lista Composta
---------------
estrutura de Listas dentro de outra lista
'Pedro', 25 / 'Maria', 19 /  'João', 32
-------,--- / -------,--- / -------,----
  0      1       0     1       0     1
------------/------------ /----------------
      0           1               2
'''
pessoas = [['Pedro',25],['Maria',19],['João',32]] # ficando assim a lista dentro da lista

print(pessoas[0][0]) # mostra o valor que ta dentro da lista na estrutura 0 do item 0 = 'Pedro'
print(pessoas[1][1]) # mostra o valor da estrutura 1 do valor 1 = 19
print(pessoas[2][0]) # mostra a estrutura 2 no item 0 = 'João'
print(pessoas[1]) # mostra somente a estrutura 1, no caso a lista inteira dentro dda estrutura 1

# Exemplos praticos
# lista de teste
teste = list()
teste.append('gustavo')
teste.append(40)
print(teste) # mostra a lista composta
galera = list()
galera.append(teste[:]) # criamos uma copia da lista teste ao adicionar o [:], sem isso adicionamos a lista
teste[0] = 'Maria' # tentaremos modificar a lista
teste[1] = 22
galera.append(teste[:]) # tentaremos mostrar a lista com as alterações feitas, sem o [:], alteramos a lista original
print(galera)
'''
Graças a ligação que existe entre as litas, ao modificar uma lista, modifica a original também,
mas ao acrescentar [:], cria uma copia da lista que permite mante a original sem alterações.
'''
gale = [['joão', 19],['Ana', 33],['Joaquim', 13],["Maria", 45]] # 4 estruturas dentro de 1 lista
print(gale) 
print(gale[0]) # mostra todos os dados do 'João'
print(gale[0][0]) # mostra so o nome do 'joão'
print(gale[2][1]) # mostra so o item 1 da estrutura 2 = 13
for p in gale: 
  print(p) # pode-se usar o for para mostrar a lista ordenada
for p in gale:
  print(p[0]) # permite mostrar somente a estrutura escolhida
for p in gale:
  print(f'{p[0]} tem {p[1]} anos') # permite mostrar somente as informações desejadas
galeris = list() # lista original
dados = list() # lista que vai receber a copia
for c in range(0 ,3): # for para adicionar as informações da lista composta
  dados.append(str(input('Digite um nome: ')))
  dados.append(int(input('Idade: ')))
  galeris.append(dados[:]) # faz uma copia da lista dados usando o [:], para a lista galeris
  dados.clear() # limpa a lista de dados, e sem o [:], afeta a duas listas, ja que estão
                # ligadas entre si, e com o [:], so limpa a lista desejada 

print(galeris) # mostra a lista composta 

totmaior = totmenor = 0 # exemplo pratico composto
for p in galeris: # para mostrar um dado especifico, no caso a idade.
  if p[1] >= 21:
    print(f'{p[0]} é maior de idade')
    totmaior += 1
  else:
    print('São menores de idade:')
    print(f'{p[0]} são menores de idade')
    totmenor += 1
print(f'Temos {totmaior} maiores e {totmenor} menores de idade')

# Exemplos praticos 2
testis = []
