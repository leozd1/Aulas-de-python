# Estrutura de Repetição
# Con teste Lógico 
# WHILE (enquanto ... ate...), outra forma de limitação de repetição
# onde o while testa cada repetição para atender uma condição especifica,
# saindo do laço se (ou não) a condição for atendida.
# 
'''
Exemplo:
portugol                                python
enquanto não maça:                    while nor maça:
    se tiver chão,                      if chão:
        passo                               passo
    se tiver buraco,                    if buraco:
        pula                                pula
    se tiver moeda,                     if moeda:
        pega                                pega
pega(fim)                               pega
'''
# Exemplo pratico 1
'''
for c in range (1, 5):
    print(c)
print('Fim')
print('-'*20)
c = 1
while c < 5: # condição de contagem (repetição)
    print(c)
    c += 1 # para ele somar o contador na volta e manter o controle da repetição, 
    # senão ele continuará a repetição eternamente (ou ate o fim da memoria)
print('Fim')
'''
# Exemplo pratico 2
'''
for c in range (1,2): # o for i in range (inicio, fim), necessita de um limite 
    n = int(input('Digite um numero: '))
print('Fim')
print('-'*30)
n = 1
while n != 0: # n!=0 (chamado de flag, é a condição de parada do laço de repetição)
    n = int(input('Digite um numero: '))
print('Fim')
print('-'*30)
'''
# Exemplo pratico 3
'''
r = 'S' # inicializador do laço (a variavel que explica o inicio do laço)
while r =="S": # flag que controla o laço (enquanto r for 'S' o laço continua, senão o laço termina)
    n = int(input('Digite um numero: '))
    r = str(input('Quer continuar? [S/N]')).upper()
print('Fim')
'''
# Exemplo pratico 4

n = 1
par = impar = 0 # forma preguiçosa de "receber" mais de uma variavel (evitar)
while n != 0:
    n = int(input(" Diigite um numero: "))
    if n != 0: # so use se achar que zero não é um numero PAR pra contabilizar (¯\(°_o)/¯)
        if n % 2 == 0:
            par +=1
        else:
            impar += 1
print(" Numero digitados: \n Par: {}\n Impar: {}".format(par, impar))
