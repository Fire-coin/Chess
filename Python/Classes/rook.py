from Classes.chesspiece import Piece
# I will calculate castling separately in chess.py file

class Rook(Piece):
    def __init__(self, position: list[int], color: int, ID: int) -> None:
        super().__init__(position, color, ID)
        self.firstMove = True
    
    def getMoves(self, chessboard: list[list[int]]) -> list[list[int]]:
        moves = []
        row = self.position[1]
        column  = self.position[0]
        
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
        
        return moves

if __name__ == "__main__":
    r = Rook([4, 3], 1, 0)
    ch = []
    for i in range(8):
        ch.append([2] * 8)
    ch[3][4] = 1
    ch[6][4] = 0
    for i in ch:
        print(*i)
    arr = r.getMoves(ch)
    print(arr)
    print()
    for column, row in arr:
        ch[row][column] = 9
    
    for i in ch:
        print(*i)