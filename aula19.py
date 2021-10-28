# Dicionários
'''
Sendo variavéis compostas, assim como as listas e as tuplas,
os dicionários são estruturas de dados semelhantes as listas() e 
as Tuplas(), sendo seus indices personalizados, como literais (palavras).
Onde os dicionários são variáveis compostas mutaveis, sendo declarados como ditc() ou {}.
Os elementos, os indices, do codionário são chamados de chaves, ou keys.
E seus dados, as informações, são chamados de valores.
Exemplos Teóricos:
Tuplas          Listas                      Dicionários
dados = ()      dados = list() ou []        dados = {} ou dict()

dados = dict ('nome': 'pedro', 'idade': 25)
dados = {'nome': 'pedro', 'idade': 25}

|'pedro'  | 25 |
--------   ---- 
'nome'   'idade'    
print(dados['nome']) = 'pedro'
-------------------------
print(dados['idade']) = 25
---------------
Para adicionar variaveis, simplesmente adicionamos as variaveis no dicionarios
dados['sexo'] = M

|'pedro'  | 25 |   'M' |
--------   ----   ----
'nome'   'idade'  'sexo'
---------------
print(dados['sexo']) = 'M'
---------------

Para remover as variaveis usamos o del,
que remove a varia´vel e suas informações

del dados['idade']

''' 
# Exemplos praticos
filmes = {'titulo': 'Star Wars', 
          'ano': 1987,
          'diretor': 'George Lucas',
}

print(filmes.values()) # mostra todos os valores do dicionário
'''
------------------------------------------------
dict_values(['Star Wars', 1987, 'George Lucas'])
------------------------------------------------
'''
print(filmes.keys()) # mostra as chaves, os titulos do dicionário
'''
------------------------------------------------
dict_keys(['titulo', 'ano', 'diretor'])
------------------------------------------------
'''
print(filmes.items()) # mostra tudo, tanto os valores como as chaves
'''
------------------------------------------------
dict_items([('titulo', 'Star Wars'), ('ano', 1987), ('diretor', 'George Lucas')])
-------------------------------------------------

O items() e comumente usados em laços for para mostrar todos os itens
'''
for key, valor in filmes.items():
    print(f' o {key} é {valor}')
'''
-------------------------------------------------
o titulo é Star Wars
o ano é 1987
o diretor é George Lucas
-------------------------------------------------
'''
# Exemplos praticos

'''
Podemos juntar os dicionários em lista maior,
colocando os itens dentro da lista com append()
ex:
'''
pessoas = {'nome': 'gustavo', 'sexo': 'M', 'idade': 25}

print(pessoas) # {'nome': 'gustavo', 'sexo': 'M', 'idade': 25}
print(pessoas['nome']) # gustavo
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos') # atenção ao recerenciar os elementos
                                                          # se usa colchetes [] e ao declarar usa-se chaves {}
                                                          # e pra colocar string dentro da declaração formatada
                                                          # usa-se aspas duplas dentro das simples (f'xxx "aaa "xxx ')
'''
-------------------------------------------------------
O gustavo tem 25 anos
-------------------------------------------------------
'''
print(pessoas.keys()) # dict_keys(['nome', 'sexo', 'idade']) ; mostra as chaves 
print(pessoas.values()) # dict_values(['gustavo', 'M', 25]) ; mostra os valores 
print(pessoas.items()) # dict_items([('nome', 'gustavo'), ('sexo', 'M'), ('idade', 25)]) ; mostra os itens
# sendo o itens uma composição, onde os itens são uma lista composta de Tuplas.

# usa-se laços para acessar partes especificas dos itens
for k in pessoas.keys(): # para cada chave de pessoas.chaves
    print(k) # mostre a chave
'''
------------------------------------
nome
sexo
idade
------------------------------------
Percebe-se que fica mais bonitinho e organizado assim
'''
for k in pessoas.values(): # para cada chave de pessoas.valores
    print(k) # mostra os valores 
'''
------------------------------------
gustavo
M
25
------------------------------------
mas ao usar o itens() deve usar duas declarações no for
'''
for k, v in pessoas.items():
    print(f'{k} = {v}') 
'''
------------------------------------
nome = gustavo
sexo = M
idade = 25
------------------------------------
no caso do dicionário, não usa-se o enumerete,
ele é mais usado em Tuplas e listas. Sendo necessário
usar o items(), keys() ou values() junto com o for

da pra usar o for pra arrumar a estrutura dos itens
'''
del pessoas['sexo'] # del serve para apagar um item e seus valores
for k, v in pessoas.items():
    print(f'{k} = {v}') 
'''
------------------------------------
nome = gustavo
idade = 25
------------------------------------
'''
pessoas['nome'] = 'leonice' 
for k, v in pessoas.items():
    print(f'{k} = {v}') 
'''
por ser mutavél, permite modificar os valores das chaves
------------------------------------
nome = leonice
idade = 25
------------------------------------
'''
pessoas['peso'] = 54.4 
for k, v in pessoas.items():
    print(f'{k} = {v}') 
'''
Além de permitir adcionar, por simples declaração,
itens ao dicionário
------------------------------------
nome = leonice
idade = 25
peso = 54.4
------------------------------------
'''
# Alem de permitir colocar um dicionário dentre de uma lista 
brasil = list()
estado1 = {'uf:': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf:': 'Para', 'sigla': 'PA'}
estado3 = {'uf': 'Sao Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
brasil.append(estado3)

print(brasil)
'''
------------------------------------
[{'uf:': 'Rio de Janeiro', 'sigla': 'RJ'}, {'uf:': 'Para', 'sigla': 'PA'}, {'uf': 'Sao Paulo', 'sigla': 'SP'}]
------------------------------------
'''
print(brasil[0])
'''
------------------------------------
{'uf:': 'Rio de Janeiro', 'sigla': 'RJ'}
------------------------------------
'''
print(brasil[0]['uf:'])
'''
------------------------------------
Rio de Janeiro
------------------------------------
'''
brasil = list()
estado = dict()
for c in range(0, 3): 
    estado['uf'] = str(input('Digite o estado: ')) # lembre-se por ser um dicionario, preferivel 
    estado['sigla'] = str(input('Digite a sigla do estado: ')) # coloca-lo como String
    brasil.append(estado.copy()) # ao inseri-lo em uma lista, é necessario fazer uma copia, usando o .copy()
print(brasil) # assim a copia-se o conteudo pra lista, sem erro de inserir so um item.
for e in brasil: # um for pra forma de mostrar mais organizado, sendo o for de fora pra lista
    # print(e)
    for k, v in e.items(): # e esse para o dicionario
        print(f' o campo {k} tem o valor {v}') # onde mostra cada chave com seu respctivo valor


'''
------------------------------------

------------------------------------
'''