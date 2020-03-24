from random import randint

board = []

for x in range(8):
    board.append(["0  "] * 8)


def print_board(board):
    for row in board:
        print(" ".join(row))


print("Let's play Battleship\n\n")
print_board(board)


def random_row(board):
    return randint(0, len(board) - 1)


def random_col(board):
    return randint(0, len(board[0]) - 1)


ship_row = random_row(board)
ship_col = random_col(board)
print(ship_row)
print(ship_col)

guess_row = int(input("Guess row >  "))
guess_col = int(input("Guess col >  "))

turn = 1
while turn < 6:
    if turn == 5:
        print("Game Over!")
        break

    if (guess_row < 0 or guess_row > 7) or (guess_col < 0 or guess_col > 7):
        print("Oops, that's not even in the ocean.")
        turn += 1
        print("Turn ", turn)
        guess_row = int(input("Guess row >  "))
        guess_col = int(input("Guess col >  "))

    if (guess_row != ship_row or guess_col != ship_col) or (guess_row != ship_row and guess_col != ship_col):
        print("You can't kill my ship, Dude!, Try AGAIN!!!")
        turn += 1
        print("Turn ", turn)
        guess_row = int(input("Guess row >  "))
        guess_col = int(input("Guess col >  "))

    elif guess_row == ship_row and guess_col == ship_col:
        print("You won and sank my ship and it took you %s attempts" % turn)
        break


#         elif (board[guess_row][guess_col] == "X "):
#             print("You guesses that one already.")
#             turn +=1
#
#         else:
# 		    print("You missed my battleship!")
# 		    board([guess_row][guess_col] == "X ")
#     print("Turn:", turn + 1)
#     print_board(board)