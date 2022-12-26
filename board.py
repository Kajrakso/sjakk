from CONST import SIZE, FEN_START, colors
import pieces

def create_piece(x: int, y: int, char: str) -> object:
    if char == char.upper(): c = colors.WHITE
    else: c = colors.BLACK
    match char.lower():
        case 'p': return pieces.Pawn(x, y, color=c)
        case 'k': return pieces.King(x, y, color=c)
        case 'q': return pieces.Queen(x, y, color=c)
        case 'r': return pieces.Rook(x, y, color=c)
        case 'n': return pieces.Knight(x, y, color=c)
        case 'b': return pieces.Bishop(x, y, color=c)
    
def readFEN(board: list, pos_info: dict, FEN: str) -> None:
    """Reads FEN and updates the chess dictionary keys board and pos_info"""        
    FEN_board, FEN_info = FEN.split(' ', 1)[0], FEN.split(' ')[1:] 
    i = 0
    for char in FEN_board:
        if char.isalpha():
            x, y = i % SIZE, SIZE - i // SIZE - 1
            board[x][y] = create_piece(x, y, char) 
            i += 1
        else:
            try: i += int(char)
            except: pass

    for j, info in enumerate(FEN_info):
        match j:
            case 0: pos_info["move"] = (colors.BLACK if info == 'b' else colors.WHITE)
            case 1: pos_info["castle"] = info
            case 2: pos_info["en_passant"] = info
            case 3: pos_info["halfmove"] = int(info)
            case 4: pos_info["fullmove"] = int(info)

class Board():
    board: list[list] = [[None for _ in range(SIZE)] for _ in range(SIZE)] 
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

    def get_legal_moves(self, x: int, y: int):
        piece = self.board[x][y]
        return piece.moves()

    def update_pos_info(self):
        """Updates position info"""
        if self.pos_info['move'] == colors.WHITE: self.pos_info['move'] = colors.BLACK
        elif self.pos_info['move'] == colors.BLACK: self.pos_info['move'] = colors.WHITE
        self.pos_info['halfmove'] += 1
        if self.pos_info['halfmove'] % 2 == 0:
            self.pos_info['fullmove'] += 1
        #! Also needs to update en passant
        #! Also need to update castle 
    
    def update_pos(self):
        for i in range(SIZE):
            for j in range(SIZE):
                if self.board[i][j] != None:
                    x_new = self.board[i][j].x
                    y_new = self.board[i][j].y
                    self.board[i][j], self.board[x_new][y_new] = None, self.board[i][j]

if __name__ == "__main__":
    pass