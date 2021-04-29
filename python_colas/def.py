#def = serve para definir funções onde terá uma sequencia de comandos e quando
quando você precisar dessas sequência em alguma parte do programa basta
chama-la que ela vai executar a função que você definiu

#return

#args



#todos os tipos de def
def jogador_de_futebol():
    print('o nome dele é neymar')


jogador_de_futebol()
////////////////

def jogadorzin(nome):
    print(nome)


jogadorzin('neymar')
////////////////

def jogadorzao(nome):
    return nome


jogadorz = jogadorzao('Taffarellll')
print(jogadorz)
////////////////


#exemplo basico criando variavel chamada funcao() e chamando ela depois
def funcao():
    print('Olá mundo!')

funcao()
funcao()

#exemplo def list for in
def fim_de_game(pessoa):
    print(pessoa)


list_Time = ['ggwp rafael','ggwp lucca','ggwp matheus','ggwp andre']

for pessoa in list_Time:
    fim_de_game(pessoa)



#exemplo def
def fim_de_game(cumprimento, pessoa):
    print(cumprimento, pessoa)

fim_de_game('GGWP' , 'PainGaming')
fim_de_game('GG' , 'INTZ')
fim_de_game('BG', 'CHEATERS')


#exemplo def return
def divisao(n1,n2):
    return n1/n2

divide = divisao(8,2)
print(divide)

#exemplo def com 2 return
def divisao(n1, n2):
    if n2 == 0:
        return

    return n1/n2

divide = divisao(8,4)

if divide:
    print(divide)
else:
    print('Conta inválida.')



#exemplo def com soma
def soma(n1,n2,n3):
    print(n1 + n2 + n3)

soma(2,1,3)
soma(1,1,1)
soma(2,1,1)



#exemplo def return percentual
def aumento_percentual(valor, percentual):
    return valor + (valor * percentual) /100

ap = aumento_percentual(50, 10)
print(ap)
ap = aumento_percentual(100, 10)
print(ap)
ap = aumento_percentual(10, 10)
print(ap)
ap = aumento_percentual(15, 100)
print(ap)


#def lista args
def func(*args):
    print(args)

lista = [1,2,3,4,5]
n1, n2, *n = lista
print(n1, n2, n)



#def com f'
def time_basquete(time):
    return f'Bem vindo a liga {time}'

saudacao = time_basquete('palmeiras')
print(saudacao)


#def return f'  (a parte escrita no return so sera utilizada na primeira vez que o def for chamado)
def time_basquete(time):
    print('A janela de transferencias acabou')
    print('E o time a entrar na liga sera: ')
    return f'Bem vindo a liga {time}'

saudacao = time_basquete('palmeiras')
print(saudacao)



#def com return conta matematica
def soma (num1,num2):
    return num1 * num2


calculo = soma(4,6)
print(calculo)