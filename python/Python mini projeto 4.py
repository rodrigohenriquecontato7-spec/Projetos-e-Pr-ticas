def cronômetro():
    import time as t
    tempo = int(input('Quanto tempo você deseja?: '))

    print('-=' * 30)
    print(f'Você escolheu seu tempo para {tempo}!')
    print('-=' * 30)

    while tempo >=0:
        print(f'Cronômetro: {tempo}')
        t.sleep(1)
        tempo -=1
        if tempo <0:
            print('<>' * 30)
            print('Seu tempo acabou!!!!')

cronômetro()
