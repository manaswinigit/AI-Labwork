print("Enter number of queens:")
N=int(input())
board=[[0]*N for _ in range(N)]

def attack(i,j):
    for k in range(0,N):
        if board[i][k]==1 or board[k][j]==1:
            return True
    for k in range(0,N):
        for m in range(0,N):
            if (k+m==i+j) or (k-m==i-j):
                if board[k][m]==1:
                    return True
    return False
def NQueens(n):
    if n==0:
        return True
    for i in range(0,N):
        for j in range(0,N):
            if  (not(attack(i,j))) and (board[i][j]!=1):
                board[i][j]=1
                if NQueens(n-1)==True:
                    return True
                board[i][j]=0 
    return False
NQueens(N)
for i in board:
    print(i)
