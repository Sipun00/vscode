a=["k","i"," ","l","j"," ","p","o"]
j=-1
b=[]
k=len(a)
for i in range(1,(len(a)+1)):

    if a[-i]==" ":
       for j in range((len(a)-i+1),k):
           b.append(a[j])
       k=len(a)-i
       b.append(" ")   
    elif i==len(a):
         for j in range(k):
             b.append(a[j])


 













print(b)
