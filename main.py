from tkinter import *
import time
import datetime

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
#Setting icons
# for k, v in positions.items():
#     c.create_image(positions[k][0] * 106 + 53, positions[k][1] * 106 + 53, image= icons[k], tag= k)

root.mainloop()