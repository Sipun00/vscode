# def ReplaceDiagonal(mat):
    # for i in range(len(mat)):
        # if i==0:
            # mat[i][i]=mat[i][i+1]+mat[i+1][i]+mat[i+1][i+1]
        # elif i==len(mat)-1:
            # mat[i][i]=mat[i][i-1]+mat[i-1][i-1]+mat[i-1][i]
        # else:
            # mat[i][i]=mat[i-1][i-1]+mat[i-1][i]+mat[i-1][i+1]+mat[i][i-1]+mat[i][i+1]+mat[i+1][i-1]+mat[i+1][i]+mat[i+1][i+1]
    # print(mat)
# mat=[[12,20],[10,22]]
# ReplaceDiagonal(mat)
# a=input()
# A=a.split()
# c=0
# for i in A:
    # if "a" in i:
        # c+=1
# print(c)

# a=input()
# x=a.replace("the","of")
# print(x)
# a=int(input())
# b=input()
# A=list(b.split())
# sum=0
# def prime(n):
    # for i in range(n):
        # if n%i==0:
            # return False
    # return True
# for i in A:
    # if prime(i):
        # sum+=i
# print(sum)
a=int(input())
b=input()
A=list(map(int,b.split()))
sum=0
for i in A:
    if i%2==0:
        sum+=i
print(sum)


