
"""Bottom View of Binary Tree 
Medium Accuracy: 45.32% Submissions: 100k+ Points: 4
Given a binary tree, print the bottom view from left to right.
A node is included in bottom view if it can be seen when we look at the tree from bottom.

                      20
                    /    \
                  8       22
                /   \        \
              5      3       25
                    /   \      
                  10    14

For the above tree, the bottom view is 5 10 3 14 25.
If there are multiple bottom-most nodes for a horizontal distance from root, then print the later one in level traversal. For example, in the below diagram, 3 and 4 are both the bottommost nodes at horizontal distance 0, we need to print 4.

                      20
                    /    \
                  8       22
                /   \     /   \
              5      3 4     25
                     /    \      
                 10       14

For the above tree the output should be 5 10 4 14 25.
 

Example 1:

Input:
       1
     /   \
    3     2
Output: 3 1 2
Explanation:
First case represents a tree with 3 nodes
and 2 edges where root is 1, left child of
1 is 3 and right child of 1 is 2.

Thus nodes of the binary tree will be
printed as such 3 1 2.
Example 2:

Input:
         10
       /    \
      20    30
     /  \
    40   60
Output: 40 20 60 30"""




















# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

class Solution:
      #Function to return a list of nodes visible from the top view 
    #from left to right in Binary Tree.
    
    def verticaltraversal(self,root,h_dist,v_dist,values):#refer from verticaltree.py
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
            max=0
            v=0
            for  i in (values[x]):
                
                
                if i[0]>=max:
                    max=i[0]
                    v=i[1]

            result.append(v)
        
        
        
                
        return result

    
        
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