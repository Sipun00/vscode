# question---remove 7,36 from the string
# a="kkak73736ezhje"
# 
# i=0
# ans=""
# while i<len(a):
    # if a[i]=='7':
        # i=i+1
    # elif a[i]=='3' and i< (len(a)-1):
        # if a[i+1]=='6':
            # i=i+2
        # else:
            # ans+=a[i]  
            # i+=1  
        # 
    # else:
        # ans+=a[i] 
        # i=i+1   
# print(ans)        
# 
    # 
# 



# a="abcdfjgerj"
# b="abcdfjger"
# 
# for i in range (len(a)):
    # if i>=len(b):
        # print(a[-1])
    # elif a[i]==b[i]:
        # continue
    # else:
        # print(a[i])
        # break

# 
n=int(input)
a=[]
for i in range(n) :
     k=int(input())
     a.append(k)
s=max(a)    
t=min(a)
ans=s+t 
print(ans)


      
 
 
 
 
n=input()

for i in range(len(n)):
    while a[i]>=0:

          k=a[i]%10
          if k%2==0:
              sum+=k
              b.append(sum)
              a[i]=k//10
              
          else:
              a[i]=a[i]//10
              b.append(sum)    
              