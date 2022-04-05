import math
def SmithNumbers(n):
    k=n
    m=[]
    
    def prime(k):
        while k%2==0:
            m.append(2)
            k=k//2
        for i in range(3,int(math.sqrt(k))+1,2):
            while k%i==0:
                  m.append(i)
                  k=k//i
        if k>2:
            m.append(k)
    s=0
    
    while n>0:
        a=n%10
        n=n//10

        s+=a
    prime(k)
    sum=0
    for i in m:
        while i>0:
              a=i%10
              i=i//10
              sum+=a
                  

    if sum==s:
        return(s)
    else:
        return(-1)
print(SmithNumbers(355))

"""def countOperation(A):
    c=0
    max=0
    for i in  A:
        if max<A.count(i):
           max=A.count(i)
    for i in range(0,(len(A)-2)):
        if A[i]!=A[i+2]:
            c+=1

            A[i+2]=A[i]
    if len(A)-max<c:
        return len(A)-max
    else:
        return c

    

    

A=[3,1,3,2]
print(countOperation(A))"""