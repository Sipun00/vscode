'''Given a Binary Tree. Find the Zig-Zag Level Order Traversal of the Binary Tree.

 

Example 1:

Input:
        3
      /   \
     2     1
Output:
3 1 2
Example 2:

Input:
           7
        /     \
       9       7
     /  \     /   
    8    8   6     
   /  \
  10   9 
Output:
7 7 9 8 8 6 9 10 '''


'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
def zigzag(queue,root):
    if(root==null):
        return
    
    

class Solution:
    #Function to store the zig zag order traversal of tree in a list.
    def zigZagTraversal(self, root):
        # Your code here
        queue1=[]   
        '''THIS WILL STORE THE 1ST LEVEL DATA'''

        queue2=[]
        '''THIS WILL STORE THE NEXT LEVEL DATA'''
        result=[]
        queue1.append(root)
        side=0
        while(len(queue1)!=0 or len(queue2)!=0):
            if(side==0):
                while(len(queue1)!=0):
                    tmpNode=queue1.pop()
                    result.append(tmpNode.data)
                    if(tmpNode.left!=None):
                        queue2.append(tmpNode.left)
                    if(tmpNode.right!=None):
                        queue2.append(tmpNode.right)
                side=1
            else:
                while(len(queue2)!=0):
                    tmpNode=queue2.pop()
                    result.append(tmpNode.data)
                    if(tmpNode.right!=None):
                        '''RIGHT TO LEFT'''
                        queue1.append(tmpNode.right)
                    if(tmpNode.left!=None):
                        queue1.append(tmpNode.left)
                side=0
        
        return result
#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB

from collections import defaultdict
from collections import deque

class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
        
# Function to Build Tree   
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root
    
if __name__ == '__main__':
    
    
    s=input("element of tree(__type N for none value__)")
    root=buildTree(s)
    ob = Solution()
    res = ob.zigZagTraversal(root)
    for i in range (len (res)):
        print (res[i], end = " ")
    print()
# } Driver Code Ends 