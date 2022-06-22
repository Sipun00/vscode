# d=input()
# A=["monday","tuesday","wednesday","thursday","friday",]
# c=0
# for i in range(30):
    # if d=="saturday" or d=="sunday":
        # continue
    # else:
        # if d in A:
            # s=A.index(d)
            # c+= 

        
# import string 
# 
#  
# 
# Line1 = "And Then There Were None" 
# 
# Line2 = "Famous In Love" 
# 
# Line3 = "Famous Were The Kol And Klaus" 
# 
# Line4 = Line1 + Line2 + Line3 
# print(Line4)
# 
# print("And" in Line4) 
# 
# def isprime(n):
    # for i in range(2,n):
        # if n%i==0:
            # return False
    # return True
# c=1
# for i in range(2,input1+1):
    # if iprime(i):
        # c+=1
# return c
# 
# 
input1=4
input2=[1,2,9,9]
def ma(input1,input2):

    a=""
    for i in input2:
        a+=str(i)
    b=int(a)+1
    b=str(b)
    if len(b)>input1:
        b=b[1:]
        return 0
    for i in range(input1):
        if input2[i]!=int(b[i]):
            return i+1
print(ma(5,[1,2,9,9,9]))

b="kjlh"
b=b[1:]
print(b)