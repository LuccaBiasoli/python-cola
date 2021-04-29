#Site para ver todas as bibliotecas:
#https://docs.python.org/3/library/index.html

#exemplo de modulo math
math::::::::::::::::::::
    ceil : arredondamento para cima
    floor: arrendondamento para baixo
    trunc: eliminar da virgula para frente
    pow: potencia igual a **
    sqrt: raiz quadrada
    factorial: calculo fatorial de um numero
import math : para importar tudo de cima
from math import sqrt : para importar somente o sqrt
from math import sqrt , ceil : para importar sqrt e ceil


#exemplo de modulo math raiz quadrada
import math
num = int(input('Digite um numero: '))
raiz = math.sqrt(num)
print(f'A raiz de  {num} é igual a  {raiz}')

#Exemplo igual com arrendondar para cima com ceil
import math
num = int(input('Digite um numero: '))
raiz = math.sqrt(num)
print(f'A raiz de  {num} é igual a  {math.ceil(raiz)}')


#exemplo utilizando biblioteca random randint
import random
num = random.randint(1, 10)
print(num)
exemplo random com if
import random
computador = random.randint(0 , 5)
print('-' *20)
print('Vou pensar em um numero de 0 a 5 ')
jogador = int(input('Em que numero eu pensei? '))
if jogador == computador:
    print('Você me pegou! ')
else:
    print('Não foi dessa vez! ')

#exemplo utilizando biblioteca random choice pra escolher um nome
import random
n1 = str(input('Primeiro aluno : '))
n2 = str(input('Segundo aluno : '))
n3 = str(input('Terceiro aluno : '))
n4 = str(input('Quarto aluno : '))
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print(f'O aluno escolhido foi {escolhido}')


#exemplo utilizando biblioteca random shuffle para escolher aleatoriamente numa sequencia
import random
n1 = str(input('Primeiro aluno : '))
n2 = str(input('Segundo aluno : '))
n3 = str(input('Terceiro aluno : '))
n4 = str(input('Quarto aluno : '))
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print(f'O aluno escolhido foi {lista}')