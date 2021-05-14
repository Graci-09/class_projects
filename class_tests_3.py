from datetime import date

print('==*' * 20)
print('Programa de alistamento')
print('*==' * 20)

sexo = int(input("""1 - Masculino
2 - Feminino
Informe seu sexo: """))
if sexo == 2:
    print('Você não precisa se alistar!')
    exit()
nome = str(input('Informe o seu nome: ')).title().strip()

ano = int(input('Informe o seu ano de nascimento: '))
age = int(date.today().year - ano)

if 0 < age < 18:
    print("""{}, você ainda não precisa se alistar.
Mas fique de olho, faltam só {} anos.""".format(nome, 18 - age))
elif age == 18:
    print("""{}, você já está na idade. 
Se aliste o mais rápido possível.""".format(nome))
elif 18 < age <= 110:
    idade = int(input("""{}, você já se alistou antes?
1 - SIM 
2 - NÃO
""".format(nome)))
    if idade == 2:
        print('{}, você já passou do prazo em {} anos. '
              'O seu ano de alistamento foi em {}.'.format(nome, age - 18, ano + 18))
    elif idade == 1:
        print('Parabéns {}, você está em dia com suas obrigações.'.format(nome))
elif ano > date.today().year or age > 110:
    print('Digite um ano válido!')
print('--FIM--')