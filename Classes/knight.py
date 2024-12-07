from Classes.chesspiece import Piece

class Knight(Piece):
    def __init__(self, position: list[int], color: bool, ID: int) -> None:
        super().__init__(position, color, ID)
    
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