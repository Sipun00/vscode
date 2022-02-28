def rotate(a,k):
    n=len(a)
    b=[0]*n
    for i in range(n):
        b[(i+k)%n]=a[i]

    a=b
    return a


a=[1,2,3,4,5]
k=3
print(rotate(a,k))        

    
