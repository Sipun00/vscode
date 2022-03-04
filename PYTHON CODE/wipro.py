def sockMerchant(n, ar):
    pair = 0
    d = {}
    for i in ar:
        if i in d:
            d[i] += 1
        if i not in d:
            d[i] = 1
        print(type(d))    
    print(d)
    for x in d:
        u = d[x]//2
        pair += u
    return pair
n=int(input("n"))
ar=[]
for i in range(n):
    x=int(input("k"))
    ar.append(x)
print(sockMerchant(n,ar))    