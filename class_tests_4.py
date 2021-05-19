from random import randint
from time import sleep

print('PEDRA - PAPEL - TESOURA')
sleep(2)
print('Você vai jogar Jokenpô com um computador.\nSerá que irá se sair bem nessa?')
print('[ 1 ] PEDRA\n'
      '[ 2 ] PAPEL\n'
      '[ 3 ] TESOURA')
lista = [1, 2, 3]
n = randint(1, 3)
user = int(input('Escolha sua opção: '))
marc = '*=' * 15
vit = 'JOGADOR VENCE'
der = 'COMPUTADOR VENCE'
emp = 'EMPATOU'
# opcao invalida
if user != 1 and user != 2 and user != 3:
    print('Opção Inválida. Reinicie o jogo.')
    quit()
else:
    # contagem jokenpo
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PÔ')
    sleep(1)
    # se de empate >>>
    if user == 1 and n == 1:
        print('{}\nComputador escolheu Pedra\nJogador escolheu Pedra\n{}\n{}'.format(marc, marc, emp))
    elif user == 2 and n == 2:
        print('{}\nComputador escolheu Papel\nJogador escolheu Papel\n{}\n{}'.format(marc, marc, emp))
    elif user == 3 and n == 3:
        print('{}\nComputador escolheu Tesoura\nJogador escolheu Tesoura\n{}\n{}'.format(marc, marc, emp))
    # derrotas jogador >>>
    if user == 1 and n == 2:
        print('{}\nComputador escolheu Papel\nJogador escolheu Pedra\n{}\n{}'.format(marc, marc, der))
    elif user == 3 and n == 1:
        print('{}\nComputador escolheu Pedra\nJogador escolheu Tesoura\n{}\n{}'.format(marc, marc, der))
    elif user == 2 and n == 3:
        print('{}\nComputador escolheu Tesoura\nJogador escolheu Papel\n{}\n{}'.format(marc, marc, der))
    # vitorias jogador >>>
    if user == 1 and n == 3:
        print('{}\nComputador escolheu Tesoura\nJogador escolheu Pedra\n{}\n{}'.format(marc, marc, vit))
    elif user == 3 and n == 2:
        print('{}\nComputador escolheu Papel\nJogador escolheu Tesoura\n{}\n{}'.format(marc, marc, vit))
    elif user == 2 and n == 1:
        print('{}\nComputador escolheu Pedra\nJogador escolheu Papel\n{}\n{}'.format(marc, marc, vit))
