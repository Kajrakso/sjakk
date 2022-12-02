from dataclasses import dataclass
from enum import Enum

class pieceType(Enum):
    PAWN = "pawn"
    KNIGHT = "knight"
    BISHOP = "bishop"
    ROOK = "rook"
    QUEEN = "queen"
    KING = "king"
    NONE = "none"

class color(Enum):
    WHITE = 1
    BLACK = 0
    NONE = -1

PIECE_STR: dict = {
    pieceType.PAWN: ('♟', '♙'),
    pieceType.KNIGHT: ('♞', '♘'),
    pieceType.BISHOP: ('♝', '♗'),
    pieceType.ROOK: ('♜', '♖'),
    pieceType.QUEEN: ('♛', '♕'),
    pieceType.KING: ('♚', '♔'),
    pieceType.NONE: (' ', ' ')
}

PIECE_MAP: dict = {
    'r': pieceType.ROOK,
    'p': pieceType.PAWN,
    'n': pieceType.KNIGHT,
    'b': pieceType.BISHOP,
    'k': pieceType.KING,
    'q': pieceType.QUEEN,
    ' ': pieceType.NONE
}

@dataclass
class Piece():
    x: int
    y: int
    piecetype: str
    color: str