# Tratamento de Erros em Python
'''
 Pertencente a uma biblioteca que é disparada automaticamente ao detectar um erro no 
codigo da programação, como a sintaxe da escrita, tipos de variaveis ou valores, nomes 
de variaveis, o Exception, conhecido tambem como excessão de erros, não prejudicando o 
codigo em si, mas apenas descrição do tipo de exceção e a linha onde é localizada.
Os tipos de exceções, mas comumente os de sintaxes, são geralmente são aplicados 
quando há erro na escrita, assim como os de "typeError", os erros de tipo, quando
os tipos de variaveis são trocados "acidentalmente", alem de outros que são tratados pela
classe propria chamada Exception, que permite avaliar o erro, ou exceção, do programa
para saber se implicará numa interferencia maior. A aplicação do Try (tente) e o except(senão...
falha) serve para realizar o teste do possivel erro antes do mesmo acontecer, onde o try testará
a exceção, e se falhar disparará o except com uma mensagem ou comando.
'''
# exemplo: 
try: # tente realizar a operação
    a = int(input('numeroador: '))
    b = int(input('denominador: '))
    r = a/b
# except: # se falhar mande a mensagem 
    # print('Infelizmente não da pra dividir!')
except Exception as error: # onde é mostrado o tipo de erro com a classe Exception inserida 
    print(f'O erro encontrado foi {error.__class__}')
else: # senão(...se funcionar)
    print(f'Resultado da divisão é {r}')
finally: # finalmente (indepedente se der certo ou falhar)
    print('Volte sempre!')
    
'''
Else: será usado de forma opcional para informar caso der certo o teste feito pelo Try
Finally: é usado comumente para fechar um banco de dados ou um arquivo, sempre finalizando o programa.

Permitindo mostrar mensagens personalizadas de erro, facilitando a legibilidade do codigo,
onde todo try pode ter mais de um except, para varios tipos de exceção, como o TypeError,
o ValueError, OSError, etc. Onde cada except tera seu prorio tratamento.

Da mesma forma casa ação do programa pode ter um try para testar um erro
'''
# exemplo 2:
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a/b
except (ValueError, TypeError): # permite-se mais de um tipo de Erro na exceção
    print('Tovemos problemas com os tipos de valores digitados')
except ZeroDivisionError: # alem de permitir mais de uma exceção no try
    print('Não é possivel dividor por zero!')
except KeyboardInterrupt: # quando não se diita nada no teclado
    print('O usuario não digitou nada')
else: 
    print(f'Resultado da divisão é {r}')
finally: 
    print('Volte sempre!')
    
