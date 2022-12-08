from random import *
 
 
def land(field):
    for i in range(3):
        print("---------")
        for j in range (3):
            if j == 2:
                print(f"|{field[i][j]}|")
            else:
                print(f"|{field[i][j]}", end='|')
    print("---------")
    return 0
 
 
def move(place):
    while(True):
        try:
            n = int(input(place))
        except:
            print("It's not a number")
        else:
            if n <=3 and n >= 1:
                return n
            else:
                print("n should be a number from 1 to 3")
 
 
#This is very bad method in terms of OOP principles but it works at least:)
def player_move(player, field):
    while(True):
        stroke = move(f"Player {player} stroke: ")-1
        column = move(f"Player {player} column: ")-1
        if (field[stroke][column] == " "):
            if player == "1":
                field[stroke][column] = "X"
                win = check_win(stroke, column, field, player, "X")
                if win == 1:
                    return 1 
                return 0
            if player == "2":
                field[stroke][column] = "O"
                win = check_win(stroke, column, field, player, "O")
                if win == 1:
                    return 1 
                return 0
        else:
            print("There is something already")
 
 
#This one also bad designed
def check_win(stroke, column, field, player, player_mark):
    count = 0
    for i in range(3):
        if field[stroke][i] == player_mark:
            count += 1
        else:
            count = 0
            break
        if count == 3:
            for i in range(3):
                field[stroke][i] = "W"
            return 1
    for i in range(3):
        if field[i][column] == player_mark:
            count += 1
        else:
            count = 0
            break
        if count == 3:
            for i in range(3):
                field[i][column] = "W"
            return 1
    if (column == stroke):
        for i in range(3):
            if field[i][i] == player_mark:
                count += 1
            else:
                count = 0
                break
            if count == 3:
                for i in range(3):
                    field[i][i] = "W"
                return 1
    if (column + stroke == 2):
        for i in range(3):
            if field[2-i][i] == player_mark:
                count += 1
            else:
                count = 0
                break
            if count == 3:
                for i in range(3):
                    field[2-i][i] = "W"
                return 1
    return 0
 
 
def endgame():
    print("Do you want to continue?")
    while (True):
        will = input()
        if will.upper() in decline:
            return True
        elif will.upper() in accept:
            return False
        else:
            print("Usage: y/n or else")
 
 
decline = ["N", "NO"]
accept = ["Y", "YES"]
field = [[" "," "," "], [" "," "," "], [" "," "," "]]
counter, games = 0, 0
score = [0, 0]
endgames = False
filename = f"game#0{randrange(1, 1000)}{randrange(1, 1000)}"
file = open(filename, "w+")
while (endgames != True):
    land(field)
    game = True
    while (game == True):
        player1 = player_move("1", field)
        counter += 1
        if player1 == 1:
            print(f"Player 1 wins!")
            score[0] += 1
            land(field)
            game = False
        else:
            land(field)
        if (counter == 9) and (game == True):
            print("Tie!")
            game = False
        if game == True:
            player2 = player_move("2", field)
            counter += 1
            if player2 == 1:
                print(f"Player 2 wins!")
                score[1] += 1
                land(field)
                game = False
            else:
                land(field)
    field = [[" "," "," "], [" "," "," "], [" "," "," "]]
    games += 1
    endgames = endgame()
    file.writelines(f"Game {games}; Player 1:Player 2 - {score[0]}:{score[1]}\n")
file.close()
