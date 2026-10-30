from Classes.chesspiece import Piece

class Queen(Piece):
    def __init__(self, position: list[int], color: bool, ID: int):
        super().__init__(position, color, ID)
    
    def getMoves(self, chessboard: list[list[int]]) -> list[list[int]]:
        moves = []
        row = self.position[1]
        column = self.position[0]
        
        # Rook movement
        # Checking for moves up
        r = row - 1
        try:
            while (r >= 0):
                if chessboard[r][column] == 2:
                    moves.append([column, r])
                elif chessboard[r][column] == (not self.color):
                    moves.append([column, r])
                    break
                else:
                    break
                r -= 1
        except IndexError:
            pass
        
        # Checking for moves down
        r = row + 1
        try:
            while (r <= 7):
                if chessboard[r][column] == 2:
                    moves.append([column, r])
                elif chessboard[r][column] == (not self.color):
                    moves.append([column, r])
                    break
                else:
                    break
                r += 1
        except IndexError:
            pass
        
        # Checking for moves right
        c = column + 1
        try:
            while (c <= 7):
                if chessboard[row][c] == 2:
                    moves.append([c, row])
                elif chessboard[row][c] == (not self.color):
                    moves.append([c, row])
                    break
                else:
                    break
                c += 1
        except IndexError:
            pass
        
        # Checking for moves left
        c = column - 1
        try:
            while (c >= 0):
                if chessboard[row][c] == 2:
                    moves.append([c, row])
                elif chessboard[row][c] == (not self.color):
                    moves.append([c, row])
                    break
                else:
                    break
                c -= 1
        except IndexError:
            pass
        
        # Bishop movement
        # Checking for moves in righ up direction
        r = row - 1
        c = column + 1
        try:
            while (r >= 0 and column <= 7):
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
        c = column + 1
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
        c = column - 1
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
        c = column - 1
        try:
            while (r <= 7 and column >= 0):
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

if __name__ == "__main__":
    q = Queen([4, 3], 1, 0)
    ch = []
    for i in range(8):
        ch.append([2] * 8)
    ch[3][4] = 1
    ch[6][4] = 0
    for i in ch:
        print(*i)
    arr = q.getMoves(ch)
    print(arr)
    print()
    for column, row in arr:
        ch[row][column] = 9
    
    for i in ch:
        print(*i)