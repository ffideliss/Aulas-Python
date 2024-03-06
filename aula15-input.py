#input é usado para coletar dados do usuário

#nome = input('Qual o seu nome? ')
#print (f'O seu nome é {nome}')

numero_1 = input('Digite um número: ') # a coleta de dados é feita em str
numero_2 = input('Digite outro número: ')

int_numero_1 = int(numero_1) #coercao do numero_1 que está em str para int
int_numero_2 = int(numero_2)

print(f'A soma dos números é: {int_numero_1 + int_numero_2}')