from . import heuristics
import copy
import random

def next_move(board, n=3):
    h_score = -1
    h_move = 0
    if len(board.getEmptyCells())>4:
        n=4
    else:
        n=5

    for i in range(1,5):
        newBoard = copy.deepcopy(board)
        newBoard.move(i)
        if board.cells == newBoard.cells :
            continue
        score = expectimax(newBoard, n-1, False)
        if score > h_score:
            h_score = score
            h_move = i

    if h_move == 0:
        return random.randint(1,4)

    return h_move


def expectimax(board, n, maxPlayer):
    if n==0:
        if not board.canMove():
            return 0
        return heuristics.patternHeuristics(board) # - heuristics.clusterHeuristics(board)

    if maxPlayer:
        h_val = -1
        for i in range(1,5):
            newBoard = copy.deepcopy(board)
            score = newBoard.move(i)
            if board.cells == newBoard.cells :
                continue
            val = expectimax(newBoard, n-1, False)

            if val > h_val:
                h_val = val
        return h_val

    else:
        sum_val = 0
        num = 0
        for cell in board.getEmptyCells():
            newBoard = copy.deepcopy(board)
            x,y = cell
            newBoard.cells[x][y] = 2

            sum_val += expectimax(newBoard, n-1, True)
            num += 1

        if num == 0:
            newBoard = copy.deepcopy(board)
            return expectimax(newBoard, n-1, True)

        return sum_val / num
            

