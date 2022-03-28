"""Top View of Binary Tree 
Medium Accuracy: 32.3% Submissions: 100k+ Points: 4
Given below is a binary tree. The task is to print the top view of binary tree. Top view of a binary tree is the set of nodes visible when the tree is viewed from the top. For the given below tree

       1
    /     \
   2       3
  /  \    /   \
4    5  6   7

Top view will be: 4 2 1 3 7
Note: Return nodes from leftmost node to rightmost node.

Example 1:

Input:
      1
   /    \
  2      3
Output: 2 1 3
Example 2:

Input:
       10
    /      \
  20        30
 /   \    /    \
40   60  90    100
Output: 40 20 10 30 100"""

# Tree Node
# class Node:
#     def __init__(self, val):
#         self.right = None
#         self.data = val
#         self.left = None

class Solution:
      #Function to return a list of nodes visible from the top view 
    #from left to right in Binary Tree.
    
    def verticaltraversal(self,root,h_dist,v_dist,values):#refer from verticaltraversal.py
        if not root:
            return
        if h_dist in values:
            values[h_dist].append((v_dist,root.data))
        else:
            values[h_dist]=[(v_dist,root.data)]
        self.verticaltraversal(root.left,h_dist-1,v_dist+1,values)
        self.verticaltraversal(root.right,h_dist+1,v_dist+1,values)
    def topView(self,root):
        #Your code here
        v_dist=0
        h_dist=0
        values={}
        result=[]
        re=[]
        self.verticaltraversal(root,h_dist,v_dist,values)
        
        
        for x in sorted(values.keys()):
            column=[i[1] for  i in sorted(values[x])]
            result.append(column)
        for i in result:
            
            re.append(i[0])
                
        return re

    
        
        # code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

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
    
    
    s=input("type element of tree// type N for none::")
    root=buildTree(s)
    ob= Solution()
    
    res = ob.topView(root)
    for i in res:
        print(i,end=" ")
    print()