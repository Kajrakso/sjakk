from board import Board
import rules
import UI

def move(board, x_from, y_from, x_to, y_to):
    #! Må gjøre noe med denne oppdateringsgreia.
    board.move_piece(x_from, y_from, x_to, y_to)
    board.update_pos_info()

def main():
    chess_game: Board = Board()
    board: list = chess_game.board
    while True:
        UI.display(chess_game)
        try:
            (x_from, y_from), (x_to, y_to) = UI.get_user_move()
            moving_piece = chess_game.board[x_from][y_from]
            
            possible_moves, possible_captures = rules.legal_moves(board, x_from, y_from)

            if not (chess_game.pos_info['move'] == moving_piece.color):
                raise MovingWrongPiece

            if (((x_to, y_to) in possible_moves)
                or 
                ((x_to, y_to) in possible_captures)):
                move(chess_game, x_from, y_from, x_to, y_to)
            else:
                raise IllegalMove
        
        except ValueError: UI.error_msg(f"\nHar du skrevet noe feil?\n{ValueError}\n")
        except IndexError: UI.error_msg(f"\nPrøver du å flytte ut av brettet?\n{IndexError}\n")
        except AttributeError: UI.error_msg(f"\nPrøver du å flytte på et tomt felt?\n{AttributeError}\n")
        except MovingWrongPiece: UI.error_msg(f"\nPrøver du å flytte motstanderens brikke?\n{MovingWrongPiece}\n")
        except IllegalMove: UI.error_msg(f"\nHar du lov til å flytte dit?\n{IllegalMove}\n")

class MovingWrongPiece(Exception): pass
class IllegalMove(Exception): pass

if __name__ == "__main__":
    main()