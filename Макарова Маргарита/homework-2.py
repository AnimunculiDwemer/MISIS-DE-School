# Пояснение к коду:
# Для того, чтобы выводился счет игры, и она запускалась несколько раз, я ввела бесконечный цикл while True: 
# Для завершения работы данного цикла я брала условие, что участники могут играть до трех побед (то есть как только первый или второй игрок наберет 3 очка, программа прекращает свою работу)


#Крестики-нолики
import pickle
score1=0 #Счетчик ведения игры для первого игрока
score2=0 #Счетчик ведения игры для второго игрока
while True: #Бесконечный цикл, позволяющий игре запускаться заново
    mas=[[0, 0, 0], [0, 0, 0], [0, 0, 0]] #поле для игры
    print("Изначальное поле для игры")
    for i in range(len(mas)):
        for k in range(len(mas[i])):
            print(mas[i][k], end = " ")
        print()

    def CheckX(): #Проверка выигрыша X
        if (mas[0][0]=="X"and mas[0][1]=="X"and mas[0][2]=="X"):
            print("Победил X")
            mas[0][0]=mas[0][1]=mas[0][2]="*"
            for i in range(len(mas)):
                for k in range(len(mas[i])):
                    print(mas[i][k], end = " ")
                print()
            return 1
        if (mas[1][0]=="X"and mas[1][1]=="X"and mas[1][2]=="X"):
            print("Победил X")
            mas[1][0]=mas[1][1]=mas[1][2]="*"
            for i in range(len(mas)):
                for k in range(len(mas[i])):
                    print(mas[i][k], end = " ")
                print()
            return 1
        if (mas[2][0]=="X"and mas[2][1]=="X"and mas[2][2]=="X"):
            print("Победил X")
            mas[2][0]=mas[2][1]=mas[2][2]="*"
            for i in range(len(mas)):
                for k in range(len(mas[i])):
                    print(mas[i][k], end = " ")
                print()
            return 1
        if (mas[0][0]=="X"and mas[1][0]=="X"and mas[2][0]=="X"):
            print("Победил X")
            mas[0][0]=mas[1][0]=mas[2][0]="*"
            for i in range(len(mas)):
                for k in range(len(mas[i])):
                    print(mas[i][k], end = " ")
                print()
            return 1
        if (mas[0][1]=="X"and mas[1][1]=="X"and mas[2][1]=="X"):
            print("Победил X")
            mas[0][1]=mas[1][1]=mas[2][1]="*"
            for i in range(len(mas)):
                for k in range(len(mas[i])):
                    print(mas[i][k], end = " ")
                print()
            return 1
        if (mas[0][2]=="X"and mas[1][2]=="X"and mas[2][2]=="X"):
            print("Победил X")
            mas[0][2]=mas[1][2]=mas[2][2]="*"
            for i in range(len(mas)):
                for k in range(len(mas[i])):
                    print(mas[i][k], end = " ")
                print()
            return 1
        if (mas[0][0]=="X"and mas[1][1]=="X"and mas[2][2]=="X"):
            print("Победил X")
            mas[0][0]=mas[1][1]=mas[2][2]="*"
            for i in range(len(mas)):
                for k in range(len(mas[i])):
                    print(mas[i][k], end = " ")
                print()
            return 1
        if (mas[0][2]=="X"and mas[1][1]=="X"and mas[2][0]=="X"):
            print("Победил X")
            mas[0][2]=mas[1][1]=mas[2][0]="*"
            for i in range(len(mas)):
                for k in range(len(mas[i])):
                    print(mas[i][k], end = " ")
                print()
            return 1
        return 0
    def CheckO(): #Проверка выигрыша O
        if (mas[0][0]=="O"and mas[0][1]=="O"and mas[0][2]=="O"):
            print("Победил O")
            mas[0][0]=mas[0][1]=mas[0][2]="*"
            for i in range(len(mas)):
                for k in range(len(mas[i])):
                    print(mas[i][k], end = " ")
                print()
            return 1
        if (mas[1][0]=="O"and mas[1][1]=="O"and mas[1][2]=="O"):
            print("Победил O")
            mas[1][0]=mas[1][1]=mas[1][2]="*"
            for i in range(len(mas)):
                for k in range(len(mas[i])):
                    print(mas[i][k], end = " ")
                print()
            return 1
        if (mas[2][0]=="O"and mas[2][1]=="O"and mas[2][2]=="O"):
            print("Победил O")
            mas[2][0]=mas[2][1]=mas[2][2]="*"
            for i in range(len(mas)):
                for k in range(len(mas[i])):
                    print(mas[i][k], end = " ")
                print()
            return 1
        if (mas[0][0]=="O"and mas[1][0]=="O"and mas[2][0]=="O"):
            print("Победил O")
            mas[0][0]=mas[1][0]=mas[2][0]="*"
            for i in range(len(mas)):
                for k in range(len(mas[i])):
                    print(mas[i][k], end = " ")
                print()
            return 1
        if (mas[0][1]=="O"and mas[1][1]=="O"and mas[2][1]=="O"):
            print("Победил O")
            mas[0][1]=mas[1][1]=mas[2][1]="*"
            for i in range(len(mas)):
                for k in range(len(mas[i])):
                    print(mas[i][k], end = " ")
                print()
            return 1
        if (mas[0][2]=="O"and mas[1][2]=="O"and mas[2][2]=="O"):
            print("Победил O")
            mas[0][2]=mas[1][2]=mas[2][2]="*"
            for i in range(len(mas)):
                for k in range(len(mas[i])):
                    print(mas[i][k], end = " ")
                print()
            return 1
        if (mas[0][0]=="O"and mas[1][1]=="O"and mas[2][2]=="O"):
            print("Победил O")
            mas[0][0]=mas[1][1]=mas[2][2]="*"
            for i in range(len(mas)):
                for k in range(len(mas[i])):
                    print(mas[i][k], end = " ")
                print()
            return 1
        if (mas[0][2]=="O"and mas[1][1]=="O"and mas[2][0]=="O"):
            print("Победил O")
            mas[0][2]=mas[1][1]=mas[2][0]="*"
            for i in range(len(mas)):
                for k in range(len(mas[i])):
                    print(mas[i][k], end = " ")
                print()
            return 1
        return 0
        count=1
    count=1 #Счетчик ходов
    while 1:
        print("Введите координаты клетки, в которой вы хотите поставить крестик(X) или нолик(O)")
        try: # Проверка на ошибку ввода
            a = int(input("Координата столбца: "))
            b = int(input("Координата строки: "))
        except ValueError: 
            print ("Неверный формат ввода! Введите цифру от 0 до 2") 
            continue 
        if ((a==0 or a==1 or a==2)and(b==0 or b==1 or b==2)):
            if count % 2!=0:
                print("Ход X")
                for i in range(3):
                    for k in range(3):
                        if i==a and k==b:
                            mas[i][k]="X"
                            count+=1
                for i in range(len(mas)):
                    for k in range(len(mas[i])):
                        print(mas[i][k], end = " ")
                    print()
            else:
                print("Ход O")
                for i in range(3):
                    for k in range(3):
                        if i==a and k==b:
                            mas[i][k]="O"
                            count+=1
                for i in range(len(mas)):
                    for k in range(len(mas[i])):
                        print(mas[i][k], end = " ")
                    print()
        else:
            print("Неверный формат ввода! Введите цифру от 0 до 2")
            continue
    
        win1=CheckX() #Победа X
        win2=CheckO() #Победа O
        if count==10:
            print("Результатом игры стала ничья")
            print("Счетчик ходов: ", count-1)
            break
        if ((win1==1 and win2==0)or(win1==0 and win2==1)):
            if (win1==1 and win2==0):
                score1+=1
            elif (win1==0 and win2==1):
                score2+=1
            print("Счет игры равен: ", score1, ":", score2)
            break
    # Проверяем, что записалось в файл
    try:
        with open('game.bin','rb') as file:
            b1= pickle.load(file)
            b2=pickle.load(file)
    except:
        print("Ошибка работы с файлом")
    print( "Результат счетчика, сохраненный в файл", b1, b2, sep=" ")

    # Так как игра идет до трех побед, то как только набирается либо у X или O 3 очка, тогда бесконечный цикл останавливается
    if score1==3:
        break
    if score2==3:
        break
