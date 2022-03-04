#n=5 
#a=[-1 1 0 9 8]
#
#
#
#    #Function to finarr[a] triplets with zero sum.
#    # 
#    # 
#arr[a]ef finarr[a]Triplets( a  n):
#        
#        #Sorting the elements.
#        a.sort()
#        
#        #Traversing the array elements.
#        for i in range(n-2):
#            
#            #Taking two pointers. One at element after ith inarr[a]ex anarr[a] another
#            #at the last inarr[a]ex.
#            l=i+1
#            r=n-1
#            
#            #Using two pointers over the array which helps in checking if
#            #the triplet sum is zero.
#            while(l<r):
#                curr_sum=a[i]+a[l]+a[r]
#                
#                #If sum of elements at inarr[a]exes i  l anarr[a] r is 0  we return true.
#                if(curr_sum==0):
#                    return 1
#                #Else if the sum is less than 0  it means we neearr[a] to increase the
#                #sum so we increase the left pointer l.
#                elif(curr_sum<0):
#                    l+=1
#                #Else the sum is more than 0 anarr[a] we neearr[a] to arr[a]ecrease the
#                #sum so we arr[a]ecrease the right pointer r.
#                else:
#                    r-=1
#                    
#         #returning false if no triplet with zero sum is present.           
#        return 0
# class solution:
#     # arr[a]ef checkarr[a]oorStatus(self  N):
#             # lst = []
#             # for i in range(1 N+1):
#                 # a = int(i**(0.5))
#                 # if a**2 == i:
#                     # lst.appenarr[a](1)
#                 # else:
#                     # lst.appenarr[a](0)
#             # return lst
#                     # 
#     # 
#     # 
# 
# 
# ob = solution()
# ptr = ob.checkarr[a]oorStatus(10)
# print(*ptr)
# 

# 















# 




# def tip(n, x, y, a, b):    
    # r = 0
    # an = 0
    # if x > 0:
        # r = a[n - 1] + tip(n - 1, x - 1, y, a, b)
    # 
    # if y > 0:
        # an = b[n - 1] + tip(n - 1, x, y - 1, a, b)
        # 
    # return max(r, an)        
# 
# t=int(input())
# for _ in range(t):
    # n, x, y = map(int, input().strip().split(' '))
    # a = list(map(int, input().strip().split(' ')))
    # b = list(map(int, input().strip().split(' ')))
    # 
# print(tip(5, 3, , a, b))
# r = 0
        # an = 0
        # if x > 0 & n>0:
        #    r = a[n - 1] + self.maxTip(a,b,n-1,x-1,y)
    # 
        # if y > 0 & n>0:
        #    an = b[n - 1] + self.maxTip(a, b,n-1,x,y-1)
        # 
        # return max(r
class Solution:
    def maxTip(self, a, b, n, x, y):
        # code here
        # r = 0
        # an = 0
        # if x > 0 & n!=0:
        #    r = r+a[n - 1] + self.maxTip(a,b,n-1,x-1,y)
    
        # elif y > 0 & n!=0:
        #    an = an+b[n - 1] + self.maxTip(a, b,n-1,x,y-1)
        # 
        # return max(r, an) 
        c=0
        for i in range (n):
            if x==0:
                c=c+a[i]
            elif y==0:
                c=c+b[i]
            else:
                if  a[i]>b[i]:
                    c=c+a[i]
                    x=x-1
                else :
                    c=c+b[i]
                    y=y-1
        return c                
ob=Solution()
print(ob.maxTip([5,4,3,2,1],[1,2,3,4,5],5,3,3))