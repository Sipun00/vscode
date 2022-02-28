def alpossible(a,mid,m):
    su=0
    stucount=1
    for i in range(len(a)):
        if su+a[i]<=mid:
            su=su+a[i]
        else:
            stucount+=1 
            
            if stucount>m or a[i]>mid:
                return False 
            su=a[i]
    return True        









a=[10,20,30,40]
m=2
s=0
sum=0
ans=0
for i in range(len(a)):
    sum=sum+a[i]
e=sum
mid=(s+e)//2
while(s<=e):
    if alpossible(a,mid,2):
        ans=mid
        e=mid-1
    else:
        s=mid+1 
    mid=(s +e)//2


print(ans)       
    


       