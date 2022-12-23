from enum import Enum

SIZE = 8
FEN_START: str = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 0"

class colors(Enum):
    WHITE = 0
    BLACK = 1
    # NONE = -1

class pieces(Enum):
    PAWN = ("P", "p")
    ROOK = ("R", "r")
    KNIGHT = ("N", "n")
    BISHOP = ("B", "b")
    QUEEN = ("Q", "q")
    KING = ("K", "k")
    NONE = (None, None)

if __name__ == "__main__":
    print(pieces.PAWN.value[colors.WHITE.value])
    print(pieces.PAWN.value[colors.BLACK.value])