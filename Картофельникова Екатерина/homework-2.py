# Картофельникова екатерина бивт-22-8

mas = []
hod = 0
mas = ["*"] * 3
flag = True
x = 0
y = 0

def criatef():
    with open("kn.txt", "w", encoding='utf-8') as f:
        pass
def save():
    msg = ""
    for i in range(len(mas)):
        for j in range(len(mas[i])):
            msg += mas[i][j]+" "
        msg += "\n"
    msg+="\n"
    with open("kn.txt", "a",encoding='utf-8') as f:
        f.write(msg)


def print_mas():
    for i in range(len(mas)):
        for j in range(len(mas[i])):
            print(mas[i][j], end=" ")
        print()


def change(position, symbol):
    match position:
        case 1:
            mas[0][0] = symbol
            mas[0][1] = symbol
            mas[0][2] = symbol

        case 2:
            mas[1][0] = symbol
            mas[1][1] = symbol
            mas[1][2] = symbol
        case 3:
            mas[2][0] = symbol
            mas[2][1] = symbol
            mas[2][2] = symbol
        case 4:
            mas[0][0] = symbol
            mas[1][0] = symbol
            mas[2][0] = symbol
        case 5:
            mas[0][1] = symbol
            mas[1][1] = symbol
            mas[2][1] = symbol
        case 6:
            mas[0][2] = symbol
            mas[1][2] = symbol
            mas[2][2] = symbol
        case 7:
            mas[0][0] = symbol
            mas[1][1] = symbol
            mas[2][2] = symbol
        case 8:
            mas[0][2] = symbol
            mas[1][1] = symbol
            mas[2][0] = symbol


def check_winner():
    global flag
    if (mas[0][0] != "*" and mas[0][0] == mas[0][1] == mas[0][2]):
        if mas[0][0] == "X":
            print("Победа Х")
            change(1, "❌")
        elif mas[0][0] == "0":
            print("Победа 0")
            change(1, "⭕️")
        flag = False
    elif (mas[1][0] != "*" and mas[1][0] == mas[1][1] == mas[1][2]):
        if mas[1][0] == "X":
            print("Победа Х")
            change(2, "❌")
        elif mas[1][0] == "0":
            print("Победа 0")
            change(2, "⭕️")
        flag = False
    elif (mas[2][0] != "*" and mas[2][0] == mas[2][1] == mas[2][2]):
        if mas[2][0] == "X":
            print("Победа Х")
            change(3, "❌")
        elif mas[2][0] == "0":
            print("Победа 0")
            change(3, "⭕️")
        flag = False
    elif (mas[0][0] != "*" and mas[0][0] == mas[1][0] == mas[2][0]):
        if mas[0][0] == "X":
            print("Победа Х")
            change(4, "❌")
        elif mas[0][0] == "0":
            print("Победа 0")
        change(4, "⭕️")
        flag = False
    elif (mas[0][1] != "*" and mas[0][1] == mas[1][1] == mas[2][1]):
        if mas[0][1] == "X":
            print("Победа Х")
            change(5, "❌")
        elif mas[0][1] == "0":
            print("Победа 0")
            change(5, "⭕️")
        flag = False
    elif (mas[0][2] != "*" and mas[0][2] == mas[1][2] == mas[2][2]):
        if mas[0][2] == "X":
            print("Победа Х")
            change(6, "❌")
        elif mas[0][2] == "0":
            print("Победа 0")
            change(6, "⭕️")
        flag = False
    elif (mas[0][0] != "*" and mas[0][0] == mas[1][1] == mas[2][2]):
        if mas[0][0] == "X":
            print("Победа Х")
            change(7, "❌")
        elif mas[0][0] == "0":
            print("Победа 0")
            change(7, "⭕️")
        flag = False
    elif (mas[0][2] != "*" and mas[0][2] == mas[1][1] == mas[2][0]):
        if mas[0][2] == "X":
            print("Победа Х")
            change(8, "❌")
        elif mas[0][2] == "0":
            print("Победа 0")
            change(8, "⭕️")
        flag = False

        flag = False


for i in range(3):
    mas[i] = ["*"] * 3
print_mas()
criatef()
while flag:
    if (hod % 2 == 0):
        print("Ходит  X")
    else:
        print("Ходит 0")
    try:
        print("Введите X")
        x = int(input())
        print("Введите Y")
        y = int(input())
        if (x < 0 or x > 2) or (y < 0 or y > 2):
            raise ValueError
    except ValueError:
        print("Введите число от 0 до 2")
        continue
    if (0 <= x <= 2 and 0 <= y <= 2 and mas[x][y] == "*"):
        if (hod % 2 == 0):
            mas[x][y] = "X"
        else:
            mas[x][y] = "0"
    hod += 1

    print_mas()
    check_winner()
    save()
    if not (flag):
        print_mas()
        break
    if hod == 9:
        print("Ничья")
        break

