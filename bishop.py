import copy

class Bishop:
    def __init__(self, position: list[int], color: bool, ID: int) -> None:
        self.position = position
        self.color = color
        self.ID = ID
    
    def getMoves(self, chessboard: list[list[int]]) -> list[list[int]]:
        
        moves = []
        row = self.position[1]
        col = self.position[0]
        
        # Checking for moves in righ up direction
        r = row - 1
        c = col + 1
        try:
            while (r >= 0 and col <= 7):
                if chessboard[r][c] == 2: # If cell is free
                    moves.append([c, r])
                elif chessboard[r][c] == (not self.color): # If it meets oposite color piece it can take it and stop
                    moves.append([c, r])
                    break
                else: # If there is piece of same color as bishop
                    break
                r -= 1
                c += 1
        except IndexError:
            pass
        
        # Checking for moves in right bottom direction
        r = row + 1
        c = col + 1
        try:
            while (r <= 7 and c <= 7):
                if chessboard[r][c] == 2: # If cell is free
                    moves.append([c, r])
                elif chessboard[r][c] == (not self.color): # If there is piece of other color than bishop on cell
                    moves.append([c, r])
                    break
                else: # If there is piece of same color as bishop on cell
                    break
                r += 1
                c += 1
        except IndexError:
            pass
        
        #Checkig for moves in left up direction
        r = row - 1
        c = col - 1
        try:
            while (r >= 0 and c >= 0):
                if chessboard[r][c] == 2: # If cell is free
                    moves.append([c, r])
                elif chessboard[r][c] == (not self.color): # If there is piece of other color than bishop on cell
                    moves.append([c, r])
                    break
                else: # If there is piece of the same color as bishop on cell
                    break
                r -= 1
                c -= 1
        except IndexError:
            pass
        
        # Checking for moves in left bottom direction
        r = row + 1
        c = col - 1
        try:
            while (r <= 7 and col >= 0):
                if chessboard[r][c] == 2: # If cell is free
                    moves.append([c, r])
                elif chessboard[r][c] == (not self.color): # If there is piece of other color than bishop on cell
                    moves.append([c, r])
                    break
                else: # If there is piece of the same color as bishop on cell
                    break
                r += 1
                c -= 1
        except IndexError:
            pass
        
        return moves
    
    def getPosition(self) -> list[int]:
        return self.position
    
    def setPosition(self, newPosition: list[int]) -> None:
        self.position = newPosition
    
    def tryMove(self, newPosition: list[int], chessboard: list[list[int]]) -> tuple:
        possibleMoves = self.getMoves(chessboard)
        oldPosition = self.position
        chboard = copy.deepcopy(chessboard)
        self.setPosition(newPosition)
        valid = (newPosition in possibleMoves)
        
        chboard[oldPosition[1]][oldPosition[0]] = -1
        chboard[self.position[1]][self.position[0]] = int(self.color)
        
        self.setPosition(oldPosition) # Setting back old possition
        
        return tuple([chboard, oldPosition, valid])
    
    def setPositionChessboard(self, newPosition: list[int], chessboard: list[list[int]]) -> None:
        column = newPosition[0]
        row = newPosition[1]
        
        oldColumn = self.position[0]
        oldRow = self.position[1]
        
        chessboard[oldRow][oldColumn] = -1
        chessboard[row][column] = self.color
        
        self.setPosition(newPosition)

if __name__ == "__main__":
    b = Bishop([3, 4], 1, 0)
    ch = []
    for i in range(8):
        ch.append([2] * 8)
    # ch[7][6] = 1
    # ch[6][4] = 0
    ch[4][3] = 1
    ch[3][3] = 0
    ch[6][2] = 0
    for i in ch:
        print(*i)
    arr = b.getMoves(ch)
    print(arr)
    print()
    for column, row in arr:
        ch[row][column] = 9
    
    for i in ch:
        print(*i)