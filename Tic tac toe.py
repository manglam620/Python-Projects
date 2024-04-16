import random
Player_mark = {"player1": "", "player2": ""}
play = True


def player_symbol():
    symbol = ""

    while symbol not in ["X", "O"]:
        symbol = input("Player1 Choose your symbol either X or O: ").upper()

        if symbol not in ["X", "O"]:
            print("Invalid input. Choose either X or O")

    Player_mark["player1"] = symbol

    if symbol == "X":
        Player_mark["player2"] = "O"
    else:
        Player_mark["player2"] = "X"

    print("\n" * 50)
    print("Symbol of Player1 is {} and Player2 is {}".format(Player_mark["player1"], Player_mark["player2"]))


def choose_player():
    if random.randint(0, 1) == 0:
        return "player1"
    else:
        return "player2"


def display_board():
    print("   |   |")
    print(f" {choice_list[1]} | {choice_list[2]} | {choice_list[3]}")
    print("   |   |")
    print("___________")
    print("   |   |")
    print(f" {choice_list[4]} | {choice_list[5]} | {choice_list[6]}")
    print("   |   |")
    print("___________")
    print("   |   |")
    print(f" {choice_list[7]} | {choice_list[8]} | {choice_list[9]}")
    print("   |   |\n")


def turn():
    global player
    if count == 0 or count % 2 == 0:
        print(player + "'s turn :")
    else:
        if player == "player1":
            print("player1's turn")
        else:
            print("player2's turn")


def user_input():
    digit = ""

    while not digit.isdigit():
        temp = input("Select your box :")

        if not temp.isdigit():
            print("Invalid input. Try again")
            continue

        elif int(temp) not in range(1, 10):
            print("Invalid input. Choose number between (1 - 9).")
            continue

        elif temp in remaining_choice:
            print("This box is already used !!!!!\nTry another one.")
            continue

        digit = temp
        remaining_choice.append(digit)

    return int(digit)


def winner_check():
    while ((choice_list[1] == choice_list[2] == choice_list[3] != " ") or (choice_list[4] == choice_list[5] == choice_list[6] != " ") or
       (choice_list[7] == choice_list[8] == choice_list[9] != " ") or (choice_list[1] == choice_list[4] == choice_list[7] != " ") or
       (choice_list[2] == choice_list[5] == choice_list[8] != " ") or (choice_list[3] == choice_list[6] == choice_list[9] != " ") or
       (choice_list[1] == choice_list[5] == choice_list[9] != " ") or (choice_list[3] == choice_list[5] == choice_list[7] != " ")):
        print("\n" * 50)
        display_board()

        if count % 2 == 0:
            print(player + " Won!!!!!")
            break
        else:
            if player == "player2":
                print("Player1 Won!!!!!")
            else:
                print("Player2 Won!!!!!")
            break

    return ((choice_list[1] == choice_list[2] == choice_list[3] != " ") or (choice_list[4] == choice_list[5] == choice_list[6] != " ") or
       (choice_list[7] == choice_list[8] == choice_list[9] != " ") or (choice_list[1] == choice_list[4] == choice_list[7] != " ") or
       (choice_list[2] == choice_list[5] == choice_list[8] != " ") or (choice_list[3] == choice_list[6] == choice_list[9] != " ") or
       (choice_list[1] == choice_list[5] == choice_list[9] != " ") or (choice_list[3] == choice_list[5] == choice_list[7] != " "))


def draw_check():
    if len(remaining_choice) == 9:
        print("\n" * 50)
        display_board()
        print("It's a DRAW!!!!!")
        return True


def play_again():
    global play
    while True:
        ask = input("Do you want to play again?\nType Y for yes and N for no.")
        ask1 = ask.upper()
        if ask1 not in ["Y", "N"]:
            print("Invalid input.")
            continue
        elif ask1 == "N":
            play = False
            print("Got it")
            break
        else:
            play = True
            print("\n" * 50)
            break


print("----------- WELCOME TO TIC TAC TOE GAME -----------\n"
      "Rules : 1) Select Symbol either X or O\n"
      "        2) Select number (1 - 9) to fill the corresponding box\n"
      "   |   |   \n"
      " 1 | 2 | 3 \n"
      "___|___|___\n"
      "   |   |   \n"
      " 4 | 5 | 6 \n"
      "___|___|___\n"
      "   |   |   \n"
      " 7 | 8 | 9 \n"
      "   |   |   \n")


while True:
    choice_list = [" "]*10
    remaining_choice = []
    player_symbol()
    player = choose_player()
    print(player + " will go first")
    count = 0
    while play:
        display_board()
        turn()
        choice = user_input()
        choice_list[choice] = Player_mark[player]
        if winner_check():
            play_again()
            break
        elif draw_check():
            play_again()
            break
        print("\n" * 50)
        count += 1
        if player == "player1":
            player = "player2"
        else:
            player = "player1"
    if not play:
        break
