# import numpy as np
import cmath
# def alpossible(a,mid,m,n,e):
    # su=0
    # stucount=1
    # for i in range(n):
        # for j in range(1,e):
            # if su+(a[i]*j)<=mid:
                # su=su+(a[i]*j)
            # else:
                # stucount+=1 
                # 
                # if stucount>m or a[i]*j>mid:
                    # return False 
                # su=0    
                # break
                #  
    # return True    
    # 
# 
from cmath import sqrt


a=[1,2,3,4]
m=11
n=len(a)
# s=0
# sum=0
# ans=0
# n=len(a)
# b=np.max(a)
# 
# for i in range(1,m+1):
    # sum=sum+(b*i)
# e=sum
# 
# 
# mid=(s+e)//2
# 
# while(s<=e):
    # if alpossible(a,mid,m,n,e):
        # ans=mid
        # e=mid-1
    # else:
        # s=mid+1 
    # mid=(s +e)//2
# 
# 
# print(ans)       
        #   
s=1
e=5*(m*(m+1))
while e>s:
    mid=(e+s)//2
    d=0
    for i in range(n-1):
        d=d+(-1+sqrt(1+(8*mid)/a[i]))//2
        if d<m:
            s=mid+1
        e=mid
print(e)            
            
