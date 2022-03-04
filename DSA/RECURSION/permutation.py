




def swap(a,i,j):
    temp=a[i]
    a[i]=a[j]
    a[j]=temp
s="abc"
s=list(s)
def perm(a,e=0):
    if e==(len(a)-1):
        print("".join(a))
    for i in range(e,len(a)):
         swap(a,e,i)
       
       
         perm(a,e+1)
         swap(a,e,i)
         
         
perm(s)            