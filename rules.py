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
            break   
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
    return moves, captures
    
def inside_board(x_index: int, y_index: int):
    return True if ((x_index in range(0,8)) and (y_index in range(0,8))) else False

def remove_squares_not_in_board(moves: list[tuple]) -> None:
    moves = list(filter(
        lambda move: 
            (move[0] in range(0,8)) and (move[1] in range(0,8))
        , moves))

# def moves(self) -> list[tuple]:
#     #! COMPLICTED PIECE
#     #! NEEDS MORE WORK
#     scope = []
#     if self.color == colors.WHITE:
#         scope = [(self.x    , self.y - 1), 
#                     (self.x - 1, self.y - 1),
#                     (self.x + 1, self.y - 1)]
#         if self.start_square:
#             scope.append((self.x, self.y - 2))
#     elif self.color == colors.BLACK:
#         scope = [(self.x    , self.y + 1), 
#                     (self.x - 1, self.y + 1),
#                     (self.x + 1, self.y + 1)]
#         if self.start_square:
#             scope.append((self.x, self.y + 2))
    
#     remove_squares_not_in_board(scope)
#     return scope