def ReplaceDiagonal(mat):
    for i in range(len(mat)):
        if i==0:
            mat[i][i]=mat[i][i+1]+mat[i+1][i]+mat[i+1][i+1]
        elif i==len(mat)-1:
            mat[i][i]=mat[i][i-1]+mat[i-1][i-1]+mat[i-1][i]
        else:
            mat[i][i]=mat[i-1][i-1]+mat[i-1][i]+mat[i-1][i+1]+mat[i][i-1]+mat[i][i+1]+mat[i+1][i-1]+mat[i+1][i]+mat[i+1][i+1]
    print(mat)
mat=[[12,20],[10,22]]
ReplaceDiagonal(mat)