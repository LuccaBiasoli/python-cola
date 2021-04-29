dicionario : nao é alterado se criado uma variavel depois,tanto a variavel
quanto o dicionario vao ficar com a ultima alteraçao

#exemplo basico de dicionario

d1 = dict(chave1='Valor da chave',chave2='valor da chave2')
print(d1['chave1'])




#exemplo basico de del no dicionario

d1 = dict(chave1='Valor da chave',chave2='valor da chave2')
del d1['chave1']
print(d1)



#dicionario com for in values (para mostrar os valores depois do : )
#(sem o values vai mostrar antes do :
#items no lugar de values vai mostrar os dois

d1 = {
    'chave1': 'valor1',
    'chave2': 'valor2',
    'chave3': 'valor3',

}

for v in d1.values():
    print(v)


#criando dicionarios dentro de dicionarios e mostrando em ordem para baixo
    
clientes = {
    'cliente1' : {
        'nome' : 'luiz',
        'sobrenome' :'otavio',
    },
    'cliente2' : {
        'nome' : 'lucca',
        'sobrenome' : 'biasoli',
    },
    'cliente3' : {
        'nome' : 'rafael',
        'sobrenome' : 'reis',
    },
}

for clientes_k, clientes_v in clientes.items():
    print(f'Exibindo {clientes_k}')
    for dados_k, dados_v in clientes_v.items():
        print(f'\t{dados_k} = {dados_v}')


#import copy deepcopy (serve para na variavel copia ,nao alterar o dicionario
#assim o dicionario continua com o valor intacto nao importa oq a copia mude

import copy

d1 = {1: 'a', 2: 'b', 3: 'c', 'd' : ['luiz', 'otavio']}
v = copy.deepcopy(d1)

v[1] = 'luiz'
v['d'][0] = 'joaozinho'

print(d1)
print(v)


#pop serve para deletar a parte que eu escolher

lista = { 1 : 2 , 'foda' : 'sim',}
lista.pop('foda')
print(lista)


#update serve para juntar os dois dicionarios

lista = { 3 : 'aham' , 'foda' : 'sim',}
listinha = {1:'sim', 2 :' falo nada'}
lista.update(listinha)
print(lista)
print(listinha)