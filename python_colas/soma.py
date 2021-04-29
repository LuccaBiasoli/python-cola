#exemplo1
n1 = input ('digite um numero ')
n2 = input ('digite outro numero')
s = int(n1) + int(n2)
print ('a soma de ', n1 , 'com ', n2, 'da ',s)



#exemplo2
n1= int(input('Digite um valor : '))
n2= int(input('Digite outro : '))
s = n1 + n2
print('A soma entre ', n1, 'e',n2,' vale ',s)


#exemplo3 que é o exemplo2 com format
n1= int(input('Digite um valor : '))
n2= int(input('Digite outro : '))
s = n1 + n2
print('A soma entre {0} e {1} vale {2}'.format(n1, n2, s))


#exemplo4 que é o exemplo 3 com format diferente
n1= int(input('Digite um valor : '))
n2= int(input('Digite outro : '))
s = n1 + n2
print(f'A soma entre {n1} e {n2} vale {s}')




#ordem de precedencia de operadores aritmeticos

1: ()
2:  ** #exponencia
3: * /  // %
4: + -


#exemplo de ordem de precedencia com varias contas
n1 = int(input('digite um numero:'))
n2 = int(input('digite outro numero :'))
s= ((n1+n2)/2)*5
print(s)

outro exemplo:
pagamento = (dias * 60) + (km * 0.15)



#exemplo para diminuir as cadas depois do ponto
{n1*2:.2f}
foco no :.2f


#exemplo com raiz quadrada:
{n1**(1/2)}


#exemplo porcentagem
5 por cento de n1
n1*5)/100
10 por cento de n1
n1*5)/100

fazer o desconto de um produto :
preço = float(input('qual o preço do produto ? r$'))
novo = preço - (preço *5 / 100)
