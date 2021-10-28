# Exercicio 113
# Reescreva a função leiaInt() que fizemos no desafio 104,
# incluindo agora a possibilidade da digitação de um número de tipo inválido.
# Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
'''
def leiaInt(num):    
    while True:
        try:
            entrada = int(input(num))            
        except (TypeError, ValueError):
            print(f'\033[1;31m ERRO: Digite um valor inteiro\033[m') 
            continue # apos o teste ele joga no laço novamente para testar    
        except (KeyboardInterrupt): # caso queria interronper com (ctrl + c), que ele retorna um 0
            print('Entrada de dados interronpida pelo usuario')
            return 0    
        else:
            return entrada    
        
def leiaFLoat(num):
    while True: # enquanto for verdadeiro
        try: # teste essa entrada
            entrada = float(input(num))
        except (TypeError, ValueError): # se der erro, manda o print
            print(f'\033[1;31m ERRO: valor invalido, tente novamente!\033[m') 
            continue # e volta pro inicio do laço
        except (KeyboardInterrupt): # caso queria interronper com (ctrl + c), que ele retorna um 0
            print('Entrada de dados interronpida pelo usuario')
            return 0
        else: # mas se der certo, retorne a entrada
            return entrada

# programa principal
p = leiaInt("Digite um valor inteiro: \n")
x = leiaFLoat('Digire um valor em float: \n')
print(f'O valor inteiro digitado foi {p} e o valor real foi {x}')
'''

# Exercicio 114
# Crie um código em Python que teste se o site pudim está acessível pelo computador usado.
# http://pudim.com.br/
'''
import urllib # biblioteca para verificar endereços (url's)
import urllib.request # requisição de url's

try:
    site = urllib.request.urlopen('http://pudim.com.br') # a biblioteca de url requesita abrir uma url 
except urllib.error.URLError:
    print('Site não funciona, tente mais tarde!')
else:
    print('Site funciona!')
    print(site.read()) # permite ler o conteudo em html do site (sem necessidade, por hora.)
'''

# Exercicio 115a e 115b 
# Vamos criar um menu simples em Python, usando modularização
'''
from time import sleep
from aula23bPacote.interface import *

cabeçalho('SISTEMA ARQUIVO V.1.0')
while True: # um laço para escolher as opções da lista 
    resposta = menu(['CADASTRAR', 'LISTAR', 'EXCLUIR', 'SAIR DO SISTEMA'])
    if resposta == 1:
        cabeçalho('Você escolheu 1','vermelho') # coloquei uma corzinha no resultado da opção
    elif resposta == 2:
        print('Você escolheu a 2')
    elif resposta == 3:
        print('Você digitou 3')
    elif resposta == 4:
        cabeçalho("Você decidiu sair do sistema...Bye bye!",'branco') # o cabeçalho so pra deixar bonitinho
        break
    else:
        print('\033[1;31;43mVocê digitou errado... Tente novamente\033[m')
    sleep(1.7) # da uma pausa antes de reiniciar o laço
    '''
    
# Exercicio 115b
# Vamos ver como fazer acesso a arquivos usando o Python.
# disponivel no arquivo __init__.py da pasta arquivo.
'''
from time import sleep
from aula23bPacote.interface import *
from aula23bPacote.arquivo import *

arq = 'cursoemvideo.txt' # nomeia o arquivo

# if arquivoExiste(arq): # verifica se o arquivo existe pela função
#    print('Arquivo encontrado com sucesso!')
#else: # se ele não existir, cria o arquivo
#    print('Arquivo não encontrado!')
#    criarArquivo(arq)
    
if not arquivoExiste(arq): # se arquivo não existir, cria ele
    criarArquivo(arq)
    

while True: # um laço para escolher as opções da lista 
    resposta = menu(['CADASTRAR', 'LISTAR', 'EXCLUIR', 'SAIR DO SISTEMA'])
    if resposta == 1:
        cabeçalho('Você escolheu 1','vermelho') # coloquei uma corzinha no resultado da opção
        # essa opção ainda não existe, tenha calma
    elif resposta == 2:
        print('Você escolheu a 2')
        # opção de listar o conteudo do arquivo
        lerArquivo(arq)
    elif resposta == 3:
        print('Você digitou 3')
        # remove todo o conteudo logo, tem que ter outro jeito?
        excluirArquivo(arq)
    elif resposta == 4:
        cabeçalho("Você decidiu sair do sistema...Bye bye!",'branco') # o cabeçalho so pra deixar bonitinho
        break
    else:
        print('\033[1;31;43mVocê digitou errado... Tente novamente\033[m')
    sleep(1.7) # da uma pausa antes de reiniciar o laço
'''
    
# Exercicio 115c
# Vamos finalizar o projeto de acesso a arquivos em Python.    
from time import sleep
from aula23bPacote.interface import *
from aula23bPacote.arquivo import *

arq = 'cursoemvideo.txt' # nomeia o arquivo
    
if not arquivoExiste(arq): # se arquivo não existir, cria ele
    criarArquivo(arq)  

while True: # um laço para escolher as opções da lista 
    resposta = menu(['CADASTRAR', 'LISTAR', 'EXCLUIR', 'SAIR DO SISTEMA'])
    if resposta == 1:
        cabeçalho('Você escolheu 1','vermelho') # coloquei uma corzinha no resultado da opção
        # cadatra pessoas
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ') # para aceitar somente numero inteiro
        cadastrar(arq, nome, idade) # vai cadastrar no arquivo, os nomes e idades
    elif resposta == 2:
        cabeçalho('Você escolheu a 2', 'verde')
        # opção de listar o conteudo do arquivo
        lerArquivo(arq)
    elif resposta == 3:
        print('Você digitou 3')
        # remove todo o conteudo logo, tem que ter outro jeito, procura ae!
        excluirArquivo(arq)
    elif resposta == 4:
        cabeçalho("Você decidiu sair do sistema...Bye bye!",'branco') # o cabeçalho so pra deixar bonitinho
        break
    else:
        print('\033[1;31;43mVocê digitou errado... Tente novamente\033[m')
    sleep(1.7) # da uma pausa antes de reiniciar o laço