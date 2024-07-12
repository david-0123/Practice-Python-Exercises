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

while empty > 0:
    drawBoard(boardSize,game)
    print()
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
        else:
            print("Invalid move\n")

    except (IndexError, ValueError):
        print("Invalid move\n")

print("Game Over!")