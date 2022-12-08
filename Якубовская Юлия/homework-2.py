def view():

    for y1 in range(3):

        for x1 in range (3):

            if (a[x1][y1] == 0): print ('- ', end = '')

            if (a[x1][y1] == 1): print ('X ', end = '')

            if (a[x1][y1] == 2): print ('O ', end = '')

            if (a[x1][y1] == 3): print ('+ ', end = '')

        print()

    print()


def checkvictory():

    i = 0

    while i < 3:

        if a[i][0] == a[i][1] and a[i][2]:
            if a[i][0] == 1:
                print("Cross wins")
                f.write("Cross wins\n")
                return 1
            elif a[i][0] == 2:
                print("Naught wins")
                f.write("Naught wins\n")
                return 2
        elif a[0][i] == a[1][i] and a[2][i]:
            if a[0][i] == 1:
                print("Cross wins")
                f.write("Cross wins\n")
                return 1
            elif a[0][i] == 2:
                print("Naught wins")
                f.write("Naught wins\n")
                return 2

        i += 1
    if (a[0][0] == a[1][1] and a[0][0] == a[2][2]) or (a[0][2] == a[1][1] and a[0][2] == a[2][0]):
        if a[1][1] == 1:
            print("Cross wins")
            f.write("Cross wins\n")
            return 1
        elif a[1][1] == 2:
            print("Naught wins")
            f.write("Naught wins\n")
            return 2
    return 0


a = [0] * 3
for i in range(3):
    a[i] = [0] * 3

f = open('log.txt', 'r')
lines = f.readlines()
if len(lines)== 0:
    lines.append("0:0")
print(lines[0])
line = lines[-1].split(":")
xwin = int(line[0])
owin = int(line[1])
f.close()
f = open('log.txt', 'a')

hod = 0
while True:
    print()

    if hod % 2 == 0:
        print("Ход X:")

    else:
        print("Ход O:")

    try:

        x = int(input("X = "))

        y = int(input("Y = "))

    except ValueError:

        print("Необходимо ввести цифру от 0 до 2")

        continue  # исли ввели не числа, идем к началу цикла

    if x >= 0 and x <= 2 and y >= 0 and y <= 2 and a[x][y] == 0:

        if hod % 2 == 0:
            a[x][y] = 1
            s = "Cross on " + str(x)+ " " + str(y)+"\n"
            f.write(s)

        else:
            a[x][y] = 2
            s = "Naught on " + str(x) + " " + str(y)+"\n"
            f.write(s)

    else:

        print("Неверно введены координаты")

        continue

    hod += 1

    win = checkvictory()

    view()

    if win == 1:
        s = str(xwin+1)+":"+str(owin)+"\n"
        print(s)
        f.write(s)
        f.close()
        break
    if win == 2:
        s = str(xwin) + ":" + str(owin+1)+"\n"
        print(s)
        f.write(s)
        f.close()
        break

    if hod == 9:
        s = str(xwin) + ":" + str(owin)+"\n"
        f.write(s)
        print("НИЧЬЯ")
        print(s)
        f.write("Draw\n")
        f.close()
        break
