"""Given a Binary Tree with all unique values and two nodes value, n1 and n2. The task is to find the lowest common ancestor of the given two nodes. We may assume that either both n1 and n2 are present in the tree or none of them are present.

Example 1:

Input:
n1 = 2 , n2 = 3  
       1 
      / \ 
     2   3
Output: 1
Explanation:
LCA of 2 and 3 is 1.
Example 2:

Input:
n1 = 3 , n2 = 4
           5    
          /    
         2  
        / \  
       3   4
Output: 2
Explanation:
LCA of 3 and 4 is 2. """



'''
class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None
'''

class Solution:
    #Function to return the lowest common ancestor in a Binary Tree.
    def lca(self,root, n1, n2):
        # Code here
        if root==None:
            return None
        elif root.data==n1 or root.data==n2:
            return root
        leftans=self.lca(root.left,n1,n2)
        rightans=self.lca(root.right,n1,n2)
        if leftans!=None and rightans!=None:
            return root
        
        elif leftans!=None and rightans==None:
            return leftans
        
        elif leftans==None and rightans!=None:
            return rightans
        else:
            return None
        




#{ 
#  Driver Code Starts
#Initial Template for Python 3

#Contributed by Sudarshan Sharma
from collections import deque
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None



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
    
    
if __name__=="__main__":
    
        s=input("elememnt of tree")
    
        root=buildTree(s)
        a,b=list(map(int,input("n1,n2").split()))
        k=Solution().lca(root,a,b)
        print(k.data)



# } Driver Code Ends