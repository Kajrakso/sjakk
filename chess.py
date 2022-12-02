import CONST
import chessrules
import numpy as np

def color(piece) -> str:
    if ord(piece) in range(65, 91):
        return 'white'
    else:
        return 'black'