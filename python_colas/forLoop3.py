contador = 0
lista = []
listao = []
while contador < 5:
    pergunta = input('quantas vezes?')
    time = input('qual o time')
    lista.append(pergunta)
    listao.append(time)
    
    contador += 1


for v in zip(lista, listao):
    print(v)

