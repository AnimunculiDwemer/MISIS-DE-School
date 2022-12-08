import time


class Nuliki:
    def __init__(self):
        self.go = 0
        self.matrix = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
        self.close = False
        self.g = dict()
        self.g[1] = [0, 0]
        self.g[2] = [0, 1]
        self.g[3] = [0, 2]
        self.g[4] = [1, 0]
        self.g[5] = [1, 1]
        self.g[6] = [1, 2]
        self.g[7] = [2, 0]
        self.g[8] = [2, 1]
        self.g[9] = [2, 2]

    def new_game(self):
        self.go = 0
        self.matrix = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]

    def get_field(self):
        return self.matrix

    def check_field(self):
        if self.matrix[0][0] == self.matrix[0][1] == self.matrix[0][2] and self.matrix[0][0] != "-":
            if self.matrix[0][0] == "X":
                return "X"
            else:
                return "0"
        elif self.matrix[0][0] == self.matrix[1][1] == self.matrix[2][2] and self.matrix[0][0] != "-":
            if self.matrix[0][0] == "X":
                return "X"
            else:
                return "0"
        elif self.matrix[2][0] == self.matrix[1][1] == self.matrix[0][2] and self.matrix[1][1] != "-":
            if self.matrix[1][1] == "X":
                return "X"
            else:
                return "0"
        elif self.matrix[1][0] == self.matrix[1][1] == self.matrix[1][2] and self.matrix[1][1] != "-":
            if self.matrix[1][1] == "X":
                return "X"
            else:
                return "0"
        elif self.matrix[2][0] == self.matrix[2][1] == self.matrix[2][2] and self.matrix[2][2] != "-":
            if self.matrix[2][2] == "X":
                return "X"
            else:
                return "0"
        elif self.matrix[0][0] == self.matrix[1][0] == self.matrix[2][0] and self.matrix[0][0] != "-":
            if self.matrix[0][0] == "X":
                return "X"
            else:
                return "0"
        elif self.matrix[0][1] == self.matrix[1][1] == self.matrix[2][1] and self.matrix[1][1] != "-":
            if self.matrix[1][1] == "X":
                return "X"
            else:
                return "0"
        elif self.matrix[0][2] == self.matrix[1][2] == self.matrix[2][2] and self.matrix[2][2] != "-":
            if self.matrix[2][2] == "X":
                return "X"
            else:
                return "0"
        elif self.go == 9:
            return "D"
        else:
            return "NO"

    def make_move(self, kl):
        if self.close:
            return "Игра уже завершена"
        print(kl)
        row, col = self.g[int(kl)]
        self.go += 1
        if self.matrix[row][col] == "-":
            if self.go % 2 == 1:
                self.matrix[row][col] = "X"
            else:
                self.matrix[row][col] = "0"
            check = self.check_field()
            if check == "X":
                self.close = True
                return "Победил игрок X"
            elif check == "0":
                self.close = True
                return "Победил игрок 0"
            elif check == "D":
                self.close = True
                return "Ничья"
            else:
                return 'Ход оппонента'
        else:
            self.go -= 1
            return 'Клетка ' + str(kl) + ' уже занята'


def game(first, second):
    sch = 0
    game = Nuliki()
    game.new_game()

    def send(mesto_id, id, mess, keyboard=None):
        #vk_session.method("messages.send", {mesto_id: id, "message": mess, "random_id": 0, "keyboard": keyboard})
        if "оппонента" in mess:
            return
        if "|" in mess:
            print(mess)
        else: print(mess, id)

    def out(game, id):
        k = ""
        for i in game.get_field():
            k += "| " + " | ".join(i) + " |\n"
        send("user_id", id, k)

    def check_move(id):
        #for event in longpoll.listen():
        #    if event.type == VkEventType.MESSAGE_NEW.MESSAGE_NEW and event.to_me and event.text:
        response = input()
        if response.isdigit() and 1 <= int(response) <= 9:
            return response
        else:
            print("Ошибка, введите номер клетки.")
            print("1 2 3\n4 5 6\n7 8 9")
            return ""

    #send("user_id", first, 'Игра началась вы Х. [id{}|Ваш противник]'.format(second))
    #send("user_id", second, 'Игра началась вы 0, ждите хода [id{}|оппонента]'.format(first))

    while 1:
        if sch % 2 == 0:
            player = first
        else:
            player = second
        send("user_id", player, 'Ваш ход')
        out(game, player)
        k = check_move(player)
        while k == "":
            time.sleep(1)
            k = check_move(player)
        c = game.make_move(k)
        if c == "Ход оппонента":
            send("user_id", player, c)
        elif "Клетка" == c[:6:]:
            send("user_id", player, c)
            continue
        else:
            send("user_id", first, c)
            out(game, first)
            send("user_id", second, c)
            out(game, second)
            break
        sch += 1



game("X", "O")
