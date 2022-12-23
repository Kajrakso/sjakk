from board import Board
import UI

def main():
    board = Board()
    while True:
        UI.display(board.board)
        (x_from, y_from), (x_to, y_to) = UI.get_user_move()
        if (x_to, y_to) in board.get_legal_moves(x = x_from, y = y_from):
            board.board[y_from][x_from].move_to(x = x_to, y = y_to)
            board.update_pos()
        else:
            print("not legal move...")

if __name__ == "__main__":
    main()