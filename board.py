from CONST import SIZE, FEN_START, colors
import pieces

def create_piece(char: str) -> object:
    if char == char.upper(): c = colors.WHITE
    else: c = colors.BLACK
    match char.lower():
        case 'p': return pieces.Pawn(color=c)
        case 'k': return pieces.King(color=c)
        case 'q': return pieces.Queen(color=c)
        case 'r': return pieces.Rook(color=c)
        case 'n': return pieces.Knight(color=c)
        case 'b': return pieces.Bishop(color=c)
    
def readFEN(board: list, pos_info: dict, FEN: str) -> None:
    """Reads FEN and updates the chess dictionary keys board and pos_info"""        
    FEN_board, FEN_info = FEN.split(' ', 1)[0], FEN.split(' ')[1:] 
    
    # Creates Piece objects on the board 
    i = 0
    for char in FEN_board:
        if char.isalpha():
            x, y = i % SIZE, SIZE - i // SIZE - 1
            board[x][y] = create_piece(char) 
            i += 1
        else:
            try: i += int(char)
            except: pass

    # Info about the position
    for j, info in enumerate(FEN_info):
        match j:
            case 0: pos_info["move"] = (colors.BLACK if info == 'b' else colors.WHITE)
            case 1: pos_info["castle"] = info
            case 2: pos_info["en_passant"] = info
            case 3: pos_info["halfmove"] = int(info)
            case 4: pos_info["fullmove"] = int(info)

class Board():
    board: list[list] = [[None for _ in range(SIZE)] for _ in range(SIZE)] 
    white_king_pos: tuple
    black_king_pos: tuple
    pos_info: dict = {
        "move": colors.WHITE,
        "castle": "",
        "en_passant": "", 
        "halfmove": 0,
        "fullmove": 0
        }
    game_info: dict = {
        'players': ['Carlsen, Magnus', 'Jakobsen, Oskar Feed'],
        'date': 'ddmmyyyy'        
        }

    def __init__(self, pos=FEN_START):
        readFEN(self.board, self.pos_info, pos)
        all_pos = [(i, j) for i in range(SIZE) for j in range(SIZE)]
        for (x, y) in all_pos:
            if self.board[x][y].__class__ == pieces.King:
                match self.board[x][y].color:
                    case colors.WHITE:
                        self.white_king_pos = (x, y)
                    case colors.BLACK:
                        self.black_king_pos = (x, y)

    def update_pos_info(self):
        """Updates position info"""
        if self.pos_info['move'] == colors.WHITE: self.pos_info['move'] = colors.BLACK
        elif self.pos_info['move'] == colors.BLACK: self.pos_info['move'] = colors.WHITE
        self.pos_info['halfmove'] += 1
        if self.pos_info['halfmove'] % 2 == 0:
            self.pos_info['fullmove'] += 1
        #! Also needs to update en passant
        #! Also need to update castle 
    
    def move_piece(self, x: int, y: int, x_new: int, y_new: int):
        """Moves piece object."""
        self.board[x][y], self.board[x_new][y_new] = None, self.board[x][y]
        if self.board[x_new][y_new].__class__ == pieces.King:
            match self.board[x_new][y_new].color:
                case colors.WHITE:
                    self.white_king_pos = (x_new, y_new)
                case colors.BLACK:
                    self.black_king_pos = (x_new, y_new)

    def update_pos(self):
        self.update_pos_info()
        # Loops through all pieces and updates its position on the board. 
        all_pos = [(i, j) for i in range(SIZE) for j in range(SIZE)]
        for (x, y) in all_pos:
            if self.board[x][y] != None:
                x_new = self.board[x][y].x
                y_new = self.board[x][y].y
                self.board[x][y], self.board[x_new][y_new] = None, self.board[x][y]
                if self.board[x_new][y_new].__class__ == pieces.King:
                    match self.board[x_new][y_new].color:
                        case colors.WHITE:
                            self.white_king_pos = (x_new, y_new)
                        case colors.BLACK:
                            self.black_king_pos = (x_new, y_new)

if __name__ == "__main__":
    pass