#Manipulando texto

#exemplo len (de lenght)
len(frase)
    vai ler o total de palavras na frase
exemplo:
    frase = 'curso em video python'
    print(len(frase))
junçao de len e strip:
    frase = 'curso em video python'
    print(len(frase.strip()))
#OUTRO EXEMPLO LEN
usuario = input('digite seu usuario:')
qtd_caracteres = len(usuario)
if qtd_caracteres < 6:
    print ('voce precisa digitar pelo menos 6 numeros ')
else:
    print('voce foi cadastrado no sistema')
#outro exemplo len com soma de duas string
string1 = input('digite alguma coisa ')
string2 = input('digite outra')
print(f'a quantidade total de letras foi {len(string1) + len(string2)}')


#exemplo count
frase.count('x')
    vai contar quantas vezes tem a palavra x
frase.count('x',0,13)    conta quantos X tem do 0 ao 12
exemplo :
    frase = 'curso em video python'
    print(frase.count('o'))
    
#junçao de lower com count exemplo
frase = 'curso em video python'
print(frase.lower().count('o'))

#exemplo find
frase.find('xyz')
vai procurar em qual posiçao esta xyz e mostrar
se o valor resultado for -1 significa que nao foi encontrado

#exemplo in
'xyz'infrase
vai aparecer true se tiver xyz na frase





#TRANSFORMAÇAO

#exemplo replace
frase.replace('python','android')
    vai trocar onde tem escrito python,por android
exmplo:
    frase = 'curso em video python'
    print(frase.replace('python', 'Android'))
exemplo pra salvar como variavel:
    frase = 'curso em video python'
    frase = frase.replace('python', 'Android')
    print(frase)
    
#exemplo upper
frase.upper()
vai deixar todas as letras maiusculas

#exemplo lower
frase.lower()
vai deixar todas as letras minusculas
Exemplo lower com o if

nome = str(input('Qual é sue nome? '))
nome = nome.lower()
if nome == 'gustavo':
    print('Que nome lindo você tem! ')
print(f'Bom dia, {nome} ')


#exemplo capitalize
frase.capitalize()
vai deixar tudo minusculo menos a primeira letra,que vai ficar maiuscula

#exemplo title
frase.title()
palavras por palavras na frase,as primeiras letras de cada palavra vao ficar maiusculas

#exemplo strip
frase.strip()
vai remover os espaços inuteis no começo e final da frase,sem utilidade
#exemplo rstrip
vai remover os espaços do final somente (r de right)
#exemplo lstrip
vai remover os espaços do começo (l de left)



#exemplo split
frase.split()
vai dividir em blocos numerados de acordo com o espaço para terminar uma palavra
exemplo:
    frase = ('curso em video python')
    print(frase.split())
#exemplo join
'-'join(frase)
vai colocar o  -    no lugar do espaço em todas as ocasioes




#exemplos na pratica
frase = ('curso em video')
print(frase[3])
    vai mostrar a quarta letra

frase = ('curso em video')
print(frase[3:13])
    vai da quarta letra ate o 12
frase = ('curso em video')
print(frase[3])
    vai do começo ate a 12 letra
frase = ('curso em video')
print(frase[13:])
    vai da letra 13 ate o final
frase = ('curso em video')
print(frase[1:14])
    vai da letra 1 ate a 14
frase = ('curso em video')
print(frase[1:15:2])
    vai pulando de 2 em 2 ate o 15

#placeholder
pass usado como placeholder pro codigo funcionar e depois alterar o pass
