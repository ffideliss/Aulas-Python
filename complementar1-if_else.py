numero = 3

if numero > 1: # 10 é maior que 1? se sim então entra na condição abaixo
    if numero > 2: # 10 é maior que 2? se sim então entra na condição abaixo
        if numero > 3: # 10 é maior que 3? se sim então entra na condição abaixo   
            print('Número maior que 3') # exibe o resultado na tela (qualquer numero acima ou igual a 3.1 cairia nessa condição)
        else:
            print('Número menor que 3')  # caso o numero fosse 3 ou menos cairia nessa condição e seria exibido esse resultado
    else:
        print('Número menor que 2') # caso o numero fosse 2 ou menos cairia nessa condição e seria exibido esse resultado
else:
    print('Número menor que 1') # caso o numero fosse 1 ou menos cairia nessa condição e seria exibido esse resultado