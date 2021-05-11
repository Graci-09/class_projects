# class_tests#

import math

n1 = int(input('Digite o valor de a: '))
n2 = int(input('Digite o valor de b: '))
n3 = int(input('Digite o valor de c: '))

delta = (n2 ** 2) - 4 * n1 * n3

part2 = (-1 * n2 + (math.sqrt(delta))) / (n1 * 2)

part3 = (-1 * n2 - (math.sqrt(delta))) / (n1 * 2)

if delta < 0:
    print('Não tem soluções reais')
elif delta == 0:
    part2 = (-n2 + (math.sqrt(delta))) / n1 * 2
    print('A equação só possui uma raiz e é {}'.format(part2))
elif delta > 0:
    print(part2)
    print(part3)
	