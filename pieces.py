from CONST import colors, pieces

def remove_squares_not_in_board(moves: list[tuple]) -> None:
    moves = list(filter(
        lambda move: 
            (move[0] in range(0,8)) and (move[1] in range(0,8))
        , moves))
        
class Piece:
    symbol: tuple

    def __init__(self, x: int, y: int, color: colors):
        self.x = x
        self.y = y
        self.color = color

    def __str__(self):
        """returns the symbol found in CONST.pieces"""
        return self.symbol[self.color.value]

    def move_to(self, x: int, y: int) -> None:
        """Moves pieces"""
        self.x = x
        self.y = y
class Pawn(Piece):
    symbol: tuple = pieces.PAWN.value
    start_square: bool = False

    def __post_init__(self):
        if ((self.y == 1 and self.color == colors.BLACK) 
            or 
            (self.y == 6 and self.color == colors.WHITE)): 
                self.start_square = True
        else: 
            self.start_square = False
    
    def moves(self) -> list[tuple]:
        scope = []
        if self.color == colors.WHITE:
            scope = [(self.x    , self.y - 1), 
                     (self.x - 1, self.y - 1),
                     (self.x + 1, self.y - 1)]
            if self.start_square:
                scope.append((self.x, self.y - 2))
        elif self.color == colors.BLACK:
            scope = [(self.x    , self.y + 1), 
                     (self.x - 1, self.y + 1),
                     (self.x + 1, self.y + 1)]
            if self.start_square:
                scope.append((self.x, self.y + 2))
        
        remove_squares_not_in_board(scope)
        return scope
class Bishop(Piece):
    symbol: tuple = pieces.BISHOP.value
class Knight(Piece):
    symbol: tuple = pieces.KNIGHT.value
class Rook(Piece):
    symbol: tuple = pieces.ROOK.value
class Queen(Piece):
    symbol: tuple = pieces.QUEEN.value
class King(Piece):
    symbol: tuple = pieces.KING.value


if __name__ == "__main__":
    bonde = Pawn(x=1,y=2,color=colors.WHITE)
    print(str(bonde))