import UI
from enum import Enum

SIZE = 8

class color(Enum):
    WHITE = 1
    BLACK = 0
    NONE = -1

def readFEN(board: list, pos_info: dict, FEN: str) -> None:
    """Reads FEN and updates the chess dictionary keys board and pos_info"""
    FEN_board, FEN_info = FEN.split(' ', 1)[0], FEN.split(' ')[1:] 
    i = 0
    for char in FEN_board:
        if char.isalpha():
            board[i//8][i%8] = char
            i += 1
        else:
            try: i += int(char)
            except: pass
    for j, info in enumerate(FEN_info):
        match j:
            case 0: pos_info["move"] = (color.BLACK if info == 'b' else color.WHITE)
            case 1: pos_info["castle"] = info
            case 2: pos_info["en_passant"] = info
            case 3: pos_info["halfmove"] = int(info)
            case 4: pos_info["fullmove"] = int(info)

class Chess():
    FEN_START: str = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 0"
    board: list = [[' ' for _ in range(SIZE)] for _ in range(SIZE)] 
    pos_info: dict = {
        "move": color.NONE,
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

    def make_move(self, pos_from: tuple, pos_to: tuple) -> None:
        """Moves pieces and updates position info"""
        
        # Moves piece
        piece = self.board[pos_from[0]][pos_from[1]]
        self.board[pos_from[0]][pos_from[1]] = ' '
        self.board[pos_to[0]][pos_to[1]] = piece

        # Updates position info
        if self.pos_info['move'] == color.WHITE: self.pos_info['move'] = color.BLACK
        elif self.pos_info['move'] == color.BLACK: self.pos_info['move'] = color.WHITE
        self.pos_info['halfmove'] += 1
        if self.pos_info['halfmove'] % 2 == 0:
            self.pos_info['fullmove'] += 1
        #! Also needs to add en passant functionality

if __name__ == "__main__":
    test = Chess()
    test.make_move((1,1), (4,1))
    UI.display(test.board, test.pos_info, test.game_info)