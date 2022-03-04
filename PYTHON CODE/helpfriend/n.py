


ch="abcdefghijklmnopqrstuvwxyz"
a="h"
b=23
for i in range(len(ch)):
    if ch[i]==a:
        k=i
        
    else:
        continue
if (b+k)>26:
    m=(b+k)-26
    ans=ch[m] 
else:
    m=b+k
    ans=ch[m]  

print(ans)       
