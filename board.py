import CONST

CHESS_SIZE = 8
spacing = 2
unicode = True

class Board():
    def __init__(self, starting_position: str) -> None:
        self.board, self.pos_info = readFEN(starting_position)

    # def legalMoves(self, pieceMove: str, posFrom: tuple) -> list[tuple]:
    #     # pieceColor = color(pieceMove)
    #     moves = []
    #     for piece in CONST.chessPieces.keys():
    #         if pieceMove == piece:
    #             moves = chessrules.getLegalMoves(posFrom, pieceMove, pieceColor, self.board, self.pos_info)
    #     return moves
        
    def display(self, moveInfo: bool = True) -> None:
        board_string = "\n"
        for i in range(CHESS_SIZE):
            for _ in range(spacing):
                board_string += '\n'
            board_string += str(abs(i-CHESS_SIZE)) + " "*(spacing) + "|" + " "*(spacing)
            for j in range(CHESS_SIZE):
                board_string += (CONST.chessPieces[self.board[i][j]] if unicode else self.board[i][j]) + " "*spacing
        board_string += '\n' + "――"*(spacing+1) + "―"*CHESS_SIZE*(spacing+1) + '\n'
        ### a b c d e f g h
        board_string += " "*(spacing+1) + "|" + " "*(spacing)
        for k in (range(CHESS_SIZE)):
            board_string += chr(97+k) + " "*(spacing)
        board_string += '\n'
        if moveInfo:
            board_string += f'\nMove {self.pos_info["fullmove"]}'
            board_string += f'\nIt\'s {self.pos_info["move"]}\'s move\n'
        print(board_string)

    def makeMove(self, posFrom: tuple, posTo: tuple) -> None:
        """Moves pieces and updates self.pos_info"""
        piece = self.board[posFrom[0]][posFrom[1]]
        self.board[posFrom[0]][posFrom[1]] = ' '
        self.board[posTo[0]][posTo[1]] = piece
        if self.pos_info['move'] == 'white': self.pos_info['move'] = 'black'
        elif self.pos_info['move'] == 'black': self.pos_info['move'] = 'white'
        self.pos_info['halfmove'] += 1
        if self.pos_info['halfmove'] % 2 == 0:
            self.pos_info['fullmove'] += 1
        #TODO: Also needs to add en passant functionality

def readFEN(FEN: str) -> tuple[list, dict]:
    """Reads FEN string and returns board and pos_info"""
    FEN_board, FEN_info = FEN.split(' ', 1)[0], FEN.split(' ')[1:] 
    board = [list(' '*CHESS_SIZE) for _ in range(CHESS_SIZE)]
    pos_info: dict = {
            "move": '-',
            "castle": '-',
            "en_passant": '-',
            "halfmove": 0,
            "fullmove": 0 
        }
    i = 0
    for char in FEN_board:
        if char.isalpha():
            row = i // CHESS_SIZE
            col = i % CHESS_SIZE
            board[row][col] = char
            i += 1
        else:
            try: i += int(char)
            except: pass
    for i, info in enumerate(FEN_info):
        match i:
            case 0: pos_info["move"] = ("black" if info == 'b' else "white")
            case 1: pos_info["castle"] = info
            case 2: pos_info["en_passant"] = info
            case 3: pos_info["halfmove"] = int(info)
            case 4: pos_info["fullmove"] = int(info)
    return board, pos_info