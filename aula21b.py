# Exercicio 101
# Crie um programa que tenha uma função chamada voto() 
# que vai receber como parâmetro o ano de nascimento de uma pessoa,
# retornando um valor literal indicando se uma pessoa tem
# voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
'''
from emoji import emojize # só pra praticar, SQN (^_^)

def voto(ano):
    from datetime import date 
    """
    # ao importar uma biblioteca, depedendo de onde ela esta
    # Ela sera usada pelo programa inteiro, mas se ficar dentro
    # da função, ela só funcionará durante a execução, economi-
    # zando memoria.
    """
    atual = date.today().year # não cooque parenteses no year 
    idade = atual - ano         
    if idade < 16:              
        return emojize(f'{idade} anos: NÂO PODE VOTAR :rosto_gritando_de_medo:', language='pt') # observe que o return pode retornar um 'print()'
    elif 16<= idade <= 18 or idade > 65:
        return emojize(f'{idade} anos: VOTO OPCIONAL :rosto_sorridente_com_óculos_escuros:', language='pt')
    else:
        return emojize(f'{idade} anos: VOTO OBRIGATÓRIO :rosto_de_palhaço:',language='pt')
    
#programa principal = lembre-se de definir (separar), quem é quem
nasc = int(input('Qual o ano de nascimento: \n'))
print(voto(nasc))
'''
# Exercicio 102
# Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
# o primeiro que indique o número a calcular e outro chamado show,
# que será um valor lógico (opcional) indicando se será mostrado ou não na tela
# o processo de cálculo do fatorial.
'''
def fatorial(num, show = False): # valor opcional, mostra ou não
    """
    > Realiza o Fatorial de um numero, com resultado na tela.
    :param num: numero a ser calculado.
    :param show: (opcional) Mostra ou não a conta.
    :return: O valor Fatorial de um numero n.
    """
    f = 1 # variavel local (so existe dentro da função)
    for c in range( num, 0, -1):
        if show:
            print(c, end=' ')
            if c >1:
                print(f' x ', end=' ')
            else:
                print(' = ', end=' ')
        f *= c
    return f

# programa principal
help(fatorial)
print(fatorial(5, show=True))
'''

# Exercicio 103
# Faça um programa que tenha uma função chamada ficha(),
# que receba dois parâmetros opcionais:
# - o nome de um jogador e quantos gols ele marcou.
# O programa deverá ser capaz de mostrar a ficha do jogador,
# mesmo que algum dado não tenha sido informado corretamente.
'''
def ficha(nome= '', gols= 0):
    """
    > Mostra o nome e qunatidade de gols marcados, com resultado na tela.
    :param nome: (opcional) nome do jogador ou não.
    :param gols: (opcional) Mostra ou não a quantidade de gols feitos.
    :return: O valor pedido.
    """
    if nome == '' and gols =='':
        nome = '<desconhecido>'
        gols = 0
    elif nome =='' and gols != '':
        nome = '<desconhecido>'
        gols = gols
    elif nome != '' and gols == '':
        nome = nome
        gols = 0
    else: 
        nome = nome
    return f'O jogador {nome} fez {gols} gols na partida'    
        
    
# programa principal
no = str(input('Digite o nome do jogador: \n'))
gol = input('Quantos gols feitos: \n')
print('\033[0;35m==\033[m'*20)
print(ficha(no,gol))

# Resolução do professor
def fichi (n = '<desconhecido>', g = 0): # subistituira os valores, em caso de não serem usados
    print(f'O jogador {n} fez {g} gol(s) na partida')
# programa principal
jog = str(input('Digite o nome do jogador: \n'))
gol = str(input('Quantos gols feitos: \n'))
if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0
if jog.strip() =='':
    fichi(g = gol)
else:
    fichi(jog, gol)
'''

# Exercicio 104
# Crie um programa que tenha a função leiaInt(),
# que vai funcionar de forma semelhante 'a função input() do Python,
# só que fazendo a validação para aceitar apenas um valor numérico.
'''
def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric(): # verifica se o valor é um numero
            valor = int(n) # o valor se transforma em um numero inteiro
            ok = True # e o ok se tranforma em true, ouseja, fica "ok"
        else:
            print('\033[1;31mERRO! não é um numero, tente denovo!\033[m')
        if ok: # se o ok está "ok", da um break
            break
    return valor
    
# programa principal
n = leiaInt('Digite um numero: \n')
print(f'Você digitou {n}')
'''

# Exercicio 105
# Faça um programa que tenha uma função notas()
# que pode receber várias notas de alunos 
# e vai retornar um dicionário com as seguintes informações:
# – Quantidade de notas 
# – A maior nota
# – A menor nota
# – A média da turma
# – A situação (opcional)
# Adicione também as docstrings dessa função para consulta pelo desenvolvedor.
'''
def notas(*n, situa = False): # a situação é false por que não tem situação
   """
   > Funcao para avaliar notas e a situacao de varios alunos 
   :param n: recebe uma mou mais notas (acita varias) 
   :param situa: valor opcional, indica a situação
   return: docionario com varias informacoes
   """
   res = dict()
   res['total'] = len(n)
   res['maior'] = max(n)
   res['menor'] = min(n)
   res['media'] = sum(n) / len(n)
   if situa:
       if res['media'] >= 7:
           res['Situação'] = 'BOA'
       elif res['media'] >= 5:
           res['Situação'] = 'RAZOAVEL'
       else:
           res['Situação'] = 'RUIM'
   return res
    
# programa principal
resp = notas(2.6, 6.7, 3.5, 2, situa= True)
print(resp)
help(notas)
'''
# Exercicio 106
# Faça um mini-sistema que utilize o Interactive Help do Python.
# O usuário vai digitar o comando e o manual vai aparecer.
# Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará.
# Importante: use cores.
'''
from time import sleep # para realizar importes globais, coloque fora dos comandos e funções
c = ('\033[m',        # 0 -sem cor
     '\033[0;30;41m', # 1 -vermelho
     '\033[0;30;42m', # 2 -verde
     '\033[0;30;43m', # 3 -amarelo
     '\033[0;30;44m', # 4 -azul
     '\033[0;30;45m', # 5 -roxo
     '\033[7;40m'     # 6 -branco
     ); # o mesmo com a lista, ela é global

def ajuda(com): # uma função traduzida, apenas 
    titulo(f'Acessando o manual do comando \'{com}\'',4)
    print(c[6], end=' ') # não esqueça o espaço no end, senão ele nao reconhece
    help(com)
    print(c[0]) 
    sleep(2)
    
def titulo(msg, cor=0): # criação de um print de cores formatado
    tam = len(msg) + 4  # que vai ler o tamanho da mensagem + 4 espaços
    print(c[cor], end=' ')
    print('~'*tam) 
    print(f'  {msg}') # com mais 2 espaços pra alinhar
    print('='*tam)
    print(c[0])
    sleep(1)
    

# programa principal
comando = ''
while True:
    titulo('TÍTULO DE AJUDA PyHelp',2)
    comando = str(input("Função ou Biblioteca > "))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('TE LOGO!',1)
'''
