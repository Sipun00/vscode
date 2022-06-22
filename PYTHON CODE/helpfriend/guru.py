# T=3
# N=[10,25,1]
# def cubesquare(T,N):
    # 
    # for i in N:
        # c=0
        # for j in range(2,i+1):
            # if j*j<=i:
                # c+=1
        # for k in range(2,i+1):
            # if k*k*k<=i:
                # c+=1
        # print(c+1)
# print(cubesquare(T,N))

def uniqueplants(N,H):
    c=0
    for i in range (N):
        if i==0:
            if H[i]<H[i+1]:
                c+=1
        elif i==N-1:
            if H[i]<H[i-1]:
                c+=1
        elif H[i]<H[i+1] and H[i]<H[i-1]:
            c+=1
    return c
print(uniqueplants(4,[12,10,15,9]))
    
    
    
    
    
    