# Inimigos do Minecraft OverWorld e seus 'Status'
from OverWorld import zumbi, esqueleto, brisa, slime

class inimigos_nether:
    class zumbi_pigman(zumbi):
        def __init__(self, vida, xp, ferramenta, poder):
            super().__init__(vida, xp, ferramenta, poder)
            self.herança = ()
    ZumbiPigman = zumbi_pigman(20, 5, True, 'Chamar vários dos seus')

    class piglin:
        def __init__(self, vida, xp, ferramenta, poder):
            self.vida = vida
            self.xp = xp
            self.ferramenta = ferramenta
            self.poder = poder
    Piglin = piglin(16, 5, True, False)
    
    class piglin_bruto(piglin):
        def __init__(self, vida, xp, ferramenta, poder):
            super().__init__(vida, xp, ferramenta, poder)
            self.força = ()
    PiglinBruto = piglin_bruto(50, 20, True, False)

    class hoglin:
        def __init__(self, vida, xp, ferramenta, poder):
            self.vida = vida
            self.xp = xp
            self.ferramenta = ferramenta
            self.pode = poder
    Hoglin = hoglin(40, 5, False, False)

    class esqueleto_wither(esqueleto):
        def __init__(self, vida, xp, ferramenta, poder):
            super(). __init__(vida, xp, ferramenta, poder)
            self.cabeça = True
    EsqueletoWither = esqueleto_wither(20, 5, True, 'Dar Efeito de Decomposição')

    class blaze(brisa):
        def __init__(self, vida, xp, ferramenta, poder):
            super().__init__(vida, xp, ferramenta, poder)
            self.voar = True
            self.drop_importante = True
    Blaze = blaze(20, 10, False, 'Soltar Bolas de Fogo')

    class ghast:
        def __init__(self, vida, xp, ferramenta, poder):
            self.vida = vida
            self.xp = xp
            self.ferramenta = ferramenta
            self.poder = poder
    Ghast = ghast(10, 5, False, 'Soltar Bolas de Fogo')

    class cubos_magma(slime):
        def __init__(self, vida, xp, tamanho):
            super().__init__(vida, xp, tamanho)
            self.poder = True
    MagmaCubeGrande = cubos_magma(16, 4, 'Grande')
    MagmaCubeMedio = cubos_magma(4, 2, 'Médio')
    MagmaCubePequeno = cubos_magma(1, 1, 'Pequeno')

    class the_wither_boss:
        def __init__(self, vida, xp, poder1, poder2, recompensa):
            self.vida = vida
            self.xp = xp
            self.poder1 = poder1
            self.poder2 = poder2
            self.recompensa = recompensa
    TheWitherBoss = the_wither_boss(300, 50, 'Lançar Cabeças de Decomposição', 'Voar', 'Estrela do Nether')

    print(ZumbiPigman)
    print(Piglin)
    print(PiglinBruto)
    print(Hoglin)
    print(EsqueletoWither)
    print(Blaze)
    print(Ghast)
    print(f'Grande: {MagmaCubeGrande} Médio: {MagmaCubeMedio} e Pequeno: {MagmaCubePequeno}')
   
print('O código do Nether, acaba aqui')
