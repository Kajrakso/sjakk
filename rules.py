from CONST import colors

def get_knight_king_moves(self, board: list):
    moves: list[tuple] = []
    captures: list[tuple] = []
    for (i, j) in self.direction:
        if inside_board(self.x+i, self.y+j):
            if board[self.x+i][self.y+j] == None:
                moves.append((self.x+i, self.y+j))
                continue
            if (board[self.x+i][self.y+j].color != self.color):
                captures.append((self.x+i, self.y+j))    
    return moves, captures        

def get_sliding_moves(self, board: list):
    moves: list[tuple] = []
    captures: list[tuple] = []
    for (dir_x, dir_y) in self.direction:    
        i = j = 0
        while inside_board(self.x+i, self.y+j):
            if board[self.x+i][self.y+j] == self:
                i += dir_x
                j += dir_y
                continue
            if board[self.x+i][self.y+j] == None:
                moves.append((self.x+i, self.y+j))
                i += dir_x
                j += dir_y
                continue
            if (board[self.x+i][self.y+j].color != self.color):
                captures.append((self.x+i, self.y+j)) 
            break        
    return moves, captures

def get_pawn_moves(self, board: list):
    moves: list[tuple] = []
    captures: list[tuple] = []
    direction = 1 if (self.color == colors.WHITE) else -1
    
    if ((self.y == 6 and self.color == colors.BLACK) 
        or 
        (self.y == 1 and self.color == colors.WHITE)): 
            self.start_square = True
            self.moves.add((0,2))
    else: 
        self.start_square = False

    for (i, j) in self.moves:
        j *= direction
        if inside_board(self.x+i, self.y+j):
            if board[self.x+i][self.y+j] == None:
                moves.append((self.x+i, self.y+j))
            else:
                break

    for (i, j) in self.captures:
        j *= direction
        if inside_board(self.x+i, self.y+j):
            if board[self.x+i][self.y+j] == None:
                continue
            if (board[self.x+i][self.y+j].color != self.color):
                captures.append((self.x+i, self.y+j))    
    return moves, captures

def inside_board(x_index: int, y_index: int):
    return True if ((x_index in range(0,8)) and (y_index in range(0,8))) else False

def in_check(board, color: colors):
    king_pos: tuple = (board.white_king_pos if color == colors.WHITE else board.black_king_pos)
    piece = board.board[king_pos[0]][king_pos[1]]
    # late som om kongen er enhver brikke.
    pass