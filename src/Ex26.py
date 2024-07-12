def checkRow(row):
    if row[0] == row[1] == row[2] == 1:
        return "P1"
    elif row[0] == row[1] == row[2] == 2:
        return "P2"
    else:
        return False

def checkCol(game):
    for i in range(3):
        if game[0][i] == game[1][i] == game[2][i] == 1:
            return "P1"
        elif game[0][i] == game[1][i] == game[2][i] == 2:
            return "P2"

    return False

def checkDiag(game):
    if game[0][0] == game[1][1] == game[2][2] == 1:
        return "P1"
    elif game[0][0] == game[1][1] == game[2][2] == 2:
        return "P2"
    elif game[0][2] == game[1][1] == game[2][0] == 1:
        return "P1"
    elif game[0][2] == game[1][1] == game[2][0] == 2:
        return "P2"
    else:
        return False

def checkWin(board):
    for i in range(3):
        if checkRow(board[i]) == "P1":
            print("Player 1 wins!")
            return
        elif checkRow(board[i]) == "P2":
            print("Player 2 wins!")
            return

    if checkCol(board) == "P1":
        print("Player 1 wins!")
        return
    elif checkCol(board) == "P2":
        print("Player 2 wins!")
        return

    if checkDiag(board) == "P1":
        print("Player 1 wins!")
        return
    elif checkDiag(board) == "P2":
        print("Player 2 wins!")
        return

    print("There was no winner :(")

finalBoard = [[1, 2, 0],
        [2, 1, 0],
        [2, 1, 0]]

checkWin(finalBoard)