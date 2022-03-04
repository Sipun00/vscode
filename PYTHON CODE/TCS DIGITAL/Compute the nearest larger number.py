a="73475943759"
b="93458974390"
c=""



if len(a)!=len(b):
    print("-1")
else:
    for i in range(len(b)):
        min=10
        
        j=0
        while j<len(a):
            if int(b[i])>=int(a[j]):
                x=int(b[i])-int(a[j])
                if x<min:
                    min =x
                
            else:
                x=int(a[j])-int(b[i])
                if x<min:
                    min=x
            j+=1
        n=int(b[i])+min
        if n>9:
            n=int(b[i])-min
        n=str(n)
        a= a.replace(n, '', 1)
        c+=n
  
        


print(c)