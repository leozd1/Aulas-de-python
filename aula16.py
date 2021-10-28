# Tuplas
'''
 As tuplas são variáveis compostas e imutáveis que permitem armazenar vários valores em uma mesma estrutura,
 acessíveis por chaves individuais.
Os indices  são indicadores de elementos diferentes, que reunidos montam a Tupla.
 Tornando assim as Tuplas uma variavel composta que permite fatiamento dos elementos das variaveis
 OBS.: As Tuplas são imutaveis, não podem ser trocadas ou excluidas. 
 As variveis compostas podem ser ter parenteses-(), chaves-[], colchetes-{}, ou nem isso
 Sendo:
 Tuplas= ()
 Listas = []
 Dicionário = {}

Exemplo: 
'''
lanche = ('hamburguer', 'pizza', 'suco', 'pudim') # preferencia em usar esse
lanche = 'hamburguer', 'pizza', 'suco', 'pudim'
print(lanche) # cuidado, mesmo sem parenteses, o print pode considerar um Tupla, mostrando com os parenteses 

#Fatiamento
print(lanche[1]) # se usa colchetes para referenciar a variavel desejada
print(lanche[-2]) # se usa menos (-) para mostrar de tras pra frente
print(lanche[1:3]) # deverá mostrar os elementos fatiados de 1 ate 2, sendo que o 3 é ignorado
print(lanche[2:]) # mostra da variavel inicial ate o final, ou seja, 'suco' ate 'pudim' ou [3,4]
print(lanche[:2]) # mostra do inicio da tupla ate a variavel final,ignorando o ultimo elemento, ou seja, do 'hamburguer' ate a 'pizza' ou [0,1]
print(lanche[-2:]) # começa do fim ate o elemento variavel, 'suco' are 'pudim'

'''
 Sendo tuplas imutaveis, não permite troca
#lanche [1] = "bolo"
#print(lanche[1])
mostrando o erro: 'TypeError: 'tuple' object does not support item assignment' 
                    (objetos do tipo tuplas não podem ser assimilados)
'''
# o for permite alem de ler os elementos, permites organizar los
# sendo um laço de repetição com interação, permitindo manipular a tupla
lanche = ('hamburguer', 'pizza', 'suco', 'pudim')
for comida in lanche:
    print(f'\033[1;31mQuero comer {comida}\033[m')
# podendo o for aceitar o len() para mostrar a tupla
for cont in range(0, len(lanche)): # onde a leitura da tupla sera da mesma forma que antes
    print(lanche[cont])

for cont in range(0, len(lanche)): # caso precise mostrar a posição 
    # print(lanche[cont], cont)
    print(f'como {cont}° foi {lanche[cont]}')
    
for pos, comida in enumerate(lanche): # ou esse para mostrar posição
    print(f'\033[1;31mQuero comer {comida} na posição {pos}\033[m')
    
lanche = ('hamburguer', 'pizza', 'suco', 'pudim')
print(sorted(lanche)) # sorted, coloca a tupla em formato ordenado
print(lanche) # so pra ilustrar que o sorted coloca a tupla em lista, diferenca pelo parenteses

a = (1,3,5,7,9)
b = (2,4,5,8)
c = a + b # se tentar "somar" as tuplas, elas vão concatenar (juntar) las
print(c)
print(len(c)) # o len, ele le a quantidade de elementos da tupla
print(c.count(5)) # o .count() conta quantas vezes o elemento aparece na tupla
print(c.index(8)) # o index mostra a posição do elemento da tupla, se tiver mais um elemento igual, ele mostra o primeiro
print(c.index(5, 3)) # mas colocando o .index() para procurar o elemento partir da posição conhecida do primeiro elemento igual,
# ele mostra o proximo

pessoa = ('leia', 1, 'livro', 3.4) # A tupla permite mais de um tipo de elemento
del(pessoa) # del() permite apagar somente a tupla inteira
print(pessoa)


