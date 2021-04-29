#pergunta a resposta usando dicionario for e if

print()
print('Texto explicativo.')

perguntas = {
    'pergunta 1': {
        'pergunta': 'quanto é 2+2? ',
        'respostas': {'a': '1','b': '4','c': '5', },
        'resposta_certa': 'b',
     },
    'pergunta 2': {
        'pergunta': 'quanto é 3*2? ',
        'respostas': {'a': '4', 'b': '10', 'c': '6', },
        'resposta_certa': 'c',
    }
 }
print()

respostas_certas = 0

for perguntaA, perguntaV in perguntas.items():
    print(f'{perguntaA}: {perguntaV["pergunta"]}')

    print('respostas: ')
    for respostaA, respostaV in perguntaV['respostas'].items():
        print(f'[{respostaA}]: {respostaV}')

    resposta_usuario = input('Sua resposta: ')

    if resposta_usuario == perguntaV['resposta_certa']:
        print('Ebaa voce acertou!!')
        respostas_certas += 1
    else:
        print('ixi vc errou')
    print()

qtd_perguntas = len(perguntas)
porcentagem_acerto = respostas_certas / qtd_perguntas * 100

print(f'Voce acertou {respostas_certas} perguntas.')
print(f'Sua porcentagem de acerto foi de {porcentagem_acerto} por cento ')