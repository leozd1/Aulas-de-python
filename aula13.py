# Estrutura de Repetição 
# Com variavel de Controle
# FOR (para.. ate ..), usado para limitar a repetição de comandos
# atravez de um contador de instruções, o laço de variavel de controle 
#ex: 
# laço de C intervalo (inicio, fim, passo, incremento ou decrimento)       for C in range(1, 10):
# fim          
# OBS: cuidado com a identação, pois ele poderá  influenciar o laço                 
# Aceita outras estruturas de controle aninhadas como o if..else
# exemplo:
print('oi')
for C in range(1, 6): # a contagem do laço ingora a ultima linha fim da contagem 
    print(C)
    print('olá')
print('fim')
# para contar de tras para frente se coloca o decrimento
for b in range (6, 0, -1):
    print(b)
print('-'*20)
# para pular numeros é so modificar o incremento
for a in range(0 ,7, 2):
    print(a)

n = int(input('digite um numero: '))
for x in range (0,n):
    print(x)
print('='*11)
# Pode-se tambem ler todos os comandos do for
i = int(input('Inicio:'))
f = int(input('fim:'))
p = int(input('passo:'))
for z in range (i, f+1, p):
    print(z) # mas lembre-se para contar de tras pra frente deve ser assim (fim, inicio, passo negativo)
print('*'*10)
# Pode-se criar estruturas de contagem especificos
s = 0 # inicio do somatorio
for i in range (0, 3):
    n = int(input(' digite um valor: '))
    s = s + n # ou s += n
print('a soma de tudo é : {}'.format(s))
print('='*10)