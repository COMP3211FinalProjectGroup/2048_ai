import numpy as np

def sideHeuristics(board, a1=10, a2=5, a3=1):
    score = 0
    for x in range(board.size()):
        for y in range(board.size()):
            if x==0 or x==3 or y==0 or y==3:
                if (x==0 or x==3) and (y==0 or y==3):
                    score += a1 * board.getCell(x, y)
                else:
                    score += a2 * board.getCell(x, y)
            else:
                    score += a3 * board.getCell(x, y)

    return score

def emptyHeuristics(board):

    return len(board.getEmptyCells())


def patternHeuristics(board):

    cells = np.array(board.cells)

    W = np.array([[0,0,1,3],
                  [0,1,3,5],
                  [1,3,5,10],
                  [3,5,10,15]])

    # W = np.array([[3,4,11,12],
    #               [2,5,10,13],
    #               [1,6,9,14],
    #               [0,7,8,15]])

    return np.sum(W*cells) #/ 16

    

def clusterHeuristics(board):

    cells = np.array(board.cells)

    size = board.size()

    penalty = np.sum(np.abs(cells[:size-1,:] - cells[1:size,:]))

    penalty += np.sum(np.abs(cells[:,:size-1] - cells[:,1:size]))

    return penalty / 16