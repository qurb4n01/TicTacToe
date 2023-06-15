canvas=["-","-","-",
        "-","-","-",
        "-","-","-"]

gameOver=False

def showTheBoard():
    print(canvas[0]+"|"+canvas[1]+"|"+canvas[2])
    print(canvas[3]+"|"+canvas[4]+"|"+canvas[5])
    print(canvas[6]+"|"+canvas[7]+"|"+canvas[8])

def xMove():
    xMove=int(input())-1
    canvas[xMove]="X"
    showTheBoard()

def oMove():
    oMove=int(input())-1
    canvas[oMove]="O"
    showTheBoard()

def checkXWin():
    def checkVertical():
        global gameOver
        if canvas[0]=="X" and canvas[3]=="X" and canvas[6]=="X":
            gameOver=True
            print("X won")
        elif canvas[1]=="X" and canvas[4]=="X" and canvas[7]=="X":
            gameOver=True
            print("X won")
        elif canvas[2]=="X" and canvas[5]=="X" and canvas[8]=="X":
            gameOver=True
            print("X won")

    def checkHorizontal():
        global gameOver
        if canvas[0]=="X" and canvas[1]=="X" and canvas[2]=="X":
            gameOver=True
            print("X won")
        elif canvas[3]=="X" and canvas[4]=="X" and canvas[5]=="X":
            gameOver=True
            print("X won")
        elif canvas[6]=="X" and canvas[7]=="X" and canvas[8]=="X":
            gameOver=True
            print("X won")

    def checkDiagonal():
        global gameOver
        if canvas[0]=="X" and canvas[4]=="X" and canvas[8]=="X":
            gameOver=True
            print("X won")
        elif canvas[2]=="X" and canvas[4]=="X" and canvas[6]=="X":
            gameOver=True
            print("X won")
    
    checkVertical()
    checkHorizontal()
    checkDiagonal()

def checkOWin():
    def checkVertical():
        global gameOver
        if canvas[0]=="O" and canvas[3]=="O" and canvas[6]=="O":
            gameOver=True
            print("O won")
        elif canvas[1]=="O" and canvas[4]=="O" and canvas[7]=="O":
            gameOver=True
            print("O won")
        elif canvas[2]=="O" and canvas[5]=="O" and canvas[8]=="O":
            gameOver=True
            print("O won")

    def checkHorizontal():
        global gameOver
        if canvas[0]=="O" and canvas[1]=="O" and canvas[2]=="O":
            gameOver=True
            print("O won")
        elif canvas[3]=="O" and canvas[4]=="O" and canvas[5]=="O":
            gameOver=True
            print("O won")
        elif canvas[6]=="O" and canvas[7]=="O" and canvas[8]=="O":
            gameOver=True
            print("O won")

    def checkDiagonal():
        global gameOver
        if canvas[0]=="O" and canvas[4]=="O" and canvas[8]=="O":
            gameOver=True
            print("O won")
        elif canvas[2]=="O" and canvas[4]=="O" and canvas[6]=="O":
            gameOver=True
            print("O won")

    checkVertical()
    checkHorizontal()
    checkDiagonal()

def checkDraw():
    k=0
    global gameOver
    for i in canvas:
        if i!="-":
            k+=1
    if k==9:
        gameOver=True
        print("Draw")


showTheBoard()
print("Enter the relevant numbers(1-9) to make your move")
while gameOver==False:
    xMove()
    checkXWin()
    checkDraw()
    if gameOver==False:
        oMove()
        checkOWin()
        checkDraw()