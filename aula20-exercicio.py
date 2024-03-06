primeiro_valor = int(input('Digite o valor de A: '))
segundo_valor = int(input('Digite o valor de B: '))

if primeiro_valor > segundo_valor:
    print(f'{primeiro_valor} é maior que {segundo_valor}')

elif primeiro_valor < segundo_valor:
    print(f'{primeiro_valor} é menor que {segundo_valor}')

else:
    print(f'Os valores são iguais')

