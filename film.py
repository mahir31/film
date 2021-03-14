while True:
    x = input('> ')
    
    if x == 'print':
        with open("film.txt", "r") as x:
            y = [y.strip('\n') for y in (x.readlines())]
            for number, z in enumerate(y, 1):
                print(f'{number}. {z}')

    if x == 'add':
        print('input movie name')
        x = input('> ')
        with open("film.txt", "a") as y:
            y.write(f'\n{x}')
        print(f'movie {x} has been added!')
    
    if x == 'exit':
        break