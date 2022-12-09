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

            if a[i][0] == 2:
                print("Naught wins")
                f.write("Naught wins\n")
                return 2

        if a[0][i] == a[1][i] and a[2][i]:

            if a[0][i] == 1:
                print("Cross wins")
                f.write("Cross wins\n")
                return 1

            if a[0][i] == 2:
                print("Naught wins")
                f.write("Naught wins\n")
                return 2
        i += 1

    if (a[0][0] == a[1][1] and a[0][0] == a[2][2]) or (a[0][2] == a[1][1] and a[0][2] == a[2][0]):
        if a[1][1] == 1:
            print("Cross wins")
            f.write("Cross wins\n")
            return 1

        if a[1][1] == 2:
            print("Naught wins")
            f.write("Naught wins\n")
            return 2

    return 0


a = [0] * 3
for i in range(3):
    a[i] = [0] * 3

f = open('log.txt', 'r')
lines = f.readlines()
if len(lines) == 0:
    lines.append("0:0")
score = lines[-1].split(":")
xwin = int(score[0])
owin = int(score[1])
f.close()

hod = 0
f = open('log.txt', 'a')

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

        print("You must enter a number from 0 to 2")

        continue

    if 0 <= x <= 2 and 0 <= y <= 2 and a[x][y] == 0:

        if hod % 2 == 0:
            a[x][y] = 1
            s = "Cross on " + str(x) + " " + str(y)+"\n"
            f.write(s)

        else:
            a[x][y] = 2
            s = "Naught on " + str(x) + " " + str(y)+"\n"
            f.write(s)

    else:

        print("Wrong coordinates")

        continue

    hod += 1

    win = checkvictory()

    view()

    if win == 1:
        score = str(xwin + 1) + ":" + str(owin) + "\n"
        print(score)
        f.write(score)
        f.close()
        break

    if win == 2:
        score = str(xwin) + ":" + str(owin + 1) + "\n"
        print(score)
        f.write(score)
        f.close()
        break

    if hod == 9:
        score = str(xwin) + ":" + str(owin) + "\n"
        f.write(score)
        print("Draw")
        print(score)
        f.write("Draw\n")
        f.close()
        break













