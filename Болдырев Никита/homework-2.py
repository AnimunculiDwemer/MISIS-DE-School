hod = 0
win = 0
points_X = 0
points_Y = 0
a = [[0] * 3 for i in range(3)]
f = open("output.txt", mode='w')


def printresults():
    print(f'Счёт\nX: {points_X} Y: {points_Y}')
    f.write(f'Счёт\nX: {points_X} Y: {points_Y}\n')


def view():
    for y1 in range(3):
        for x1 in range (3):
            if a[x1][y1] == 0:
                print('- ', end='')
                f.write('- ')
            if a[x1][y1] == 1:
                print('X ', end='')
                f.write('X ')
            if a[x1][y1] == 2:
                print('O ', end='')
                f.write('O ')
            if a[x1][y1] == 3:
                print('+ ', end='')
                f.write('+ ')
        print()
        f.write('\n')
    print()
    f.write('\n')


def pr_win():
    for i in range(3):
        if a[i][0] == 1 and a[i][1] == 1 and a[i][2] == 1:
            print("Победил X")
            f.write("Победил X\n")
            a[i][0] = a[i][1] = a[i][2] = 3
            return 1
        elif a[i][0] == 2 and a[i][1] == 2 and a[i][2] == 2:
            print("Победил O")
            f.write("Победил O\n")
            a[i][0] = a[i][1] = a[i][2] = 3
            return 2
        elif a[0][i] == 1 and a[1][i] == 1 and a[2][i] == 1:
            print("Победил X")
            f.write("Победил X\n")
            a[0][i] = a[1][i] = a[2][i] = 3
            return 1
        elif a[0][i] == 2 and a[1][i] == 2 and a[2][i] == 2:
            print("Победил O")
            f.write("Победил O\n")
            a[0][i] = a[1][i] = a[2][i] = 3
            return 2
    if a[0][0] == 1 and a[1][1] == 1 and a[2][2] == 1:
        print("Победил X")
        f.write("Победил X\n")
        a[0][0] = a[1][1] = a[2][2] = 3
        return 1
    elif a[0][0] == 2 and a[1][1] == 2 and a[2][2] == 2:
        print("Победил O")
        f.write("Победил O\n")
        a[0][0] = a[1][1] = a[2][2] = 3
        return 2
    elif a[0][2] == 1 and a[1][1] == 1 and a[2][0] == 1:
        print("Победил X")
        f.write("Победил X\n")
        a[0][2] = a[1][1] = a[2][0] = 3
        return 1
    elif a[0][2] == 1 and a[1][1] == 1 and a[2][0] == 1:
        print("Победил O")
        f.write("Победил O\n")
        a[0][2] = a[1][1] = a[2][0] = 3
        return 2
    return 0


while 1:
    print()
    f.write('\n')
    if hod % 2 == 0:
        print("Ход X:")
        f.write("Ход X:\n")
    else:
        print("Ход O:")
        f.write("Ход X:\n")

    try:
        x = int(input("X = "))
        f.write(f"X = {x}\n")
        y = int(input("Y = "))
        f.write(f"Y = {y}\n")
    except ValueError:
        print ("Необходимо ввести цифру от 0 до 8")
        f.write("Необходимо ввести цифру от 0 до 8\n")
        continue

    if 0 <= x <= 2 and 0 <= y <= 2:
        if a[x][y] == 0:
            if hod % 2 == 0:
                a[x][y] = 1
            else:
                a[x][y] = 2
        else:
            print("Клетка уже занята, введите другие координаты")
            f.write("Клетка уже занята, введите другие координаты\n")
            continue
    else:
        print("Неверно введены координаты")
        f.write("Неверно введены координаты\n")
        continue

    hod += 1
    win = pr_win()
    view()

    if win != 0:
        if win == 1:
            points_X += 1
        else:
            points_Y += 1
        printresults()
        hod = 0
        win = 0
        a = [[0] * 3 for i in range(3)]
        continue

    if hod == 9:
        print("НИЧЬЯ")
        f.write("НИЧЬЯ\n")
        printresults()
        hod = 0
        win = 0
        a = [[0] * 3 for i in range(3)]
        continue
