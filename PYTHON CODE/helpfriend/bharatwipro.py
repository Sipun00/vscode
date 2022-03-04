# a="11233455"
# b=[]
# c=0
# for i in range(len(a)):
    # for j in range(i+1,len(a)):
        # if a[i] in b:
            # break
        # elif a[i]==a[j]:
            # c+=1
            # b.append(a[i])
# print(c)
# 
# 
a=int(input())
b=input()
c=list(b.split(" "))
d=0
for i in range(a):
    if int(c[i])<0:
        d+=1
print(d)        