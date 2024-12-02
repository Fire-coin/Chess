# import tkinter as tk
import copy
# 0 is for white in matrix
# 1 is for black in matrix
# -1 is for free space in cell


class Pawn():
    def __init__(self, position: list[int], color: bool, ID: int, direction: bool) -> None:
        self.position: list[int] = position
        self.color: bool = color
        self.ID: int = ID
        self.direction: bool = direction # If True, then pawn moves up, down otherwise
        self.firstMove: bool = True
    
    def getMoves(self, chessBoard: list[list[int]]) -> list[list[int]]:
        """Checks for possible moves in on chessboard.

        Args:
            chessBoard (_type_): _description_

        Returns:
            list[list[int]]: List of possible moves of pawn, on given chessboard. Coordinates are in list
            format [x, y] / [column, row], (use in list / matrix without adding / substractig 1).
        """
        moves = []
        row = self.position[1]
        column = self.position[0]
        
        rMove = -1 if self.direction else 1 # Row move is used to increment / decrement row when 
                                            # checking for pawn movement
        #TODO Add try ... except statements to catch errors
        try:
            # Checking if first move of 2 squares is possible
            if self.firstMove and chessBoard[row + rMove * 2][column] == -1:
                moves.append([column, row + rMove * 2])
        except IndexError:
            pass
        
        try:
            # Checking if pawn can move 1 square forward
            if chessBoard[row + rMove][column] == -1:
                moves.append([column, row + rMove])
        except IndexError:
            pass
        
        try:
            # Checking if pawn can take piece of another player of column in the right
            if chessBoard[row + rMove][column + 1] == (not self.color):
                moves.append([column + 1, row + rMove])
        except IndexError:
            pass
        
        try:
            # Checking if pawn can take piece of another player of column in the left
            if chessBoard[row + rMove][column - 1] == (not self.color):
                moves.append([column - 1, row + rMove])
        except IndexError:
            pass
        
        return moves

    def getPosition(self) -> list[int]:
        return self.position

    def setPosition(self, newPosition: list[int]) -> None:
        self.position = newPosition
        
    def tryMove(self, newPosition: list[int], chessboard: list[list[int]]) -> tuple:
        """Renders how it would look like if pawn moved to specified position. Does not change
        pawn icon on canvas, this has to be done manually.

        Args:
            newPosition (_type_): _description_
            chessboard (list[list[int]]): _description_

        Returns:
            tuple: Returns tuple of how would chessboard look like after move, old position of pawn
            and if move is valid (if it can be played in normal chess game), checked by getMoves method.
        """
        possibleMoves = self.getMoves(chessboard)
        oldPosition = self.position
        chboard = copy.deepcopy(chessboard)
        self.setPosition(newPosition)
        
        chboard[oldPosition[1]][oldPosition[0]] = -1
        chboard[self.position[1]][self.position[0]] = int(self.color)
        
        valid = False
        if newPosition in possibleMoves:
            valid = True
        
        return tuple([chboard, oldPosition, valid])

    def setPositionChessboard(self, newPosition: list[int], chessboard: list[list[int]]) -> None:
        column = newPosition[0]
        row = newPosition[1]
        
        oldColumn = self.position[0]
        oldRow = self.position[1]
        
        chessboard[oldRow][oldColumn] = -1 # Removing color from square where pawn was
        chessboard[row][column] = self.color # Setting square where pawn moved to its color
        
        self.setPosition(newPosition) # Setting new position of pawn
        
        self.firstMove = False