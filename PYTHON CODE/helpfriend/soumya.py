# c=input()
# V=list(map(int,c.split()))
# N=V[0]
# 
# K=V[1]
# b=input()
# A=list(map(int,b.split()))
# A=set(A)
# c=0
# for i in A:
    # if i-2 in A or i+2 in A :
        # c+=1
    # elif i-2>= min(A) and i+2<=max(A) :
        # for j in range (i-2,i+3):
            # if j in A:
                # c+=1
                # break
# print(c)
# 
# 



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





# def sum(cls,input1,input2):
    # l=max(cls.input2)+min(cls.input2)
    # return l
    # pass
# 
# 
# def lis(cls,input1,input2):
# 
    # k=[1]*cls.input1
    # for i in range(1,cls.input1):
        # 
        # for j in range(0,i):
            # if cls.input2[i]>cls.input2[j] and k[i]<k[j]+1:
                # k[i]=k[j]+1
# 
    # 
# 
# 
    # maxi=0
    # for i in range(cls.input1):
        # maxi=max(maxi,k[i])
    # return maxi
    # pass
# 
# 
# input1=5
# input2=[41,18467,6334,26500,19169]
# print(lis(input1,input2))
    # 
# 
# 
# 
# 
# 
# s=input()
# A=list(s.split(" "))
# B=['*','%','!','@','(',")"]
# count=0
# for i in A:
    # if i[-1] in B:
        # count+=1
# print (count)
# 
# 
# 
# 
# 
# 
# 
# 
# 

# n=int(input())
# sampleInput=input()
# A=list(sampleInput.split(" "))
# even=1
# odd=1
# for i in A:
    # if int(i) %2==0:
        # even*=int(i)
    # else:
        # odd*=int(i)
# result=abs(even-odd)
# print(result)

# n=int(input())
# sampleInput=input()
# result=-404
# A=list(sampleInput.split(" "))
# summ=0
# c=0
# for i in range(n):
    # if i%2==0:
        # c+=1
        # summ+=int(A[i])
# 
# result=summ//c
# print(result)

n=int(input())
s=int(input())
sampleInput=input()
result=-404
A=list(sampleInput.split(" "))

for i in A:
    if len(i)==s:
        print (i)







