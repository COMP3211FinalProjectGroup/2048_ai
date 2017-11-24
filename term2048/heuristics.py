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
                  [1,3,5,15],
                  [3,5,15,30]])

    # W = np.array([[0,1,2,3],
    #               [1,2,3,4],
    #               [2,3,4,5],
    #               [3,4,5,6]])

    # W = np.array([[3,4,11,12],
    #               [2,5,10,13],
    #               [1,6,9,14],
    #               [0,7,8,15]])

    # W = np.array([[0,4,8,12],
    #               [1,5,9,13],
    #               [2,6,10,14],
    #               [3,7,11,15]])
                  

    return np.sum(W*cells) #/ 16

    

def clusterHeuristics(board):

    cells = np.array(board.cells)

    size = board.size()
    penalty = 0

    # penalty = np.sum(np.abs(cells[:size-1,:] - cells[1:size,:]))

    # penalty += np.sum(np.abs(cells[:,:size-1] - cells[:,1:size]))

    penalty += np.sum(np.abs(cells[:size-2,:] - cells[1:size-1,:]))
    penalty += np.sum(np.abs(cells[2:size,:] - cells[1:size-1,:]))
    penalty += np.sum(np.abs(cells[:,:size-2] - cells[:,1:size-1]))
    penalty += np.sum(np.abs(cells[:,2:size] - cells[:,1:size-1]))

    # for i in range(size):
    #     for j in range(size):
    #         for h in [1,-1]:
    #             for k in [1,-1]:
    #                 if i+h>=size or i+h<0 or j+k>=size or j+k<0:
    #                     continue
    #                 penalty = np.abs(cells[i+h][j+k] - cells[i][j]) 

    return penalty / 32
 

def monotonicHeuristics(board):

    cells = np.array(board.cells)

    size = board.size()
    cells[cells<1] = 0.1


    # score = cells[1:size,3]/cells[:size-1,3]
    score1 = cells[1:size,3]/cells[:size-1,3]
    score2 = cells[3,1:size]/cells[3,:size-1]

    score = np.sum(score1[score1==2])
    score+= np.sum(score2[score2==2])

    return score * 10



    
def monotonicHeuristics2(board):

    cells = np.array(board.cells)

    size = board.size()



    score1 = cells[1:size, 2:4] - cells[:size-1,2:4]
    score1[score1>0] = 1
    score1[score1<=0] = -1

    score2 = cells[2:4, 1:size] - cells[2:4, :size-1]
    score2[score2>0] = 1
    score2[score2<=0] = -1

    score = np.sum(score1) + np.sum(score2)

    return score 
