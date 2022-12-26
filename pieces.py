from CONST import colors, repr_piece, piece_moves
import rules

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


class Bishop(Piece):
    symbol: tuple = repr_piece.BISHOP.value
    # sliding piece
    direction: set = piece_moves.BISHOP
    applied_rules = rules.get_sliding_moves

class Rook(Piece):
    symbol: tuple = repr_piece.ROOK.value
    # sliding piece
    direction: set = piece_moves.ROOK
    applied_rules = rules.get_sliding_moves

class Queen(Piece):
    symbol: tuple = repr_piece.QUEEN.value
    # sliding piece
    direction: set = piece_moves.QUEEN
    applied_rules = rules.get_sliding_moves

class King(Piece):
    symbol: tuple = repr_piece.KING.value
    # knight/king piece
    direction: set = piece_moves.KING
    applied_rules = rules.get_knight_king_moves

class Knight(Piece):
    symbol: tuple = repr_piece.KNIGHT.value
    # knight/king piece
    direction: set = piece_moves.KNIGHT
    applied_rules = rules.get_knight_king_moves

class Pawn(Piece):
    symbol: tuple = repr_piece.PAWN.value
    start_square: bool = False
    # direction: set = piece_moves.PAWN
    # direction = rules.PAWN if (self.color == colors.BLACK) else rules.PAWN.inverse
    # pawn piece
    applied_rules = rules.get_pawn_moves

    def __init__(self, x: int, y: int, color: colors):
        super().__init__(x, y, color)
        if ((y == 6 and color == colors.BLACK) 
            or 
            (y == 1 and color == colors.WHITE)): 
                self.start_square = True
        else: 
            self.start_square = False

if __name__ == "__main__":
    pass