import pprint

def play_is_over(field):
    combinations = []
    for i in range(3):
        combinations.append(field[i])
    for i in range(3):
        raw = []
        for j in range(3):
            raw.append(field[j][i])
        combinations.append(raw)
    main_diagonal = []
    for i in range(3):
        for j in range(3):
            if i == j:
                main_diagonal.append(field[i][j])
        combinations.append(main_diagonal)
    diagonal = []
    for i in range(3):
        diagonal.append(field[i][-i - 1])
    combinations.append(diagonal)

    for i in range(len(combinations)):
        if combinations[i].count('x') == 3 or combinations[i].count('o') == 3:
            return 1, i
    return 0, i

play = 1
steps = ['o', 'x']
current_step = steps[int(input(f'Кто начинает?\nЕсли крестики, введите 1, если нолики, введите 0>>'))]
field = [[' ' for i in range(3)] for j in range(3)]
while play:
    r_step, c_step = [int(i) for i in input(f'Ходит {current_step}.\nВведите строку и столбец хода через пробел>>').split()]
    field[r_step - 1][c_step - 1] = current_step
    res, comb_draw = play_is_over(field)
    if res:
        if 0 <= comb_draw <= 2:
            for j in range(3):
                field[comb_draw % 3][j] = '*'
        if 3 <= comb_draw <= 5:
            for j in range(3):
                field[j][comb_draw % 3] = '*'
        if comb_draw == 6:
            for i in range(3):
                field[i][i] = '*'
        if comb_draw == 7:
            for i in range(3):
                field[i][-i - 1] = '*'
        print(f'{current_step} выиграли')
        play = 0
    current_step = steps[abs(steps.index(current_step) - 1)]
    for elem in field:
        print(elem)
