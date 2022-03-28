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



def PrintTreeinshape(root,level=0):#this is for diagram presernation of tree
    if root.right:
        PrintTreeinshape(root.right,level+1)
    #print(self.data,sep="  ")
    
    print(' ' * 4 * level + '-> ' + str(root.data))
    if root.left:
        PrintTreeinshape(root.left,level+1) 
def printBinaryTree(root, space, height):
 
    # Base case
    if root is None:
        return
 
    # increase distance between levels
    space += height
 
    # print right child first
    printBinaryTree(root.right, space, height)
    print()
 
    # print the current node after padding with spaces
    for i in range(height, space):
        print(' ', end='')
 
    print(root.data, end='')
 
    # print left child
    print()
    printBinaryTree(root.left, space, height)   
if __name__ == '__main__':
    
    
    s=input("element of tree(__type N for none value__)")
    root=buildTree(s)
    
    PrintTreeinshape(root)
    space = 0
    height = 10
    
    printBinaryTree(root, space, height)
    
    
    
