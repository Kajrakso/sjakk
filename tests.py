import board
import UI
import main
import CONST

all_pos = [[(i, j) for i in range(CONST.SIZE)] for j in range(CONST.SIZE)]

def gyldig():
    pass

def test1():
    testbrett = main.Board()
    UI.display(testbrett.board)
    for (x, y) in andre+syvende:
        # print(x, y)
        moves = testbrett.board[x][y].applied_rules(testbrett.board)
        print(f'Brikke på ({x}, {y})   -    trekk/slag: {moves}')
        assert len(moves[0]) == 2, "ikke to trekk" 
        

if __name__ == "__main__":
    print(all_pos)