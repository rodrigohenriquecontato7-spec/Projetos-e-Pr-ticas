'''isso é uma calculadora simples
Por favor não leve esse projeto 
como algo profissional, fiz apenas
por diversão'''

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
operações = input('Digite uma das quatro operaçoes: ')

R_Soma = (num1 + num2)
R_Sub = (num1 - num2)
R_Mult = (num1 * num2)
R_Div = (num1 / num2)

if operações == '+' or operações == 'soma':
    print('-' * 30)
    print(f'O resultado da soma é {R_Soma}!')
if operações == '-' or operações == 'subtração':
    print('-' * 30)
    print(f'O resultado da subtração é {R_Sub}!')
if operações == '*' or operações == 'multiplicação':
    print('-' * 30)
    print(f'O resultado da multiplicação é {R_Mult}!')
if operações == '/' or operações == 'divisão':
    print('-' * 30)
    print(f'O resultado da divisão é {R_Div}!')

print('-' * 30)
print('Obrigado por usar a minha calculadora!')