from Classes.chesspiece import Piece

class Pawn(Piece):
    def __init__(self, position: list[int], color: bool, ID: int, direction: bool) -> None:
        super().__init__(position, color, ID)
        self.direction: bool = direction # If True, then pawn moves up, down otherwise
    
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
        try:
            # Checking if first move of 2 squares is possible
            if self.firstMove and chessBoard[row + rMove * 2][column] == 2:
                moves.append([column, row + rMove * 2])
        except IndexError:
            pass
        
        try:
            # Checking if pawn can move 1 square forward
            if chessBoard[row + rMove][column] == 2:
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

if __name__ == "__main__":
    p = Pawn([5, 7], 1, 0, True)
    ch = []
    for i in range(8):
        ch.append([2] * 8)
    ch[7][5] = 1
    ch[6][4] = 0
    for i in ch:
        print(*i)
    p.setPositionChessboard([5, 6], ch)
    arr = p.getMoves(ch)
    print(arr)
    print()
    for column, row in arr:
        ch[row][column] = 9
    
    for i in ch:
        print(*i)