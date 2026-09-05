# Inimigos do Minecraft OverWorld e seus 'Status'

class inimigos_end:
    class enderman:
        def __init__(self, vida, xp, ferramenta, poder):
            self.vida = vida
            self.xp = xp
            self.ferramenta = ferramenta
            self.poder = poder
    Enderman = enderman(40, 5, False, 'Se Teletransportar')

    class endermite:
        def __init__(self, vida, xp, ferramenta, poder):
            self.vida = vida
            self.xp = xp
            self.ferramenta = ferramenta
            self.poder = poder
    Endermite = endermite(8, 3, False, False)

    class shulker:
        def __init__(self, vida, xp, poder1, poder2):
            self.vida = vida
            self.xp = xp
            self.poder1 = poder1
            self.poder2 = poder2
    ShulkerBox = shulker(30, 5, 'Bolas de Levitação', 'Teletransporte')

    class ender_dragon:
        def __init__(self, vida, xp, poder1, poder2, recompensa):
            self.vida = vida
            self.xp = xp
            self.poder1 = poder1
            self.poder2 = poder2
            self.recompensa = recompensa
    EnderDragon = ender_dragon(200, 12.000, 'Lançar Bolas de Dano', 'Voar')

    print(Enderman)
    print(Endermite)
    print(ShulkerBox)
    print(EnderDragon)

print('O código do The End, acaba aqui')