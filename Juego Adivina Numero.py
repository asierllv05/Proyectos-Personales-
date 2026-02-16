def juego():
    n=int(input('Dame el nivel de dificultad [1,2,3]: '))
    if n == 1:
        import random
        na= random.randint(1, 10)
        num = int(input('Dame un numero entre el 1 y el 10: '))
        while num != na:
            if num < na:
                print('Dame un numero mas Grande')
                num = int(input('Dame un numero entre el 1 y el 10: '))
            elif num > na:
                print('Dame un numero mas Pequeño')
                num = int(input('Dame un numero entre el 1 y el 10: '))
        print('Acertaste')
    if n == 2:
        import random
        na= random.randint(1, 100)
        num = int(input('Dame un numero entre el 1 y el 100: '))
        while num != na:
            if num < na:
                print('Dame un numero mas Grande')
                num = int(input('Dame un numero entre el 1 y el 100: '))
            elif num > na:
                print('Dame un numero mas Pequeño')
                num = int(input('Dame un numero entre el 1 y el 100: '))
        print('Acertaste')
    if n == 3:
        import random
        na= random.randint(1, 1000)
        num = int(input('Dame un numero entre el 1 y el 1000: '))
        while num != na:
            if num < na:
                print('Dame un numero mas Grande')
                num = int(input('Dame un numero entre el 1 y el 1000: '))
            elif num > na:
                print('Dame un numero mas Pequeño')
                num = int(input('Dame un numero entre el 1 y el 1000: '))
        print('Acertaste')
        
juego()
