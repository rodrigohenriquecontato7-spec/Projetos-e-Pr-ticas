'''Aulas Completas de Estudo Python 'LanCode' 
   
   Usar para estudos de Códigos e Lpogica de programação
'''
# Print e Variável
PNUMERO = 7
SNUMERO = 8

print(PNUMERO + SNUMERO)
print(PNUMERO - SNUMERO)
print(PNUMERO * SNUMERO)
print(PNUMERO / SNUMERO)

# Input
Nome = input('Qual é seu nome?: ')
print(Nome)
#--------------------------------------------------------------------------------------------------
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

# Operação
R_soma = (n1 + n2)
print(f'O resultado da soma entre {n1} e {n2} é -={R_soma}=-')
#--------------------------------------------------------------------------------------------------

# Condicionais IF e ELSE
Idade = int(input('Quantos anos você tem?: '))

if Idade >= 18:
    print('Liberado')
else:
    print('TU É DE MENÓ, SAI DAQUIIII')
#--------------------------------------------------------------------------------------------------
senha = 'Larinha1729'
tentavia_senha = input('Digite a senha: ')

if senha != tentavia_senha:
    print('Pode entrar!')
else:
    print('sai daqui otário!')
#--------------------------------------------------------------------------------------------------

# ELIF e sua função
nota = float(input('Digite sua nota: '))

if nota >=7:
    print('Passou')
elif nota >=5:
    print('Recuperação')
else:
    print('Reprovou')
#--------------------------------------------------------------------------------------------------

# Navegando em Listas
frutas = ['banana', 'maçã', 'uva']

frutas[1] = 'abacate'
frutas.insert(0, 'Morango') 
frutas.remove("banana")
print(frutas)

if "Morango" in frutas:
    print('Tem maçã em frutas')

print(frutas)
#--------------------------------------------------------------------------------------------------
cores = ('vermelho', 'verde', 'azul')
print(cores)
#--------------------------------------------------------------------------------------------------
minhas_tuplas = [('Maçã', 'Banana'), ('Verde', 'Vermelho')]
print(minhas_tuplas[1][0])
#--------------------------------------------------------------------------------------------------
dados ={'nome':'Rodrigo', 'idade':13}
print(dados['idade'])
#--------------------------------------------------------------------------------------------------

# Temporizador com biblioteca
import time as t
contador = 10

while contador >=0:
    print(f'Cronômetro: {contador}')
    t.sleep(1)
    contador -=1

print('TEMPO ESGOTADO')
#--------------------------------------------------------------------------------------------------

# Acho que dava para ser mais simples
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
operações = input('Digite uma operação: ')

if operações == '+' or operações == 'soma':
    print('O resultado da soma é ', (n1 + n2))
if operações == '-' or operações == 'subtração':
    print('O resultado da subtração é ', (n1- n2))
if operações == '*' or operações == 'multiplicação':
    print('O resultado da multiplicação é ', (n1 * n2))
if operações == '/' or operações == '//' or operações == 'divisão':
    print('O resultado da divisão é ', (n1//n2))
#--------------------------------------------------------------------------------------------------

# Match e Case para cálculos matemáticos
Num1 = int(input('Digite o primeiro número: '))
Num2 = int(input('Digite o segundo número: '))
operação = input('Digite uma operação: ')

match operação:
    case 'soma':
        res = Num1 + Num2
    case 'subtração':
        res = Num1 - Num2
    case 'multiplicação':
        res = Num1 * Num2
    case 'divisão':
        res = Num1 // Num2
print(f'O resultado da operação é {res}!')
#--------------------------------------------------------------------------------------------------

# loops em WHILE
senha = 'Larinha1729'
tentativa_senha = ''
while senha != tentativa_senha:
    tentativa_senha = input('Digite sua senha: ')
    if tentativa_senha != senha:
        print('Senha incorreta! Tente novamente')
    else:
        print('Muito bem, acertou :)')
#--------------------------------------------------------------------------------------------------

# Navegando em listas com FOR
números = [5,6,2,9,0,1,5,6]
for numero in números:
    if numero % 2 == 0:
        continue
    print(numero)
#--------------------------------------------------------------------------------------------------

# Até as funções tem funções
def ola(nome):
    print(f'Olá, {nome}')

nome_inserido = input('Digite seu nome: ')

ola(nome_inserido)
#--------------------------------------------------------------------------------------------------

# Definições e Funções na prática
def somar(a, b):
    resultado = a + b
    return resultado

def cumprimento(nome):
    print(f'Olá {nome}')
    
# Bibliotecas PYTHON
import time, random, qrcode

print('Aguarde...')
time.sleep(4)
print('pronto')

while True:
    numero_aleatorio = random.randint(1, 50)
    print(numero_aleatorio)
    time.sleep(1)
    if numero_aleatorio %2 == 0:
        break
#----------------------------------------------------------------------------------------------------

# Objetos e suas Peculiaridades
class quadrado:
    def __init__(self, base, altura, area):
        self.base = base
        self.altura = altura
        self.area = area
    
    def base(self, quantidade=int(input('Quanto e a base?: '))):
        self.base = quantidade
    def altura(self, quantidade=int(input('Quanto e a altura?: '))):
        self.altura = quantidade
    def area(self, quantidade= (altura * base)):
        self.area = quantidade