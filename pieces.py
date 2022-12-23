from CONST import colors, pieces



class Piece:
    def __init__(self, x: int, y: int, color: colors):
        self.x = x
        self.y = y
        self.color = color

    def move_to(self, pos_to: tuple) -> None:
        """Moves pieces"""
        self.x = pos_to[0]
        self.y = pos_to[1]

class Pawn(Piece):
    symbol_white = pieces.PAWN.value[colors.WHITE.value]
    symbol_black = pieces.PAWN.value[colors.BLACK.value]
    start_square: bool

    def __post_init__(self):
        if ((self.y == 1 and self.color == colors.BLACK) 
            or 
            (self.y == 6 and self.color == colors.WHITE)): 
                self.start_square = True
        else: 
            self.start_square = False

class Bishop(Piece):
    symbol_white = pieces.BISHOP.value[colors.WHITE.value]
    symbol_black = pieces.BISHOP.value[colors.BLACK.value]

class Knight(Piece):
    def __str__(self):
        return "N"
class Rook(Piece):
    def __str__(self):
        return "R"
class Queen(Piece):
    def __str__(self):
        return "Q"
class King(Piece):
    def __str__(self):
        return "K"


if __name__ == "__main__":
    pass