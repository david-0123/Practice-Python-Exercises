def checkRow(row):
    if row[0] == row[1] == row[2] == "X":
        return "P1"
    elif row[0] == row[1] == row[2] == "O":
        return "P2"
    else:
        return False

def checkCol(game):
    for i in range(3):
        if game[0][i] == game[1][i] == game[2][i] == "X":
            return "P1"
        elif game[0][i] == game[1][i] == game[2][i] == "O":
            return "P2"

    return False

def checkDiag(game):
    if game[0][0] == game[1][1] == game[2][2] == "X":
        return "P1"
    elif game[0][0] == game[1][1] == game[2][2] == "O":
        return "P2"
    elif game[0][2] == game[1][1] == game[2][0] == "X":
        return "P1"
    elif game[0][2] == game[1][1] == game[2][0] == "O":
        return "P2"
    else:
        return False

def checkWin(board):
    for i in range(3):
        if checkRow(board[i]) == "P1":
            print("Player 1 wins!")
            return True
        elif checkRow(board[i]) == "P2":
            print("Player 2 wins!")
            return True

    if checkCol(board) == "P1":
        print("Player 1 wins!")
        return True
    elif checkCol(board) == "P2":
        print("Player 2 wins!")
        return True

    if checkDiag(board) == "P1":
        print("Player 1 wins!")
        return True
    elif checkDiag(board) == "P2":
        print("Player 2 wins!")
        return True

    return False

def drawHor(size):
    for i in range(size):
        print(" ---", end="")

def drawVert(size, row):
    for j in range(size):
        print("|", end=" "+str(row[j])+" ")
    print("|", end="")

def drawBoard(size, board):
    for k in range(size):
        drawHor(size)
        print()
        drawVert(size, board[k])
        print()
    drawHor(size)

boardSize = 3
game = [[' ' for a in range(boardSize)] for b in range(boardSize)]

empty = boardSize ** 2
player1 = True

drawBoard(boardSize,game)
print()
while empty > 0:
    if player1:
        print("Player 1's Turn")
        symbol = "X"
    else:
        print("Player 2's Turn")
        symbol = "O"

    try:
        move = input("Enter your move: ").strip()
        row = int(move.split(",")[0])-1
        col = int(move.split(",")[1])-1

        if game[row][col] == ' ' and row >= 0 and col >= 0:
            game[row][col] = symbol
            empty -= 1
            player1 = not player1
            print()
            drawBoard(boardSize,game)
            print()
            if checkWin(game):
                break
        else:
            print("Invalid move\n")

    except (IndexError, ValueError):
        print("Invalid move\n")

print("Game Over!")