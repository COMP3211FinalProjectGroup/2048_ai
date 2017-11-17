import copy
import random

from . import heuristics

def next_move(b):
    m, _ = predict_next(b)
    return m


def predict_next(b):
    h_score = 0
    h_move = 0

    for i in range(1,5):

        board = copy.deepcopy(b)
        score = board.move(i)
        # if score != 0:
        #     score += 0.01 * heuristics.sideHeuristics(board) + 0.01 * heuristics.emptyHeuristics(board)

        if score > h_score:
            h_score = score
            h_move = i
        
    if h_move==0:
        h_move = random.randint(1,4)

    return (h_move, h_score)