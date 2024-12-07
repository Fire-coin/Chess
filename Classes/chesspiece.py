import copy
# 0 is for white in matrix
# 1 is for black in matrix
# 2 is for free space in cell

class Piece:
    """Base class for chess pieces.
    """
    def __init__(self, position: list[int], color: bool, ID: int) -> None:
        self.position = position
        self.color = color
        self.ID = ID
        self.firstMove = True
    
    def getPosition(self) -> list[int]:
        return self.position

    def setPosition(self, newPosition: list[int]) -> None:
        self.position = newPosition
    
    def getMoves(self, chessboard: list[list[int]]) -> list[list[int]]:
        ...
    
    def tryMove(self, newPosition: list[int], chessboard: list[list[int]]) -> tuple:
        possibleMoves = self.getMoves(chessboard)
        oldPosition = self.position
        chboard = copy.deepcopy(chessboard)
        self.setPosition(newPosition)
        valid = (newPosition in possibleMoves)
        
        chboard[oldPosition[1]][oldPosition[0]] = 2
        chboard[self.position[1]][self.position[0]] = int(self.color)
        
        self.setPosition(oldPosition) # Setting back old possition
        
        return tuple([chboard, oldPosition, valid])
    
    
    def setPositionChessboard(self, newPosition: list[int], chessboard: list[list[int]]) -> None:
        column = newPosition[0]
        row = newPosition[1]
        
        oldColumn = self.position[0]
        oldRow = self.position[1]
        
        chessboard[oldRow][oldColumn] = 2 # Removing color from square where pawn was
        chessboard[row][column] = self.color # Setting square where pawn moved to its color
        
        self.setPosition(newPosition) # Setting new position of pawn
        
        self.firstMove = False