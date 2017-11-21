from . import greedyMove
import copy
import random


def next_move(board, n=3):
    m, _ = predict_move(board, n)
    return m

def predict_move(board, n):
    h_score = -100000000
    h_move = 0

    if n==1:
        return greedyMove.predict_next(board)

    for i in range(1,5):
        newBoard = copy.deepcopy(board)
        score = newBoard.move(i)
        if board.cells == newBoard.cells :
            continue
        
        tmove, tscore = predict_move(newBoard, n-1)

        score += tscore

        if score > h_score:
            h_score = score
            h_move = i

    if h_move==0:
        h_move = random.randint(1,4)

    return h_move, h_score
