'''
Esse é o esqueleto de uma Calculadora.
Por mais que eu tenha um conhecimento
raso, tentarei meu melhor
'''
def calculadora():
    print('-' * 30)
Num1 = float(input('Digite um número: '))
print('-' * 30)
Num2 = float(input('Digite outro número: '))
print('-' * 30)
Operação = input('Digite uma operação(Soma, Subtração, Multiplicação ou Divisão): ')
Resultado_Soma = (Num1 + Num2)
Resultado_Sub = (Num1 - Num2)
Resultado_Mult = (Num1 * Num2)
Resultado_Div = (Num1 / Num2)

if Operação == '+' or Operação == 'soma' or Operação == 'Soma':
    print('-' * 30)
    print(f'O resultado é {Resultado_Soma}')
elif Operação == '-' or Operação == 'subtração' or Operação == 'Subtração':
    print('-' * 30)
    print(f'O resultado é {Resultado_Sub}')
elif Operação == '*' or Operação == 'multiplicação' or Operação == 'Multiplicação':
    print('-' * 30)
    print(f'O resultado é {Resultado_Mult}')
else:
    print('-' * 30)
    print(f'O resultado é {Resultado_Div}') 

