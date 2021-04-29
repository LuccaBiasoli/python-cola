#lista
lista = ['chave', 'foda', 8]
lista[1] = 'kkkk'
print (lista[1])


#lista EXTEND para expandir a lista sem criar um L3
l1 = [1,2,3]
l2 = [4,6,7]
l1.extend(l2)

print(l1)
print(l2)


#lista append ou extend colocando uma str a mais (append no final)
l1 = [1,2,3]
l2 = [4,6,7]
l1.append('a')  #no lugar de append pode ser extend,colocando no final

print(l1)
print(l2)

#lista insert para inserir no local desejado
l1 = [1,2,3]
l2 = [4,6,7]
l1.insert(0,'a')

print(l1)
print(l2)


#pop   (para retirar o ultimo elemento da lista)
l2 = [4,5,6]
l2.insert(0, 'banana')
l2.pop()
print(l2)


#del para deletar elementos da lista
l2 = [1,2,3,4,5,6,7,8,9]
del(l2[3:5])          (vai retirar o 4 e o 5 ,nas posiçoes 3 e 4)


#max e min
l2 = [1,2,3,4,5,6,7,8,9]
print(max(l2))         (para pegar o maior numero da lista)
print(min(l2))          (para pegar o menor numero da lista )




#lista def sort (sort para colocar na ordem menor pra maior)

lista = [

        ['p1',13],
        ['p2',6],
        ['p3',7],
        ['p4',50],
        ['p5',8],
]

def func (item):
    return item[1]

lista.sort(key=func)
print(lista)



#lista def sort reverse (sort reverse para colocar do maior pro menor)

lista = [

        ['p1',13],
        ['p2',6],
        ['p3',7],
        ['p4',50],
        ['p5',8],
]

def func (item):
    return item[1]

lista.sort(key=func, reverse = True)
print(lista)


#lista lambda  sort (mesmo que o de cima mas lambda no lugar de def)

lista = [

        ['p1',13],
        ['p2',6],
        ['p3',7],
        ['p4',50],
        ['p5',8],
]



lista.sort(key=lambda item:[1])
print(lista)
