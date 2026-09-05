class Transfiguração:
    def __init__(self, largura, comprimento, altura):
        self.largura = largura
        self.comprimento = comprimento
        self.altura = altura
    def Comprimento(self, quantidade=1):
        self.comprimento += quantidade

objeto_transfigurado = Transfiguração(10, 20, 9)
objeto_transfigurado2 = Transfiguração(19, 28 , 10)

print(f'Quantidade do comprimento: {objeto_transfigurado.comprimento}')
objeto_transfigurado.Comprimento(10)
print(f'Quantidade do comprimento agora: {objeto_transfigurado.comprimento}')