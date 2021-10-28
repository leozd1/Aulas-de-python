#  Funções (Parte 1)
'''
Função são rotinas personalizadas de comandos considerados rotineiros, que podem ser chamados 
constantemente pelo progrmador, sendo seus maiores exemplos o print(), o len() e input(), além de outros,
também chamados de def (definição de função).
'''
# exemplo pratico 1:
print('------------------------------------')
print('        SISTEMA DE CADASTRO         ')
print('------------------------------------')

def mostraLinha():
    print('\033[1;32m-\033[m'*36)
    
    
mostraLinha()
print('        SISTEMA DE CADASTRO         ')
mostraLinha()
    
'''
As funções podem ser usadas em momentos diferentes do programa. Sendo que toda a vez que a função
é chamado, ele entra dentro da execução do programa da função executa o programa e depois volta 
depois pro programa principal.

Por questão estetica o python difive o programa em duas partes: a função com seu escopo, 
pula-se duas linhas,
e o programa principal, onde escreve-se o programa e chama-se a função para ser executada.
'''
# exemplo pratico 2:
def lin():
    print('\033[1;35m-\033[m'*36)


lin()
print('        SISTEMA DE ALUNOS           ')
lin()
lin()
print('                ALUNOS              ')
lin()

'''
Parametros são estruturas das funções que podem ser personalizadas para receberem entradas de
comandos ou variaveis para serem usadas nas funções
'''
def mensagem(msn):
    print('\033[1;33m-\033[m'*36)
    print(msn)
    print('\033[1;33m-\033[m'*36)

mensagem('{:^36}'.format('SISTEMA ATIVO')) # 

# Exercicios praticos
'''Como aplicar a chamada de função, o def() '''

a = 4
b = 5
s = a+b
print(s)
a = 8
b = 9
s = a+ b
print(s)
a = 2
b = 1
s = a +b
print(s)

def soma(a, b): # a função soma() é criada com a entrada das variaveis a e b para serem chamadas
    print(f'A = {a} e B = {b}')
    s = a + b # o escopo da função, o que ele vai fazer
    print(f'A soma = {s}')
    
# programa principal     = Tenta identificar o programa principal no inicio
soma(4,5) # a entrada dos paramentros (valores) da função chamada
soma(1,2)
soma(3,7) # quando passar os paramentros atente para a quantidade pedida.
soma(b= 7, a= 3) # pode-se mudar a ordem dos parametros recebidos, contanto que seje explicado

# empatamento de paramentros, permite adicionar varios paramentros sem restrições
def contador(*num): # ao adicionar um numero incerto de paramentros o * "desempacota-os" ao 
    print(num)
    tam = len(num)
    print(f'  o tamanho de numeros lidos é {tam}')
    for valor in num: # for aplicado para apenas mostrar a 
        print(f'{valor} ', end='')
    print('FIM')
    
contador(2,6,9,4)
contador(2,5,8)

'''
Podendo ser aplicado em listas, que por ter a vantagem de ser alteravel, mutavél,
que por ser composta de varios valores que são identificaveis por indices, iniciando com 0,
alterando seus valores por rotinas constantes, por funções, que pode ser aplicada em indices espcificos
ou na lista inteira.

Obs: em Python, a passagem de parametros é por referencia, diferente de Java que é por valor.
Sendo que tudo que for feito no valor dos paramentro da função atingira os valores da lista, difierente do
desempacotamento de de valores de parametros.
'''
# exercicio pratico 2
def dobrar(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1
        
valores = [7,4,1,2,6]
print(valores)
dobrar(valores)
print(valores)