class criacao:
    def __init__(self, largura, altura, comprimento):
        self.largura = largura
        self.altura = altura
        self.comprimento = comprimento

ObjetoCriado = criacao(input('defina largura: '), input('defina altura: '), input('defina comprimento: '))

print('-=' * 30)
print(f'A largura é: {ObjetoCriado.largura}!') 
print('-=' * 30)
print(f'A altura é: {ObjetoCriado.altura}!')
print('-=' * 30)
print(f'O comprimento é: {ObjetoCriado.comprimento}!')
print('-=' * 30)