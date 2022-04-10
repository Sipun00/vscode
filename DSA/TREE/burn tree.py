"""Given a binary tree and a node called target. Find the minimum time required to burn the complete binary tree if the target is set on fire. It is known that in 1 second all nodes connected to a given node get burned. That is its left child, right child, and parent.


Example 1:

Input:      
          1
        /   \
      2      3
    /  \      \
   4    5      6
       / \      \
      7   8      9
                   \
                   10
Target Node = 8
Output: 7
Explanation: If leaf with the value 
8 is set on fire. 
After 1 sec: 5 is set on fire.
After 2 sec: 2, 7 are set to fire.
After 3 sec: 4, 1 are set to fire.
After 4 sec: 3 is set to fire.
After 5 sec: 6 is set to fire.
After 6 sec: 9 is set to fire.
After 7 sec: 10 is set to fire.
It takes 7s to burn the complete tree.
Example 2:

Input:      
          1
        /   \
      2      3
    /  \      \
   4    5      7
  /    / 
 8    10
Target Node = 10
Output: 5
"""



class Solution:
    def minTime(self, root,target):
        # code here
        mapp={}
        q=[root]
        mapp[root]=None
        
        while q:
            root=q.pop(0)
            if root.data==target:
                tar=root
            
            if root.left:
                mapp[root.left]=root
                q.append(root.left)
            if root.right:
                mapp[root.right]=root
                q.append(root.right)
        #visited=collections.defaultdict(bool)
        q=[tar]
        visited=[tar.data]
        level=-1
        while q:
            for i in range(len(q)):
                node=q.pop(0)
                if node.left and node.left not in visited:
                    q.append(node.left)
                    visited.append(node.left)
                if node.right and node.right not in visited:
                    q.append(node.right)
                    visited.append(node.right)

                if mapp[node] and mapp[node] not in visited:
                    q.append(mapp[node])
                    visited.append(mapp[node])
            level+=1
        return level
            

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
    
    
        line=input("tree element::")
        target=int(input("at what node tumhe aag lagana h::"))
        root=buildTree(line)
        print(Solution().minTime(root,target))

# } Driver Code Ends