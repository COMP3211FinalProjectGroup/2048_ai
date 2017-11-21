import copy
import random

from . import heuristics

def next_move(b):
    m, _ = predict_next(b)
    return m


def predict_next(b):
    h_score = -100000000
    h_move = 0

    for i in range(1,5):

        board = copy.deepcopy(b)
        score = board.move(i)

        if board.cells == b.cells :
            continue

        # score += 1 * heuristics.sideHeuristics(board) - heuristics.clusterHeuristics(board)
        # score += - heuristics.clusterHeuristics(board)
        # score +=  heuristics.patternHeuristics(board)
        # score +=  heuristics.patternHeuristics(board) - heuristics.clusterHeuristics(board)

        if not board.canMove():
            score = -1

        if score > h_score:
            h_score = score
            h_move = i
        
    if h_move==0:
        h_move = random.randint(1,4)

    return (h_move, h_score)