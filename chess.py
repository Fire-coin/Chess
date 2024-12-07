from tkinter import *
import time
import datetime
from Classes.canvaspiece import VisiblePiece
from Github.Chess.Classes.pawn import Pawn
from Github.Chess.Classes.bishop import Bishop
from Github.Chess.Classes.knight import Knight
from Classes.king import King
from Classes.queen import Queen
from Classes.rook import Rook

selected = False
selectedID = -1

def deleteGlow():
    c.delete("glow")


def showGlow(ID):
    deleteGlow()
    possibleMoves = pieces[ID].getMoves(chessboard)
    canvasPieces[ID].showMoves(possibleMoves, chessboard)


def findFigureOnCoords(coords: list[int]):
    for key, value in pieces.items():
        if value.position == coords:
            return key


def selectCell(e: Event) -> list[int] | None:
    x = e.x
    y = e.y
    row = y // 106
    col = x // 106
    if row > 7 or row < 0 or col > 7 or col < 0:
        print("Invalid coordinates")
        return None
    else:
        print(f"row: {row}, column: {col}")
        return [col, row]


def selectFigure(e: Event):
    # TODO make function which calculates moves, also with moves as castling
    global selected
    global selectedID
    output = selectCell(e)
    if output is None:
        return
    
    col, row = output
    
    if selected: # If some figure was already selected
        possibleMoves = pieces[selectedID].getMoves(chessboard)
        if [col, row] in possibleMoves: # If selected cell is valid move
            if chessboard[row][col] != 2: # If clicked cell is not an empty cell
                pointedID = findFigureOnCoords([col, row])
                canvasPieces[pointedID].delete()
                del canvasPieces[pointedID]
                del pieces[pointedID]
            deleteGlow()
            canvasPieces[selectedID].move([col, row]) # Moves selected figure to clicked cell
            pieces[selectedID].setPositionChessboard([col, row], chessboard) # Setting positions in bit chessboard
            selected = False
            selectedID = -1
        else: # If clicked cell is not valid move
            if chessboard[row][col] == 2: # If clicked cell was empty
                selected = False
                selectedID = -1
                deleteGlow()
            else: # If there was a figure in clicked cell
                pointedID = findFigureOnCoords([col, row])
                figureColor = pieces[selectedID].color
                pointedColor = pieces[pointedID].color
                
                # If colors of clicked and selected cells are same, and it is not the same cell
                if figureColor == pointedColor and pointedID != selectedID:
                    selectedID = pointedID
                    showGlow(selectedID)
                else:
                    selected = False
                    selectedID = -1
                    deleteGlow()
    else:
        if chessboard[row][col] == 2:
            return
        
        selected = True
        selectedID = findFigureOnCoords([col, row])
        showGlow(selectedID)
    
    
    print(selected, selectedID)
    
    



root = Tk()
root.geometry("1100x1000")
root.resizable(False, False)

#White
whiteKing = PhotoImage(file= "Images\White_King.png")#Movement: Done
whiteQueen = PhotoImage(file= "Images\White_Queen.png")#Movement: Done
whiteBishop = PhotoImage(file= "Images\White_Bishop.png")#Movement: Done
whiteKnight = PhotoImage(file= "Images\White_Knight.png")#Movement: Done; Danger: Done
whiteRook = PhotoImage(file= "Images\White_Rook.png")#Movement: Done; Danger: Done
whitePawn = PhotoImage(file= "Images\White_Pawn.png")#Movement: Done; Danger: Done
#Black
blackKing = PhotoImage(file = "Images\Black_King.png")#Movement: Done
blackQueen = PhotoImage(file = "Images\Black_Queen.png")#Movement: Done
blackBishop = PhotoImage(file = "Images\Black_Bishop.png")#Movement: Done
blackKnight = PhotoImage(file = "Images\Black_Knight.png")#Movement: Done; Danger: Done
blackRook = PhotoImage(file = "Images\Black_Rook.png")#Movement: Done; Danger: Done
blackPawn = PhotoImage(file = "Images\Black_Pawn.png")#Movement: Done; Danger: Done


#Creating canvas
c = Canvas(root, bg= "Black", width= 848, height= 848, border= 1)
c.place(relx= 0.5, rely= 0.5, anchor= "center")

#Creating chessboard
counter = 1
for i in range(8):
    counter += 1
    for j in range(8):
        colour = "White" if counter % 2 == 0 else "Light Green"
        c.create_rectangle(j * 106, i * 106, (j + 1) * 106, (i + 1) * 106, fill= colour)
        counter += 1


l = "ABCDEFGH"
for i in range(8):
    Label(root, text= l[i]).place(x= i * 106 + 170, y= 50)
    Label(root, text= l[i]).place(x= i * 106 + 170, y= 925)
    Label(root, text= str(i + 1)).place(x= 100, y= i * 106 + 115)
    Label(root, text= str(i + 1)).place(x= 985, y= i * 106 + 115)

chessboard = []
for i in range(8):
    chessboard.append([2] * 8)

chessboard[0] = [1] * 8
chessboard[1] = [1] * 8

chessboard[6] = [0] * 8
chessboard[7] = [0] * 8

# Setting icons for each piece for easier use later
icons = {
    # Black pieces
    0: blackRook,
    1: blackKnight,
    2: blackBishop,
    3: blackQueen,
    4: blackKing,
    5: blackBishop,
    6: blackKnight,
    7: blackRook,
    8: blackPawn,
    9: blackPawn,
    10: blackPawn,
    11: blackPawn,
    12: blackPawn,
    13: blackPawn,
    14: blackPawn,
    15: blackPawn,
    # White pieces
    16: whitePawn,
    17: whitePawn,
    18: whitePawn,
    19: whitePawn,
    20: whitePawn,
    21: whitePawn,
    22: whitePawn,
    23: whitePawn,
    24: whiteRook,
    25: whiteKnight,
    26: whiteBishop,
    27: whiteQueen,
    28: whiteKing,
    29: whiteBishop,
    30: whiteKnight,
    31: whiteRook
}

# Creating chess pieces
pieces = {
    # Black pieces
    0: Rook([0, 0], 1, 0),
    1: Knight([1, 0], 1, 1),
    2: Bishop([2, 0], 1, 2),
    3: Queen([3, 0], 1, 3),
    4: King([4, 0], 1, 4),
    5: Bishop([5, 0], 1, 5),
    6: Knight([6, 0], 1, 6),
    7: Rook([7, 0], 1, 7),
    8: Pawn([0, 1], 1, 8, False),
    9: Pawn([1, 1], 1, 9, False),
    10: Pawn([2, 1], 1, 10, False),
    11: Pawn([3, 1], 1, 11, False),
    12: Pawn([4, 1], 1, 12, False),
    13: Pawn([5, 1], 1, 13, False),
    14: Pawn([6, 1], 1, 14, False),
    15: Pawn([7, 1], 1, 15, False),
    # White pieces
    16: Pawn([0, 6], 0, 16, True),
    17: Pawn([1, 6], 0, 17, True),
    18: Pawn([2, 6], 0, 18, True),
    19: Pawn([3, 6], 0, 19, True),
    20: Pawn([4, 6], 0, 20, True),
    21: Pawn([5, 6], 0, 21, True),
    22: Pawn([6, 6], 0, 22, True),
    23: Pawn([7, 6], 0, 23, True),
    24: Rook([0, 7], 0, 24),
    25: Knight([1, 7], 0, 25),
    26: Bishop([2, 7], 0, 26),
    27: Queen([3, 7], 0, 27),
    28: King([4, 7], 0, 28),
    29: Bishop([5, 7], 0, 29),
    30: Knight([6, 7], 0, 30),
    31: Rook([7, 7], 0, 31)
}

canvasPieces = {}

# Adding visibleFigures to canvasPieces and also placing them on canvas
for key, value in pieces.items():
    canvasPieces[key] = VisiblePiece(value.getPosition(), icons[key], 106, c, key)
    canvasPieces[key].place()

for i in chessboard:
    print(*i)

c.bind("<Button-1>", selectFigure)

root.mainloop()