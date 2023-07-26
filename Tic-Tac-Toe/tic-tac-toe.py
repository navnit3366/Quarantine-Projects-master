import random
from time import sleep


def displayBoard():
    print(board[0][0] + "|" + board[0][1] + "|" + board[0][2])
    print("-+-+-")
    print(board[1][0] + "|" + board[1][1] + "|" + board[1][2])
    print("-+-+-")
    print(board[2][0] + "|" + board[2][1] + "|" + board[2][2])


def isWinning(boards, player):
    if boards[0][0] == boards[0][1] == boards[0][2] == player or \
            boards[1][0] == boards[1][1] == boards[1][2] == player or \
            boards[2][0] == boards[2][1] == boards[2][2] == player or \
            boards[0][0] == boards[1][1] == boards[2][2] == player or \
            boards[0][2] == boards[1][1] == boards[2][0] == player or \
            boards[0][0] == boards[1][0] == boards[2][0] == player or \
            boards[0][1] == boards[1][1] == boards[2][1] == player or \
            boards[0][2] == boards[1][2] == boards[2][2] == player:
        return True


def chance(player):
    x, y = map(int, input().strip().split())
    while x < 0 or y < 0 or x > 3 or y > 3 or board[x - 1][y - 1] != " ":
        print("Wrong input! Try again")
        x, y = map(int, input().strip().split())
        if board[x - 1][y - 1] != " ":
            print("The place is already occupied, enter another values:")
            x, y = map(int, input().strip().split())
    board[x - 1][y - 1] = player


def computer(player):
    moves = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]
    # x, y = moves[random.randrange(0, 8)]
    # while board[x][y] != " ":
    #     x, y = moves[random.randrange(0, 8)]
    # board[x][y] = player
    # sleep(1)

    p2 = ("O", "X")[player == "O"]
    copy = board[:]
    for players in [player, p2]:
        for i in moves:
            if copy[i[0]][i[1]] == " ":
                copy[i[0]][i[1]] = players
                if isWinning(copy, players):
                    x, y = i
                    board[x][y] = player
                    sleep(1)
                    displayBoard()
                    return
                else:
                    copy[i[0]][i[1]] = " "

    x, y = moves[random.randrange(0, 8)]
    while board[x][y] != " ":
        x, y = moves[random.randrange(0, 8)]
    board[x][y] = player
    sleep(1)

    displayBoard()
    return


print("Who do you want to play against?")
print("Enter 1 to play against Computer")
print("Enter 2 to play against your player i.e a 2 player game")
play = int(input("Enter your choice:")) - 1

board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

name1 = input("Enter name of player 1:")
name2 = ''
if play == 1:
    name2 = input("Enter name of player 2:")

player1 = input(name1 + ", what do you choose?(X/O) :")
while player1 != "X" and player1 != "O":
    print("Wrong input! Please try again")
    player1 = input("What do you choose?(X/O) :")

player2 = ("O", "X")[player1 == "O"]
displayBoard()

entry = 9

running = True

while running:
    print("It's " + name1 + "'s turn, enter the row and column number, separated by spaces, where you want to put your "
          "piece:")
    chance(player1)
    displayBoard()
    entry -= 1
    if isWinning(board, player1):
        print(name1 + " won!!!")
        break
    if entry == 0:
        print("IT's A DRAW!!!")
        break

    if play == 0:
        print("It is computer's turn.")
        computer(player2)
        entry -= 1
        if isWinning(board, player2):
            print("Computer won!!!")
            break

    elif play == 1:
        print("It's " + name2 + "'s turn, enter the row and column number, separated by spaces, where you want to put "
                                "your piece:")
        chance(player2)
        displayBoard()
        entry -= 1
        if isWinning(board, player2):
            print(name2 + " won!!!")
            break

print("Thank you for playing.")
