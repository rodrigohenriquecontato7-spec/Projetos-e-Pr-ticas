class condicao:
    def __init__(self, condicao, cumpriu):
        self.condicao = condicao
        self.cumpriu = cumpriu

condição = condicao(input('Diga uma condição: '), input('Essa condição foi concluida?: '))

if (condicao.cumpriu) == 'Sim' or (condicao.cumpriu) == 'sim' or (condicao.cumpriu) == 's':
    print('A condição foi cumprida!')