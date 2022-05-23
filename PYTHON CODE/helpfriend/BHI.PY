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

# from __future__ import print_function
# n=int(input())
# A=[n]
# while n!=1:
    # if n%2==0:
        # n=n//2
    # else:
        # n=(n*3)+1
    # A.append(n)
# 
# 
# for i in A:
    # print i,
# 
# sampleInput=raw_input()
# A=list(sampleInput.split())
# c=0
# for i in A:
    # if i[0].isdigit():
        # c+=1
# 
# print(c)
# 
# 
# 
# 
# a=int(input())
# if a>=184:
    # print("Taller")
# if a>=154 and a<184:
    # print("Average")
# if a<154:
    # print("Dwarf")
# A=["@",'#','$','%','&','*','(']
# a=input()
# b=list(a.split())
# c=0
# for i in b:
    # if i[0] in A:
        # c+=1
# prin

# a=int(input())
# b=int(input())
# c=int(input())
# if a>b and a>c:
    # print("largest Number:", a)
# if b>a and b>c:
    # print("largest Number:", b)
# if c>a and c>b:
    #print("largest Number:", c)
# a=int(input())
# b=input()
# A=list(map(int,b.split()))
# A.sort()
# ans=A[-2]//A[1]
# print(ans)









a=int(input())
b=input()
A=list(map(int,b.split()))
k=a//2
A[0:k],A[k:]=A[k:],A[0:k]


  
for i in A:
    print(i,end=" ")   


