SIZE = 8

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

def transform(pos: str) -> tuple:
    """Transforms a chess square string to its corresponding tuple.
    For example: From "e4" to (4, 4).
    """
    x = ord(list(pos.lower())[0]) - 97
    y = abs(int(list(pos)[1]) - SIZE)
    return (y, x)

def display(board: list, pos_info: dict, game_info: dict) -> None:
    """Prints out a board with coordinate axes.
    Also prints out information about the position."""
    SPACING = 1
    moveInfo: bool = True
    board_string = "\n"

    for i in range(SIZE):
        for _ in range(SPACING):
            board_string += '\n'
        board_string += str(abs(i-SIZE)) + " "*SPACING + "|" + " "*SPACING
        for j in range(SIZE):
            # board_string += (CONST.chessPieces[self.board[i][j]] if unicode else self.board[i][j]) + " "*spacing
            board_string += board[i][j] + " "*SPACING
    board_string += '\n' + "――"*(SPACING+1) + "―"*SIZE*(SPACING+1) + '\n'
    ### a b c d e f g h
    board_string += " "*(SPACING+1) + "|" + " "*SPACING
    for k in (range(SIZE)):
        board_string += chr(97+k) + " "*SPACING
    board_string += '\n'
    if moveInfo:
        board_string += f'\nMove {pos_info["fullmove"]}'
        board_string += f'\nIt\'s {pos_info["move"]}\'s move\n'
    print(board_string)