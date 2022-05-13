# from unittest import result
# 
# 
# def isdiagnotic(s):
    # A=[]
    # for i in s:
        # if i in A:
            # continue
        # else:
            # A.append(i)
    # if len(A)==2:
        # return "Yes"
    # else:
        # return "No"
    # pass
# if __name__=="__main__":
    # s= input()
    # result=isdiagnotic(s)
    # print(result)

from __future__ import print_function
n=int(input())
A=[n]
while n!=1:
    if n%2==0:
        n=n//2
    else:
        n=(n*3)+1
    A.append(n)


for i in A:
    print i,

# sampleInput=input()
# A=list(sampleInput.split(" "))
# print(len(A))