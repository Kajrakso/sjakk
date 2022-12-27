from enum import Enum

SIZE = 8
FEN_START: str = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 0"

class colors(Enum):
    WHITE = 0
    BLACK = 1
    # NONE = -1

class repr_piece(Enum):
    PAWN = ("P", "p")
    ROOK = ("R", "r")
    KNIGHT = ("N", "n")
    BISHOP = ("B", "b")
    QUEEN = ("Q", "q")
    KING = ("K", "k")
    NONE = (None, None)

class move_dir:
    SLIDING = set([(-1, 0), (1, 0), (0, -1), (0, 1)])
    DIAG  = set([(1,1), (-1,1), (-1,-1), (1,-1)])
    ALL = SLIDING.union(DIAG)

class piece_moves:
    ROOK = move_dir.SLIDING
    BISHOP = move_dir.DIAG
    QUEEN = move_dir.ALL
    
    # SPECIAL MOVES
    KING = move_dir.ALL
    KNIGHT = {(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)}
    PAWN = {'moves': {(0,1)}, 
            'captures': {(-1, 1), (1, 1)}}

if __name__ == "__main__":
    pass