from Classes.chesspiece import Piece

class King(Piece):
    def __init__(self, position: list[int], color: bool, ID: int) -> None:
        super().__init__(position, color, ID)
    
    def getMoves(self, chessboard: list[list[int]]) -> list[list[int]]:
        moves = []
        row = self.position[1]
        column = self.position[0]
        
        arr = [-1, 0, 1]
        
        for dx in arr:
            for dy in arr:
                if dx == 0 and dy == 0:
                    continue
                try:
                    # King can either take or move to the cells around him, I will check 
                    # if he really can move to that cell in main program in chess.py
                    if chessboard[row + dy][column + dx] != self.color:
                        moves.append([column + dx, row + dy])
                except IndexError:
                    pass
        
        return moves

if __name__ == "__main__":
    k = King([5, 6], 1, 0)
    ch = []
    for i in range(8):
        ch.append([2] * 8)
    ch[6][5] = 1
    ch[6][4] = 0
    ch[5][4] = 1
    for i in ch:
        print(*i)
    arr = k.getMoves(ch)
    print(arr)
    print()
    for column, row in arr:
        ch[row][column] = 9
    
    for i in ch:
        print(*i)