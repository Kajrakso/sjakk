from board import Board
import UI

def main():
    game = Board()
    while True:
        UI.display(game.board, game.pos_info, game.game_info)
        move = UI.get_user_move()
        if UI.user_quit(move[0], move[1]):
            break
        game.make_move(move[0], move[1])

if __name__ == "__main__":
    main()