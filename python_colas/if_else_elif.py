#if e else

#exemplo if else
tempo = int(input('Quantos anos tem seu carro? '))
if tempo <=3:
    print('carro novo')
else:
    print('carro velho')
print('--FIM--')

#outro exemplo if else
n1 = float(input('Qual foi sua primeira nota ?'))
n2 = float(input('Qual foi sua segunda nota ? '))
media = (n1+n2)/2
if media >= 5:
    print('Parabens tu ta manjando')
else:
    print('Tu é um bosta mermão')

#Outro exemplo if
velocidade = float(input('Qual é a velocidade atual do carro? '))
if velocidade > 80 :
    print('MULTADO! Você excedeu o limite permitido que é de 80Km/h ')
    multa = (velocidade -80) * 7
    print(f'Você deve pagar uma multa de R${multa:.2f}!')
print('Tenha um bom dia e dirija com segurança! ')

#exemplo if para numero impar ou par
número = int(input('Me diga um número qualquer: '))
resultado = número % 2
if resultado == 0:
    print(f'O numero {número} é par ')
else:
    print(f'O numero {número} é impar ')


#exemplo if com and e or
ano = int(input('Que ano quer analisar?'))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0: #!= diferente
    print(f'O ano {ano} é bissexto ')
else:
    print(f'O ano {ano} NAO é bissexto ')


#exemplo if com o lower
nome = str(input('Qual é seu nome? '))
nome = nome.lower()
if nome == 'lucca':
    print('Que nome lindo você tem! ')
else:
    print('Teu nome é tao normal')
print(f'Bom dia, {nome} ')


#exemplo if com random
import random
computador = random.randint(0 , 5)
print('Vou pensar em um numero de 0 a 5 ')
jogador = int(input('Em que numero eu pensei? '))
if jogador == computador:
    print('Você me pegou! ')
else:
    print('Não foi dessa vez! ')


#NOT
#exemplo not
a = ''
b = 2
if not b :
    print('por favor preencha o falor de A.')

#IN
#exemplo in
nome = 'lucca biasoli'
if 'u' in nome:
    print ('Existe a letra U no seu nome ')

#exemplo senha com if and
usuario = input('nome de usuario : ')
senha = input('digite a sua senha : ')

usario_bd = ('lucca')
senha_bd =('1234')

if usuario_bd == usuario and senha_bd == senha:
    print('voce esta logado no sistema ')
else :
    print('Senha incorreta,tente novamente ')

