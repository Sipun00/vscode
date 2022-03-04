a=input()
b=""
v=['a','A','e','E','i','I','o','O','u','U']
for i in a:
    if i in v:
        index=v.index(i)
        
        index=index+2
        if index>9:
            index=index-10
            b=b+v[index]
            
        else:
             b=b+v[index]  
    else:
        b=b+i
print(b)       



