a = 'AAA'
b = 'BBB'
c = 1.1231432423423424
string = 'a={nome1} b={nome2} c={nome3:.2f}'
formato = string.format(
    nome1=a, nome2=b,  nome3=c
)
print(formato)