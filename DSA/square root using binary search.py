import numpy as np
def sqrt(n):
        s=0
        e=n
    
        ans=-1
        mid=s+(e-s)//2
        while(s<=e):

            x=mid*mid
            if x==n:
               ans=mid
               return ans
            elif x>n:
                
                e=mid-1
            elif x<n:
                ans=mid
                s=mid+1
            mid=s+(e-s)//2   
        return ans  
def moreacurate(n,pre,tempsol):
      factor=1
      a=tempsol
      for i in range(pre):
          factor=factor/10
  
          
          for j in np.arange(a,n,factor):
              if j*j==n:
                  ans=j
              elif j*j<n:
                  ans=j
                  
               
      return ans              
                          
                
            
            
                
                           
            
                
                
                
            

            
n=int(input("enter ")) 

tempsol=sqrt(n) 
print(moreacurate(n,3,tempsol))  

                  