import board
import UI
import main

andre = [(i, 1) for i in range(8)]
syvende = [(i, 6) for i in range(8)]


def test1():
    testbrett = main.Board()
    UI.display(testbrett.board)
    for (x, y) in andre+syvende:
        # print(x, y)
        moves = testbrett.board[x][y].applied_rules(testbrett.board)
        print(f'Brikke på ({x}, {y})   -    trekk/slag: {moves}')
        assert len(moves[0]) == 2, "ikke to trekk" 
        

if __name__ == "__main__":
    # print(andre+syvende)
    test1()