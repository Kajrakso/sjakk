from CONST import colors
import pieces

# def get_possible_castling(self, board, )

def legal_moves(board: list, x: int, y: int):
    piece= board[x][y]
    match piece.__class__:
        case pieces.Knight: return get_knight_king_moves(board, x, y)
        case pieces.Bishop: return get_sliding_moves(board, x, y)
        case pieces.King: return get_knight_king_moves(board, x, y)
        case pieces.Queen: return get_sliding_moves(board, x, y)
        case pieces.Pawn: return get_pawn_moves(board, x, y)
        case pieces.Rook: return get_sliding_moves(board, x, y)
        case _: return ([], [])

def get_knight_king_moves(board: list, x: int, y: int) -> tuple:
    #! CASTLING missing. New function maybe?
    """Checks every move specified in CONST.py for knight and king.
    Returns a tuple of lists containing possible moves and captures.
    """
    piece = board[x][y]
    moves: list[tuple] = []
    captures: list[tuple] = []
    for (i, j) in piece.direction:
        if inside_board(x+i, y+j):
            if board[x+i][y+j] == None:
                moves.append((x+i, y+j))
                continue
            if (board[x+i][y+j].color != piece.color):
                captures.append((x+i, y+j))
    return moves, captures        

def get_sliding_moves(board: list, x: int, y: int) -> tuple:
    """Cheks for sliding moves. Diagonal or/and vertical/horizontal.
    Returns a tuple of lists containing possible moves and captures.
    """
    piece = board[x][y]
    moves: list[tuple] = []
    captures: list[tuple] = []
    for (dir_x, dir_y) in piece.direction:    
        i = j = 0
        while inside_board(x+i, y+j):
            if board[x+i][y+j] == piece:
                i += dir_x
                j += dir_y
                continue
            if board[x+i][y+j] == None:
                moves.append((x+i, y+j))
                i += dir_x
                j += dir_y
                continue
            if (board[x+i][y+j].color != piece.color):
                captures.append((x+i, y+j)) 
            break        
    return moves, captures

def get_pawn_moves(board: list, x: int, y: int) -> tuple:
    #! En passant missing
    """Checks the moves for pawn. Not implemented en passant yet.
    Returns a tuple of lists containing possible moves and captures.
    """
    piece: pieces.Pawn = board[x][y]
    moves: list[tuple] = []
    captures: list[tuple] = []
    direction = 1 if (piece.color == colors.WHITE) else -1
    
    if ((y == 6 and piece.color == colors.BLACK) 
        or 
        (y == 1 and piece.color == colors.WHITE)): 
            piece.start_square = True
            piece.moves.add((0,2))
    else: 
        piece.start_square = False

    for (i, j) in piece.moves:
        j *= direction
        if inside_board(x+i, y+j):
            if board[x+i][y+j] == None:
                moves.append((x+i, y+j))
            else:
                break

    for (i, j) in piece.captures:
        j *= direction
        if inside_board(x+i, y+j):
            if board[x+i][y+j] == None:
                continue
            if (board[x+i][y+j].color != piece.color):
                captures.append((x+i, y+j))    
    return moves, captures

def inside_board(x_index: int, y_index: int):
    return True if ((x_index in range(0,8)) and (y_index in range(0,8))) else False

# def king_in_check(self, board: list) -> bool:
#     # king_pos: tuple = (board.white_king_pos if color == colors.WHITE else board.black_king_pos)
#     # piece = board.board[king_pos[0]][king_pos[1]]
#     # late som om kongen er enhver brikke.
#     return 