









# def moh(x,a):
    # 
    # 
# 
# 
    # 
#    
    # 
    # 
# 
    # while (x>=0):
# 
        # 
        # e=a[0]
        # if x==2:
            # for j in range (len(a)):
                # if j==(len(a)-1):
                #    a[j]=abs(a[j]-e)
                        # 
                # else:    
                        # a[j]=abs(a[j+1]-a[j]) 
            # print(a)
            # 
# 
#   
        # else:
            # for j in range (len(a)):
                # if j==(len(a)-1):
                #    a[j]=abs(a[j]-e)
                        # 
                # else:    
                        # a[j]=abs(a[j+1]-a[j]) 
        # x-=1        
                # 
    # return a 
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
#print(moh(8,[8,10,15,3,25,4]))    

# a=int(input())
# if a>=5:
    # sum=0
    # for i in range(5,a+1):
        # sum+=i
    # print(sum)
# else:
    # print(0)
# a=int(input())
# while(a!=0):
    # print(a*"*")
    # a-=1
    #    
    #    
def print2largest(arr,arr_size): 
  
    # There should be atleast 
        # two elements  
    if (arr_size < 2): 
      
        print(" Invalid Input ") 
        return
      
  
    first = second = -2147483648
    for i in range(arr_size): 
      
        # If current element is 
                # smaller than first 
        # then update both 
                # first and second  
        if (arr[i] > first): 
          
            second = first 
            first = arr[i] 
          
  
        # If arr[i] is in 
                # between first and  
        # second then update second  
        elif (arr[i] > second and arr[i] != first): 
            second = arr[i] 
      
    if (second == -2147483648): 
        print("There is no second largest element") 
    else: 
        print("The second largest element is", second) 
  
  
# Driver program to test 
# above function  
arr = [12, 35, 1, 10, 34, 1] 
n =len(arr) 
  
#print2largest(arr, n) 
  
# This code is contributed 
# by Anant Agarwal. 
k=2
m=3
k,m=m,k
print(k,m)
               
        
         
        


