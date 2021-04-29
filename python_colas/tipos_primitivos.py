#tipo primitivos e saida de dados

#int sao : numeros inteiros ex 7   -4   0  82139
estrutura do int para testar:
    
n1 = int(input('Digite um valor: '))
print(type(n1))
print(n1)


#float sao: numeros reais ex  4.5    0.076    -15.25
estrutura do float para testar:

n = float(input('Digite um valor: '))
print(type(n))
print(n)



#bool sao: True ou False
n = input("Digite qualquer coisa : ")
print(bool(n))

n = input('digite um valor : ')
print(n.isnumeric()) # para ver se é numerico

n = input('digite um valor : ')
print(n.isalpha()) #para ver se é palavra



#str sao : palavras entre aspas ex  : 'ola'  '7.5'  ''  
n1= str(input('Fale um nome : '))
print(type(n1))




#exemplo de codigo usando int e str
dia = int(input('Qual dia?'))
mes = str(input('qual mes?'))
ano = int(input('Qual ano?'))

print(f'Voce nasceu no dia {dia}, de {mes} do ano {ano} ')