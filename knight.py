import copy

class Knight:
    def __init__(self, position: list[int], color: bool, ID: int) -> None:
        self.position: list[int] = position
        self.color: bool = color
        self.ID: int = ID

    
    def setPosition(self, newPosition: list[int]) -> None:
        self.position = newPosition
    
    
    def getPosition(self) -> list[int]:
        return self.position
    
    
    def getMoves(self, chessboard: list[list[int]]) -> list[list[int]]:
        
        moves = []
        row = self.position[1]
        column = self.position[0]
        
        for dx, dy in [[0, 2], [0, -2], [2, 0], [-2, 0]]:
            # Moves that are up and down
            if dx == 0:
                try:
                    # X to the right
                    if chessboard[row + dy][column + 1] == 2 or chessboard[row + dy][column + 1] == (not self.color):
                        moves.append([column + 1, row + dy])
                except IndexError:
                    pass
                
                if column != 0:
                    try:
                        # X to the left
                        if chessboard[row + dy][column - 1] == 2 or chessboard[column + dy][column - 1] == (not self.color):
                            moves.append([column - 1, row + dy])
                    except IndexError:
                        pass
            else: # Moves that are left and right
                try:
                    # Y downwards
                    if chessboard[row + 1][column + dx] == 2 or chessboard[row + 1][column + dx] == (not self.color):
                        moves.append([column + dx, row + 1])
                except IndexError:
                    pass
                
                if row != 0:
                    try:
                        # Y upwards
                        if chessboard[row - 1][column + dx] == 2 or chessboard[row - 1][column + dx] == (not self.color):
                            moves.append([column + dx, row - 1])
                    except IndexError:
                        pass
        return moves

    
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
        valid = (newPossition in possibleMoves)
        
        chboard[oldPosition[1]][oldPosition[0]] = 2
        chboard[self.position[1]][self.position[0]] = int(self.color)

        self.setPosition(oldPosition) # Setting back old possition
        
        return tuple([chboard, oldPosition, valid])
    
    
    def setPositionChessboard(self, newPosition: list[int], chessboard: list[list[int]]) -> None:
        column = newPosition[0]
        row = newPosition[1]
        
        oldColumn = self.position[0]
        oldRow = self.position[1]
        
        chessboard[oldRow][oldColumn] = 2 # Removing color from square where knight
        chessboard[row][column] = self.color # Setting square where knight moved to its color
        
        self.setPosition(newPosition) # Setting new position of knight




if __name__ == "__main__":
    k = Knight([6, 7], 1, 0)
    ch = []
    for i in range(8):
        ch.append([2] * 8)
    ch[7][6] = 1
    ch[6][4] = 0
    for i in ch:
        print(*i)
    arr = k.getMoves(ch)
    print(arr)
    print()
    for column, row in arr:
        ch[row][column] = 9
    
    for i in ch:
        print(*i)
