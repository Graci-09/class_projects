print("""Para formar um triângulo, precisamos de trê retas.
Digite três valores e veja se eles formam um triângulo.""")
a = float(input('Primeira reta: '))
b = float(input('Segunda reta: '))
c = float(input('Terceira reta: '))

abs1 = abs(b - c)
abs2 = abs(a - c)
abs3 = abs(a - b)

soma1 = b + c
soma2 = a + c
soma3 = a + b

if abs1 < a < soma1 and abs2 < b < soma2 and abs3 < c < soma3:
    print('Com esses valores se forma um triângulo.')
else:
    print('Não é possível formar um triângulo.')