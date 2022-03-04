a=[1,2,4]
res=map(lambda x,y: x+y,a,a)
print(list(res))

b=[3,5,6]
res=map(lambda x,y:x+y,a,b)
print(list(res))


l=['sat','bat']

test=list(map(list,l))
print(test)