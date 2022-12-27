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

    def move_to(self, x: int, y: int) -> bool:
        """Moves pieces"""
        self.x = x
        self.y = y
        return True
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
    direction: int
    # pawn piece
    moves = piece_moves.PAWN['moves']
    captures = piece_moves.PAWN['captures']
    applied_rules = rules.get_pawn_moves

if __name__ == "__main__":
    pass