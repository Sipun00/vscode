a=[1,2,3]
b=[9]
#out put=123+9=132=[1,3,2]
def l2s(s):
    str1=""
    for i in s:
        str1+=str(i)
    return str1 

x=int(l2s(a))
y=int(l2s(b))

z=x+y
z=str(z)
m=[0]*len(z)
print(z)
for i in range(len(z)):
    m[i]=int(z[i])
print(m)    
