"""
operadores: or
and = (e) or (ou) not (não)
todas as condições precisam ser verdadeiras.
"""
entrada = input('Digite [E] Entrar e [S] sair: ')
senha_digitada = input('senha: ')
senha_permitida = '123456'

# if condicao True:
if (entrada  == 'E' or entrada == 'e') and senha_digitada == senha_permitida :
    print('Logado com sucesso!')
else:
    print('Sair')