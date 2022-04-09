"""Given a binary tree of size  N, a node and a positive integer k., Your task is to complete the function kthAncestor(), the function should return the kth ancestor of the given node in the binary tree. If there does not exist any such ancestor then return -1.


Example 1:



Input:
     K = 2
     Node = 4
Output: 1
Explanation:
Since, K is 2 and node is 4, so we
first need to locate the node and
look k times its ancestors.
Here in this Case node 4 has 1 as his
2nd Ancestor aka the Root of the tree.
 

Example 2:

Input:
k=1 
node=3
      1
    /   \
    2     3

Output:
1
Explanation:
K=1 and node=3 ,Kth ancestor of node 3 is 1. """





































def solve(root,node,A,ans):
    
    #code here
    if root==None:
        return
    if root.data==node:
        for i in A:
            ans.append(i)
        
        
        
        
        
        
        return 
    A.append(root.data)
    solve(root.left,node,A,ans)
    solve(root.right,node,A,ans)
    A.pop()


def kthAncestor(root,k, node):
    A=[]
    #code here
    ans=[]
    solve(root,node,A,ans)
    if len(ans)==0:
        return -1
    elif len(ans)<k:
        return -1
    return ans[len(ans)-k]

    
from collections import deque
# 
# 

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
        k=kthAncestor(root,a,b)
        print(k)

