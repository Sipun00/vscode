









def moh(x,a):
    
    


    
   
    
    

    while (x>=0):

        
        e=a[0]
        if x==2:
            for j in range (len(a)):
                if j==(len(a)-1):
                   a[j]=abs(a[j]-e)
                        
                else:    
                        a[j]=abs(a[j+1]-a[j]) 
            print(a)
            

  
        else:
            for j in range (len(a)):
                if j==(len(a)-1):
                   a[j]=abs(a[j]-e)
                        
                else:    
                        a[j]=abs(a[j+1]-a[j]) 
        x-=1        
                
    return a 
# m=int(input(""))
# a=[]
    # 
# for i in range (m):
    # n=int(input("enter"))
# 
    # a.append(n)
# x=int(input("x")) 
# print(a)                   
         
# print(moh(x,a))    
print(moh(8,[8,10,15,3,25,4]))    
       
       
               
        
         
        


