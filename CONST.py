import numpy as np
"""
CONSTANTS
"""
CHESS_SIZE = 8
CHESS_PIECES = 32

FEN_START = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 0"

knight = {
    "moves": np.array([
        [-2, -1],
        [-2,  1],
        [-1, -2],
        [-1,  2],
        [ 1, -2],
        [ 1,  2],
        [ 2, -1],
        [ 2,  1],
        ])
}

king = {
    "moves": np.array([
        [-1, -1],
        [-1,  0],
        [-1,  1],
        [ 0, -1],
        [ 0,  1],
        [ 1, -1],
        [ 1,  0],
        [ 1,  1],
    ])
}

chessPieces = {
    'r': '♖',
    'R': '♜',
    'b': '♗',
    'B': '♝',
    'n': '♘',
    'N': '♞',
    'q': '♕',
    'Q': '♛',
    'k': '♔',
    'K': '♚',
    'p': '♙',
    'P': '♟',
    ' ': ' '
}

text_not_legal = "Not a legal move! Try again."
STRING_NOT_LEGAL = f"""
{'#'*len(text_not_legal)}
{text_not_legal} 
{'#'*len(text_not_legal)}
"""
text_please_move_piece = "Please move your piece!"
STRING_PLEASE_MOVE_PIECE = f"""
{'#'*len(text_please_move_piece)}
{text_please_move_piece} 
{'#'*len(text_please_move_piece)}
"""