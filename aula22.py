# Módulos e Pacotes
'''
Modularização, ate de criar módulos, criado na decada de 60, onde os sistemas estavam
ficando maiores para armazenas em um único programa, cujo o foco são: 
-dividir um programa grande em partes pequenas, 
-aumentar a legibilidade, que permite encontrar linhas de de programação com mais facilidade dentro do programa,
-além de facilitar a organização,
-facilitando assim a manutenção do sistema em si,
-permite a ocutação do código, facilitando,
-e reutilzar meus módulos em outros projetos.

Um dos maiores exemplos de modularização é a criação de função, como o 'Fatorial', já 
que não existe uma função especifica dele.

Todo arquivo .py, desde que tenha funções, pode ser importado
Obs: deve ser usado com cuidado, pois pode apresentar incompatibilidade
     pois pode haver mais de um módulo (biblioteca) no python, o que
     pode provocar erros.

Pacote é uma pasta de modulos separados por assuntos, organizando assim o excesso 
de módulos, cuja a importação é feita da mesma fomra que um import de uma biblioteca
normal, assim como o módulo. 
Ex: 
import aula22bModulo - ou
from aula22bModulo import fatorial - da mesma forma que o modulo, a importação do
pacote é feita com imprt, usando o from para especificar a funcionalidade que será
usada.

# Pacote
Para se criar um pacote, basta criar destro do projeto uma pasta com o nome do pacote,
e suas definições, ou assunto separado, tambem sera por pasta, e os módulos dentro destas
pastas. Deixando apenas os pacotes e suas subpastas para arquivos, ou módulos muito grandes,
sendo usado uma sintaxe de nome de arquivo (_ _init_ _.py), para "iniciar" os programas 
dos pacotes e suas subpastas, sendo criado automaticamento em cada pacote e subpasta,
por isso deve-se atentar de qual pasta vai se "iniciar" o arquivo init.
'''
# Exemplos:
'''
import do modulo do Fatorial, dobro e do triplo 
Obs: o modulo esta na pasta numeros, dentro da pasta aula22Pacote, no arquivo __init__.py
'''
# import aula22bModulo  
'''
Por ser um import o modulo deve ser especificado,
para evitar a incompatibilidade.
'''

from aula22Pacote import numeros
'''
Ao importar um pacote, chama-se a pasta principal e depois a subpasta, para
para então chamar a função. (algo como mostrar o caminho da função que está dentro
da subpasta que ta dentro da pasta), tratado da mesma forma que o módulo.

O arquivo (_ _init_ _.py) serve guardar os programas dos pacotes, como substituto dos 
modulos, preste atenção de qual pasta vai chamar o arquivo init, e lembre-se em criar 
esse arquivo se for criar pacotes.

Obs: o modulo esta na pasta numeros, dentro da pasta aula22Pacote, no arquivo __init__.py
'''

# programa principal
num = int(input('Digite um valor: '))
fat = numeros.fatorial(num) # a subpasta numeros com a função fatorial
print(f"O fatorial de {num} é {fat}")
print(f'O dobro de {num} é {numeros.dobro(num)}')
