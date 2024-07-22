def drawHor(size):
    for i in range(size):
        print(" ---", end="")

def drawVert(size, content):
    for j in range(size):
        print("|", end=content)
    print("|", end="")

def drawBoard(size):
    for k in range(size):
        drawHor(size)
        print()
        drawVert(size, "   ")
        print()
    drawHor(size)

boardSize = int(input("What board size? "))
drawBoard(boardSize)