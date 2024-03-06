"""
operadores: not --> inverter  expressões

and = (e) or (ou) not (não)
todas as condições precisam ser verdadeiras.
"""
entrada = input('Escolha uma das poções: \n[E] Entrar \n[S] Sair')
senha_salva = '1234'

if entrada  == 'E' or entrada == 'e':
    print('Bem-vindo! Área restrita')
    senha = input ('Digite sua senha: ')
    if not senha:
        print('É preciso digitar sua senha!')
    elif senha == senha_salva:
        print('Bem-vindo!')
    else:
        print('Senha invalida! tente novamente.')
elif entrada  == 'S' or entrada == 's':
    print('Até mais!')
else:
    print('digite uma opcao valida')