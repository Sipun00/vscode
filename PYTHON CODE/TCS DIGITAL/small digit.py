#if a is given u have to find the smaest digit whose digit multipication form a
#ex a=100
#so b will be 455
#if a is 10
#b will be 25

a=100
i=9
b=""

while (i>=2):
    if a==1.0:
        break
    if a%i==0:
        a=a/i
        b=b+str(i)
        i=9
    else:
        i-=1
        continue


b=b[::-1]
print(b)      

