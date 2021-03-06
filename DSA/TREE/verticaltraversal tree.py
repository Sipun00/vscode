class Solution:
    
    #Function to find the vertical order traversal of Binary Tree.
    def verticaltraversal(self,root,h_dist,v_dist,values):
        if not root:
            return
        if h_dist in values:
            values[h_dist].append((v_dist,root.data))
            
        else:
            values[h_dist]=[(v_dist,root.data)]
        self.verticaltraversal(root.left,h_dist-1,v_dist+1,values)
        self.verticaltraversal(root.right,h_dist+1,v_dist+1,values)
    def verticalOrder(self, root): 
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
            for j in i:
                re.append(j)
                
        return re


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
    res = ob.verticalOrder(root)
    for i in range (len (res)):
        print (res[i], end = " ")
    