#Aula 09
# Manipulções de Strings
#Strings são imutaveis, não pode trocar "C" po "J" por exemplo, mais pode transformar
#Para uma transformação ser permanente, deve ser "salva", recebida em um objeto

# Fatiamento

frase = 'curso em video python'
frase[9] # só mostra o caractere no espaço especifico
# seguindo a regra dos colchetes ex: objeto[inicio: fim: pulo]
frase[9:13] # mostra os caracteres que estão entre o espaço 9 até o 12, sendo o 13 o fim
frase[9:21:2] # mostra os caracteres que há entre os espaços 9 a 20, já que o 21 é ignorado, pulando 2 espaços
frase[:5] # mostrando os caracteres que estão no inicio ate o espaço 4, já que o 5 é ingnorado
frase[15:] # o inverso da operação anterior, mostra o inicio até o fim, já que não sabe até onde fica o limite
frase[9::3] # mostra o inicio da contagem de caracteres ate o fim, pulando 3 espaços, já que não limite

print(frase[9])
print(frase[9:13])
print(frase[9:21:2])
print(frase[:5])
print(frase[15:])
print(frase[9::3])

# Analise

len(frase) # mostra o comprimento do objeto
frase.count('o') # mostra quantas vezes os caracteres aparecem 
frase.count('o',0,13) # mostra quantas vezes aparecem os caracteres entre inicial e final
frase.find('deo') # mostra a localização do inicio da busca
frase.find('xupa') #mostra -1 caso não encontre a localização ou caractere
'curso' in frase # Mostra se há ou não os caracteres selecionados, verdadeiro ou falso 

print(len(frase))
print(frase.count('o'))
print(frase.count('o',0,13))
print(frase.find('deo'))
print(frase.find('xupa'))
print('curso' in frase)

# Transformação

frase.replace('python', 'android') # Troca o caractere escolhido por outro
frase.upper() # Transforma caracteres minusculos em maiusculos, independentes se ja tiver
frase.lower() # Troca os caracteres maiusculos em minuculos, o oposto do upper()
frase.capitalize() # Tranformar todos os caracteres em minusculos e somente o primeiro fica maiusculo
frase.title() # Analisa os caracteres deixando somente as primeiras letras das palavras em maiusculo

frases = '   Aprenda Python  '
frases.strip() # Remove os espaços inuteis do inicio e do fim das palavras, deixando os meio livres 
frases.rsplit() # Remove os ultimos espaços dos caracteres, espaços da direita
frases.lstrip() # Remosve os primeiros espaços, os espaços da esquedas das palavras

print(frase.replace('python', 'android'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
print(frases)
print(frases.strip())
print(frases.rstrip())
print(frases.lstrip())

# Divisão

frase.split() # Divide os espaços entre palavras, criando assim uma lista de palavras

print(frase.split())

# Junção

"-".join(frase) # Deveria juntar os espaços, substituindo pelo caractere de escolha

print('-'.join(frase))

#Exemplos
#pode-se unir os modulos
print(frase.upper().count('O')) #Conta quantas vezes aparece o "O" maiusculo, sendo que não tem

print(len(frases.strip())) # Conta quantos caracteres possui, sem os espaços extras

frase = frase.replace('python', 'Java')
print(frase) #Para uma transformação ser permanente, deve ser "salva", recebida em um objeto

print(frase.lower().find('java')) # encontra a posição da palavra depois de se tornar minuscula

dividido = frase.split()
print(dividido[0]) #Permite mostrar somente a palavra desejada, pois a frase foi dividida em uma lista
print(dividido[3][0]) #mostra somente a letra da palavra escolhida na lista feita pelo split()

print(""" Para escrever um texto longo, 
pode-se usar as três aspas que ele mostra,
sem problemas, só não esqueça de colocar 
as três aspas no final, claro né!""")
