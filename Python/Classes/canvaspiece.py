from tkinter import Canvas, PhotoImage

class VisiblePiece:
    def __init__(self, position: list[int], image: PhotoImage, size: int, w: Canvas, ID: int) -> None:
        self.image = image
        self.size = size
        self.position = position
        self.w = w
        self.ID = ID
    
    def setPosition(self, newPosition: list[int]) -> None:
        self.position = newPosition
    
    def getPosition(self) -> list[int]:
        return self.position
    
    def place(self) -> None:
        row = self.position[1]
        column = self.position[0]
        xCord = (column) * self.size + self.size // 2
        yCord = (row) * self.size + self.size // 2
        self.w.create_image(xCord, yCord, image= self.image, tag= f"img{self.ID}")
    
    def deleteGlow(self) -> None:
        self.w.delete("glow")
    
    def showMoves(self, moves: list[list[int]], chessboard: list[list[int]]) -> None:
        self.deleteGlow()
        for column, row in moves:
            xCord = (column) * self.size
            yCord = (row) * self.size
            if chessboard[row][column] == 2:
                self.w.create_oval(xCord + 33, yCord + 33, \
                xCord + self.size - 33, yCord + self.size - 33,\
                fill= "grey", outline= "grey", tag= "glow")
            else:
                self.w.create_oval(xCord + 33, yCord + 33, \
                xCord + self.size - 33, yCord + self.size - 33,\
                width= 5, fill= None, outline= "grey", tag= "glow")
    
    def move(self, newPosition: list[int]) -> None:
        self.setPosition(newPosition) # Sets figure position to new one
        self.w.delete(f"img{self.ID}") # Deletes figure icon from canvas
        self.place() # Sets figure icon on canvas
    
    def delete(self) -> None:
        self.w.delete(f"img{self.ID}")
    
    def setImage(self, newImage: PhotoImage) -> None:
        self.w.delete(f"img{self.ID}")
        self.image = newImage