from CONST import colors, repr_piece, piece_moves
# import rules

class Piece:
    symbol: tuple
    def __init__(self, color: colors):
        self.color = color

    def __str__(self):
        """returns the symbol found in CONST.pieces"""
        return self.symbol[self.color.value]


class Bishop(Piece):
    symbol: tuple = repr_piece.BISHOP.value
    direction: set = piece_moves.BISHOP

class Rook(Piece):
    symbol: tuple = repr_piece.ROOK.value
    direction: set = piece_moves.ROOK

class Queen(Piece):
    symbol: tuple = repr_piece.QUEEN.value
    direction: set = piece_moves.QUEEN

class King(Piece):
    symbol: tuple = repr_piece.KING.value
    # knight/king piece
    direction: set = piece_moves.KING
    # applied_rules = rules.get_knight_king_moves
    # if king in check: 
    # pretend the king is every piece type and see if is can capture the piece of opposite color. 
    # if this is possible the king is in check.
    # This restricts the possible moves and captures such that the king no longer is in check.
    # If the list of possible moves/captures is empty and the king is in check: checkmate -> game over...
    check_directions: list =   [piece_moves.KING,
                                piece_moves.KNIGHT,
                                piece_moves.BISHOP, 
                                piece_moves.ROOK,
                                piece_moves.QUEEN,
                                piece_moves.PAWN]
    # in_check = rules.king_in_check

class Knight(Piece):
    symbol: tuple = repr_piece.KNIGHT.value
    # knight/king piece
    direction: set = piece_moves.KNIGHT

class Pawn(Piece):
    symbol: tuple = repr_piece.PAWN.value
    start_square: bool = False
    direction: int
    moves = piece_moves.PAWN['moves']
    captures = piece_moves.PAWN['captures']

if __name__ == "__main__":
    pass