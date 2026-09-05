# Inimigos do Minecraft OverWorld e seus 'Status'

class inimigos_overworld:
    class zumbi:
        def __init__(self, vida, xp, ferramenta, poder):
            self.vida = vida
            self.xp = xp
            self.ferramenta = ferramenta
            self.poder = poder
    Zumbi = zumbi(20, 5, (True or False), False)

    class esqueleto:
        def __init__(self, vida, xp, ferramenta, poder):
            self.vida = vida
            self.xp = xp
            self.ferramenta = ferramenta
            self.poder = poder
    Esqueleto = esqueleto(19.9, 5, True, False)

    class creeper:
        def __init__(self, vida, xp, ferramenta, poder):
            self.vida = vida
            self.xp = xp
            self.ferramenta = ferramenta
            self.poder = poder
    Creeper = creeper(20, 5, False, 'Explosao')

    class aranha:
        def __init__(self, vida, xp, ferramenta, poder):
            self.vida = vida
            self.xp = xp
            self.ferramenta = ferramenta
            self.poder = poder
    Aranha = aranha(16, 5, False, 'Teias')

    class bruxa:
        def __init__(self, vida, xp, ferramenta, poder):
            self.vida = vida
            self.xp = xp
            self.ferramenta = ferramenta
            self.poder = poder
    Bruxa = bruxa(26, 5, True, False)

    class slime:
        def __init__(self, vida, xp, tamanho):
            self.vida = vida
            self.xp = xp
            self.tamanho = tamanho
    SlimeGrande = slime(16, 4, 'Grande')
    SlimeMedio = slime(4, 2, 'Medio')
    SlimePequeno = slime(1, 1, 'Pequeno')

    class warden:
        def __init__(self, vida, xp, ferramenta, poder):
            self.vida = vida
            self.xp = xp
            self.ferramenta = ferramenta
            self.poder = poder
    Warden = warden(500, 5, False, 'Rajada de Ondas Sonoras')

    class aranha_cavernas(aranha):
        def __init__(self, vida, xp, ferramenta, poder):
            super().__init__(vida, xp, ferramenta, poder)
            self.efeito = True
    AranhaDasCavernas = aranha_cavernas(12, 5, False, 'Teia')

    class zumbi_mumia(zumbi):
        def __init__(self, vida, xp, ferramenta, poder):
            super().__init__(vida, xp, ferramenta, poder)
            self.efeito = True
    ZumbiMumia = zumbi_mumia(20, 5, (True or False), 'Fome')

    class zumbi_afogado(zumbi):
        def __init__(self, vida, xp, ferramenta, poder):
            super().__init__(vida, xp, ferramenta, poder)
            self.transformacao = []
    ZumbiAfogado = zumbi_afogado(20, 5, (True or False), False)

    class errante(esqueleto):
        def __init__(self, vida, xp, ferramenta, poder):
            super().__init__(vida, xp, ferramenta, poder)
            self.efeito = True
    Errante = errante(20, 5, True, 'Flechas de Lentidao')

    class pantanoso(esqueleto):
        def __init__(self, vida, xp, ferramenta, poder):
            super().__init__(vida, xp, ferramenta, poder)
            self.efeito = True
    Pantanoso = pantanoso(16, 5, True, 'Flechas de Veneno')

    class brisa:
        def __init__(self, vida, xp, ferramenta, poder):
            self.vida = vida
            self.xp = xp
            self.ferramenta = ferramenta
            self.poder = poder
    Brisa = brisa(30, 10, False, 'Bolas de Vento')

    class phantom:
        def __init__(self, vida, xp, ferramenta, poder):
            self.vida = vida
            self.xp = xp
            self.ferramenta = ferramenta
            self.poder = poder
    Phantom = phantom(20, 5, False, False)

    class traca:
        def __init__(self, vida, xp, ferramenta, poder):
            self.vida = vida
            self.xp = xp
            self.ferramenta = ferramenta
            self.poder = poder
    Traca = traca(8, 5, False, 'Entrar em Pedras')

    class saqueador:
        def __init__(self, vida, xp, ferramenta, poder):
            self.vida = vida
            self.xp = xp
            self.ferramenta = ferramenta
            self.poder = poder
    Saqueador = saqueador(24, 5, True, False)

    class vingador:
        def __init__(self, vida, xp, ferramenta, poder):
            self.vida = vida
            self.xp = xp
            self.ferramenta = ferramenta
            self.poder = poder
    Vingador = vingador(24, 5, True, False)

    class invocador:
        def __init__(self, vida, xp, ferramenta, poder):
            self.vida = vida
            self.xp = xp
            self.ferramenta = ferramenta
            self.poder = poder
    Invocador = invocador(24, 10, False, 'Invocar Vex e outros')

    class ilusionista:
        def __init__(self, vida, xp, ferramenta, poder):
            self.vida = vida
            self.xp = xp
            self.ferramenta = ferramenta
            self.poder = poder
    Ilusionista = ilusionista(32, 5, True, 'Feiticos Magicos (Clonar-se, etc)')

    class devastador:
        def __init__(self, vida, xp, ferramenta, poder):
            self.vida = vida
            self.xp = xp
            self.ferramenta = ferramenta
            self.poder = poder
    Devastador = devastador(100, 20, False, False)

    class vex(invocador):
        def __init__(self, vida, xp, ferramenta, poder):
            super().__init__(vida, xp, ferramenta, poder)
            self.tamanho = 'Pequeno'
    Vex = vex(14, 3, True, 'Voar')

    class guardiao:
        def __init__(self, vida, xp, ferramenta, poder):
            self.vida = vida
            self.xp = xp
            self.ferramenta = ferramenta
            self.poder = poder
    Guardiao = guardiao(30, 10, False, 'Dar Dano Com Laser')

    class guardiao_mestre(guardiao):
        def __init__(self, vida, xp, ferramenta, poder):
            super().__init__(vida, xp, ferramenta, poder)
            self.efeito = True
    GuardiaoMestre = guardiao_mestre(80, 10, False, 'Dar Fraqueza ao Adversario')

    print(Zumbi)
    print(Esqueleto)
    print(Creeper)
    print(Aranha)
    print(Bruxa)
    print(f'Grande: {SlimeGrande} Médio: {SlimeMedio} e Pequeno {SlimePequeno}')
    print(Warden)
    print(AranhaDasCavernas)
    print(ZumbiMumia)
    print(ZumbiAfogado)
    print(Errante)
    print(Pantanoso)
    print(Brisa)
    print(Phantom)
    print(Traca)
    print(Saqueador)
    print(Vingador)
    print(Invocador)
    print(Ilusionista)
    print(Devastador)
    print(Guardiao)
    print(GuardiaoMestre)

print('O codigo do OverWorld, acaba aqui') 
