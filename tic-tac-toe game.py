# Приветствие
print("\t"'         HI its tic-tac-toe game.'+"\n")

# заводим кортеж с выиграшными комбинациями
WIN_RULES = (
    (4, 5, 6),
    (1, 2, 3),
    (1, 4, 7),
    (2, 5, 8),
    (3, 6, 9),
    (3, 5, 7),
    (1, 5, 9),
    (7, 8, 9)
)

#функция проверки победителя
def test_WIN(n):
    for i in WIN_RULES:
        if len(set(i).intersection(n)) == 3:
            return f"win combinations {i}"
    #return False

# функция создания поля
def Game_F():
    print("\t","\t","GRID")
    print("\t"," ",["0","1","2"])
    print("______________________")
    field_XO = [[str("-") for i in range(1,4)] for j in range(1,4)]
    count = 0
    for i in field_XO:
        t = count
        print([t],"--",i) #  напечатанные сверху и сбоку цифры от 0 до 2, координаты по каим игрок ходит.
        count += 1

# функция краткого описания игры и правил
def Rules():
    text ="""Tic-tac-toe is played on a three-by-three grid by two players, 
who alternately place the marks X and O in one of the nine spaces in the grid.
The player who succeeds in placing three of their marks in a horizontal, vertical, 
or diagonal row is the winner. """
    print("\t""         Informations about game")
    print("\t", "                RuleS", "\n""______________________________________________________________________________")
    print(f"{text}")
    print()
    print("""You see grid, there are - space for marks, and numbers this are coordinates for moves""")


# функция запуска игры
def enter_game():
    a = input().upper()
    print(a)
    while a != "Y":
        if a == "N":
            break
        else:
            print("Incorrect input, try again")
            a = input().upper()
    return Game_F()

# функция игры
def Game():
    Rules()
    Game_F()
    print("If you want to play, print Y, if no print N")
    Enter_G = input("Make your choice : ").upper()
    while Enter_G != "Y" or Enter_G != "N":
        if Enter_G == "N":
            break
        elif Enter_G == "Y":
            field_XO = [[str("-") for i in range(1, 4)] for j in range(1, 4)]
            move_count = 0 #счетчик ходов
            F_index = [1, 2, 3, 4, 5, 6, 7, 8, 9] # заводим переменную, в дальнейшем будем использовать как ключ для словаря с ходами
            while move_count <= 8:
                move_x = list(input("its move X, enter coordinates separated by space in coordinates (from 0 to 2): ").split(" "))# просим сделать ход тому, кто играет Х в формате координат от 0,2 через пробел
                # Блок проверок хода Х на правельность ввода с соответсвием с правилами игры. А иммено ввод кородинат через пробел
                while any(i.isalpha() for i in move_x) or len(move_x) != 2 or any(i in [""," ","!","&"] for i in move_x):
                    move_x = list(input("its move X, enter coordinates separated by space: ").split(" "))
                su_x, do_x = move_x
                if int(do_x) >= 3 or int(su_x) >= 3 or field_XO[int(move_x[0])][int(move_x[1])] != "-":
                    move_x = list(input("incorrect, you must enter only number (from 0 to 2) or this cell occupied : ").split(" "))
                field_XO[int(move_x[0])][int(move_x[1])] = "X" # добавление Х на поле
                for i in field_XO:
                    print(i)
                XY_move = []
                # блок преобразования ходов Х в кортеж для подальшей сверки с комбинациями выиграшей
                for i in field_XO:
                    for j in i:
                        XY_move.append(j)
                XY_coord = list(zip(XY_move, F_index))
                X_combin = []
                for i in XY_coord:
                    if i[0] == "X":
                        X_combin.append(i[1])
                    else:
                        continue
                print(X_combin, "X combinations")
                if move_count > 1:
                    X_combin = set(X_combin)
                    compearX = test_WIN(X_combin)
                    if compearX:
                        print(compearX)
                        print("You WIN!!")
                        return
                move_count += 1 # подсчет ходов
                print(move_count)
                if move_count == 9: # ничья если все поле заполнено а победителя нет(9 ходов)
                    print("DRAW")
                    break
                move_o = list(input("its move O, enter coordinates separated by space: ").split(" "))
                ## Блок проверок хода O на правельность ввода с соответсвием с правилами игры. А иммено ввод кородинат через пробел
                while any(i.isalpha() for i in move_o) or len(move_o) != 2 or any(i in ["", " ", "!", "&"] for i in move_o):
                    move_o = list(input("its move O, enter coordinates separated by space: ").split(" "))
                su_y, do_y = move_o
                if int(do_y) >= 3 or int(su_y) >= 3 or field_XO[int(move_o[0])][int(move_o[1])] != "-":
                    move_o = list(input("incorrect, you must enter only number (from 0 to 2) or this cell occupied : ").split(" "))
                field_XO[int(move_o[0])][int(move_o[1])] = "O"  # добавление О на поле
                for i in field_XO:
                    print(i)
                XY_move = []
                # блок преобразования ходов О в кортеж для подальшей сверки с комбинациями выиграшей
                for i in field_XO:
                    for j in i:
                        XY_move.append(j)
                # блок где функция сверяет два множества и выдает или выиграш или продолжает игру
                XY_coord = list(zip(XY_move, F_index))
                Y_combin = []
                for i in XY_coord:
                    if i[0] == "O":
                        Y_combin.append(i[1])
                    else:
                        continue
                print(Y_combin, "Y combinations")
                # блок где функция сверяет два множества и выдает или выиграш или продолжает игру
                Y_combin = set(Y_combin)
                compearY = test_WIN(Y_combin)
                if move_count > 1:
                    if compearY:
                        print(compearY)
                        print("You WIN!!")
                        return
                move_count += 1 # подсчет ходов
        else:
            Enter_G = input("Make your choice : ").upper()
Game()

