'''
Isto é apenas um projetinho mque eu vou usar
para botar em prática tudo o que eu aprendi
em Python, entenda que eu comecei a 6 dias,
então não vai ter nada muito profissional 
entende.
'''
print('-' * 30)
print('Olá, Mundo!')
print('o resultado da soma de 3 + 3 é:', 3 + 3)
print('-' * 30)
comida = 5
dinheiro = 9
print('-' * 30)
if dinheiro >= 9:
    print('Você tem dinheiro para comprar a comida')
else:
    print('Você não tem dinheiro para comprar a comida')
print('-' * 30)
keyboard_ = 3 
if keyboard_ == 3 :
    input(keyboard_)
print('-' * 30)
Nome = 'Rogério '

if Nome == 'Rogério ':
    input(Nome)
print('-' * 30)
nome1 = 'Rogerio '
nome2 = 'Luiz '

if nome1 == 'Rogerio ':
    input(nome1), input(nome2)
print('-' * 30)
comida = 13.00
dinheiro = float(input('Digite sua quantidade de dinheiro'))

if dinheiro >= comida:
    print('Você pode comprar a comida')
else:
    print('Você não tem dinheiro o sufuciente')
print('-' * 30)
def cadastro():

    Nome = input('Digite seu nome: ')
    Idade = int(input('Digite sua idade: '))
    Cargo = input('Digite seu cargo: ')

cadastro()
print('-' * 30)
Nome = input('Digite seu nome: ')
Idade = int(input('Digite sua idade: '))
Cargo = input('Digite seu cargo: ')

if Nome == 'Rodrigo':
    print('Bem vindo(a), Rodrigo!')
else:
    print(f'Bem vindo(a) {Nome}!')
if Idade == '13':
    print('Você tem 13 anos!')
else:
    print(f'Você tem {Idade} anos!')
if Cargo == 'Animador' or Cargo == 'Animadora':
    print('Você é um(a) Animador!')
else:
    print(f'Você é um(a) {Cargo}')

print(Nome, Idade, Cargo)