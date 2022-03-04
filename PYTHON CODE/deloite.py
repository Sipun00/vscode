st=input("STUDIN")
a=list(st)
b=[]

# for i in range (len(a)):
    # if a[i].isdigit():
# 
    #    b.append(i) 
    # 
# print(b) 
# 
# c=''.join(str(e) for e in b)""
# print(c)



# for i in st:
# 
    # if i.isdigit():
    #    b.append(st.index(i))
    #    
# print(b) 
# c=''.join(str(e) for e in b)
# print(c)


res=""
for i in range(len(st)):
    if st[i]>="0" and st[i]<="9":
        res=res+str(i)
print(res)      
 
       