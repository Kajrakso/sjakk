import numpy as np
import CONST

def getLegalMoves(pos: tuple, piece: str, pieceColor: str, board, boardinfo: dict) -> list[tuple]:
    legals = []
    match piece:
        case 'p':
            legals = pawn(pos, pieceColor, board)
        case 'P':
            legals = pawn(pos, pieceColor, board)
        case _:
            pass
    return legals

def pawn(pos: tuple, color: str, board) -> list:
    legals = []
    if color == "white": direction = -1
    else: direction = 1
    possible_moves = [
        (pos[0], pos[1]+direction),
        (pos[0], pos[1]+direction*2)
    ]
    possible_captures = [
        (pos[0]-1, pos[1]+direction), 
        (pos[0]+1, pos[1]+direction)
    ]
    # BAD CHECK
    for move in possible_moves:
        if move[0] not in range(8) or move[1] not in range(8):
            possible_moves.remove(move)
    for move in possible_captures:
        if move[0] not in range(8) or move[1] not in range(8):
            possible_moves.remove(move)
    if board[possible_moves[0][0]][possible_moves[0][1]] == ' ':
        legals.append(possible_moves[0])
        if pos[1] == 1 or pos[1] == 6:
            legals.append(possible_moves[1])
    return legals

def knight():
    pass