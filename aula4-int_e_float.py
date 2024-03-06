"""
int -> numero inteiro
o tipo int representa qualquer numero
positivo ou negativo, int sem sinal é considerado positivo.

float -> numero com ponto flutuante
o tipo float representa qualquer número
positivo ou negativo com ponto flutuante.

A função type mostra o tipo que o python 
inferiu o valor
"""
print(11) #int
print(-11) #int
print(0) #int

#sempre use . (ponto) para separar as casas decimais
print(1.1, 10.11) #float
print(0.0, -1.45) #float
print(type('Fidelis'))
print(type(1))
print(type(1.0657), type(-23), type(0))