razm = 10  # размерность матрицы
pole = list(
    [list([f"{j}{i}" for i in range(razm)]) for j in range(razm)])  # матрица игрового поля изначально заполнена *
for i in pole:
    print(i)


# нас будут интересовать по 11 диагоналей, но для удобства создания списка удалим затем лишний список\
# по главной и побочной диагонали
# diags1 = [[] for _ in range(razm + 2)]
# diags2 = [[] for _ in range(razm + 2)]
# for i in range(5, -1, -1):
#     ind = i
#     for j in range(9 - i + 1):
#         diags1[i].append(pole[ind][j])
#         diags1[6 + i].append(pole[j][ind])
#         ind += 1
# diags1.pop(6)  # удалили дубликат
# for i in range(4, 10):
#     ind = i
#     for j in range(i + 1):
#         diags2[i - 4].append(pole[ind][j])
#         diags2[6 + i - 4].append(pole[9 - j][9 - ind])
#         ind -= 1
# diags2.pop(5)  # удалили дубликат


# rows = [pole[i] for i in range(razm)]
# cols = [[pole[i][j] for i in range(razm)] for j in range(razm)]
# diags = [[], []]
# for i in range(-1, razm - 1):
#     diags[0].append(pole[i + 1][i + 1])
# for i in range(razm - 1, -1, -1):
#     diags[1].append(pole[i][razm - 1 - i])
# проверка на победную комбинацию
# сначала по строкам, потом по столбцам, затем по диагоналям
def check10(pole):
    rows = [pole[i] for i in range(razm)]
    cols = [[pole[i][j] for i in range(razm)] for j in range(razm)]
    # нас будут интересовать по 11 диагоналей, но для удобства создания списка удалим затем лишний список\
    # по главной и побочной диагонали
    diags1 = [[] for _ in range(razm + 2)]
    diags2 = [[] for _ in range(razm + 2)]

    for i in range(5, -1, -1):
        ind = i
        for j in range(9 - i + 1):
            diags1[i].append(pole[ind][j])
            diags1[6 + i].append(pole[j][ind])
            ind += 1
    diags1.pop(6)  # удалили дубликат
    for i in range(4, 10):
        ind = i
        for j in range(i + 1):
            diags2[i - 4].append(pole[ind][j])
            diags2[6 + i - 4].append(pole[9 - j][9 - ind])
            ind -= 1
    diags2.pop(5)  # удалили дубликаттолько 12 диагоналей

    for i in range(5, 0, -1):
        ind = i
        for j in range(9 - i):
            diags1[i].append(pole[ind + 1][j])
            ind += 1
    ##############################################
    for r in range(razm):
        if ["X"] * 5 in rows[r]:
            s = ((" ".join(rows[r])).replace("X X X X X", "! ! ! ! !")).split()
            pole[r] = s
            return pole
        elif ["0"] * 5 in rows[r]:
            s = ((" ".join(rows[r])).replace("0 0 0 0 0", "! ! ! ! !")).split()
            pole[r] = s
            return pole

    for c in range(razm):
        if ["X"] * 5 in cols[c]:
            index = (" ".join(cols[c])).find("X X X X X") // 2
            for i in range(index, 5):
                pole[i][c] = "!"
            return pole

    if ["0"] * razm in rows:
        win = rows.index(["0"] * razm)
        pole[win] = ["!"] * 3
        return pole
    elif ["0"] * razm in cols:
        win = cols.index(["0"] * razm)
        for i in range(razm):
            pole[win][i] = "!"
        return pole
    elif ["0"] * razm in diags:
        win = diags.index(["0"] * razm)
        if win == 0:
            for i in range(-1, razm - 1):
                pole[i + 1][i + 1] = "!"
            print(pole)
        elif win == 1:
            for i in range(razm - 1, -1, -1):
                pole[i][razm - 1 - i] = "!"
        return pole

    elif ["X"] * razm in rows:
        win = rows.index(["X"] * razm)
        pole[win] = ["!"] * 3
        return pole
    elif ["X"] * razm in cols:
        win = cols.index(["X"] * razm)
        for i in range(razm):
            pole[win][i] = "!"
        return pole
    elif ["X"] * razm in diags:
        win = diags.index(["X"] * razm)
        if win == 0:
            for i in range(-1, razm - 1):
                pole[i + 1][i + 1] = "!"
        elif win == 1:
            for i in range(razm - 1, -1, -1):
                pole[i][razm - 1 - i] = "!"
        return pole


# игровой цикл
def game():
    global pole
    flag = True
    h = 0
    while flag:
        if h != 9:
            if h % 2 == 0:
                print("Ход крестиком")
            if h % 2 == 1:
                print("Ход ноликом")

            x, y = map(int, input("Введите координаты для хода через пробел: ").split())

            if pole[x][y] == "*" and x in [i for i in range(razm)] and y in [i for i in range(razm)]:
                if h % 2 == 0:
                    pole[x][y] = "X"
                else:
                    pole[x][y] = "0"
                h += 1
                ch = check10(pole)
                if ch:
                    print("Победа")
                    for i in ch:
                        print(*i)
                    flag = False
                else:
                    for i in pole:
                        print(*i)
            else:
                print("Ошибка. Введите координаты заново")
        else:
            print("Ничья. Поле очищено. Сыграйте еще раз")
            pole = list([list([f"*" for i in range(razm)]) for j in range(razm)])
            h = 0


game()
