import time as t

def calculadora():
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite outro número: '))
    operações = input('Digite uma das quatro operações: ')

    R_soma = (n1 + n2)
    R_sub = (n1 - n2)
    R_mult = (n1 * n2)
    R_div = (n1 // n2)

    if operações == '+' or operações == 'soma':
        print(f'O resultado da soma é {R_soma}')
    if operações == '-' or operações == 'subtração':
        print(f'O resultado da subtração é {R_sub}')
    if operações == '*' or operações == 'multiplicação':
        print(f'O resultado da soma {R_mult}')
    if operações == '/' or operações == '//' or operações == 'divisão':
        print(f'O resultado da divisão é {R_div}')

    print('Obrigado por usar a calculadora!')
def tempo():

    print('-=' * 30)
    tempo = int(input('Tempo- '))
    print('-=' * 30)
    while tempo >= 0:
        print(f'Cronômetro: {tempo}')
        t.sleep(1)
        tempo -=1

    print('<>' * 30) 
    print('O TEMPO ACABOU!!!')
    print('<>' * 30)
