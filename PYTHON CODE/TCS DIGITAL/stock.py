#when to buy and sell and find max profit
a=[100,180,260,320,40,535,695]
o=0
i=1
p=0
while i<len(a):
    if i==len(a)-1:
       p+= (a[i]-a[o]) 
       print("b",o,"s",i)
    if a[i]<a[i-1]:
        p=p+(a[i-1]-a[o])
        print("b",o,"s",i-1)
        o=i
        i=i+1
    
    
    
    else:
        i=i+1
print(p)            


