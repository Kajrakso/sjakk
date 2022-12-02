import CONST
from board import Board

#! RUN CHESS GAME FUNCTION
def run():
    board = Board(starting_position = CONST.FEN_START)
    run = True
    while run:
        board.display()
        moveFrom, moveTo = get_user_move()
        try:
            piece = board.board[moveFrom[0]][moveFrom[1]]
        except:
            print("Something went wrong")       #! MÅ LAGE BEDRE EXCEPTION
            continue
        if user_quit(moveFrom, moveTo): 
            run = False
        elif piece == ' ' or board.pos_info['move'] != color(piece):
            print(CONST.STRING_PLEASE_MOVE_PIECE)
        # elif moveTo not in board.legalMoves(piece, moveFrom):
        #     print(CONST.STRING_NOT_LEGAL)
        #     continue
        else:
            board.makeMove(moveFrom, moveTo)
            # TODO: SKRIVE trekk til fil
            # TODO: SJEKKE matt evt. patt
            # TODO: AVSLUTTE spillet

def color(piece) -> str:        # TODO enums type drid
    if ord(piece) in range(65, 91):
        return 'white'
    else:
        return 'black'

#! IO
# * Transforms from e.g. "e4" to (4, 4) 
def transform(pos: str) -> tuple:
    x = ord(list(pos.lower())[0]) - 97
    y = abs(int(list(pos)[1]) - CONST.CHESS_SIZE)
    return (y, x)

def get_user_move() -> tuple:
    moveFrom, moveTo = input("Move piece from square: "), input("to square: ")
    if moveFrom == "q" or moveTo == "q":
        return ("q", "q")
    return (transform(moveFrom), (transform(moveTo)))

def user_quit(*user_input: str) -> bool:
    for string in user_input:
        if string == "q":
            return True
    return False