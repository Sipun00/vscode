c=input()
V=list(map(int,c.split()))
N=V[0]

K=V[1]
b=input()
A=list(map(int,b.split()))
A=set(A)
c=0
for i in A:
    if i-2 in A or i+2 in A :
        c+=1
    elif i-2>= min(A) and i+2<=max(A) :
        for j in range (i-2,i+3):
            if j in A:
                c+=1
                break
print(c)





# 
# 
# t=int(input())
# for i in range(t):
    # 
# 
    # N=int(input())
    # K=int(input())
    # b=input()
    # A=list(map(int,b.split()))
    # c=0
    # for i in A:
        # if i<=K:
            # c+=1
    # print(c)
