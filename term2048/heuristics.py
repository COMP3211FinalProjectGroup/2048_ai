

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