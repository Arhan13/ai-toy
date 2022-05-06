N = 8

def printSolution(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end = " ")
        print()

def isSafe(row, col, sC, bsC,rL, sCL, bsCL):
    if (sCL[sC[row][col]] or bsCL[bsC[row][col]] or rL[row]):
        return False
    return True

def solveNQueensUtil(board,col,sC,bsC,rL,sCL,bsCL):
    if(col >= N):
        return True
    for i in range(N):
        if(isSafe(i,col,sC,bsC,rL,sCL,bsCL)):
            board[i][col] = 1
            rL[i] = True
            sCL[sC[i][col]] = True
            bsCL[bsC[i][col]] = True
            if(solveNQueensUtil(board,col + 1,sC,bsC,rL,sCL,bsCL)):
                return True
            board[i][col] = 0
            rL[i] = False
            sCL[sC[i][col]] = False
            bsCL[bsC[i][col]] = False
    return False

def solveNQueens():
    board = [[0 for i in range(N)]for j in range(N)]
    sC = [[0 for i in range(N)]for j in range(N)]
    bsC = [[0 for i in range(N)]for j in range(N)]
    rL = [False] * N
    x = 2 * N - 1
    sCL = [False] * x
    bsCL = [False] * x
    for rr in range(N):
        for cc in range(N):
            sC[rr][cc] = rr + cc
            bsC[rr][cc] = rr - cc + 7
    if(solveNQueensUtil(board,0,sC,bsC,rL,sCL,bsCL) == False):
        print("Solution does not exist")
        return False
    printSolution(board)
    return True
    
solveNQueens()
