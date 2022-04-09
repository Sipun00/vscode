"""Given inorder and postorder traversals of a Binary Tree in the arrays in[] and post[] respectively. The task is to construct the binary tree from these traversals.

 

Example 1:

Input:
N = 8
in[] = 4 8 2 5 1 6 3 7
post[] =8 4 5 2 6 7 3 1
Output: 1 2 4 8 5 3 6 7
Explanation: For the given postorder and
inorder traversal of tree the  resultant
binary tree will be
           1
       /      \
     2         3
   /  \      /  \
  4    5    6    7
   \
     8
 

Example 2:

Input:
N = 5
in[] = 9 5 2 3 4
post[] = 5 9 3 4 2
Output: 2 9 5 4 3
Explanation:  
the  resultant binary tree will be
           2
        /     \
       9       4
        \     /
         5   3"""



'''
class Node:
            def __init__(self, data):
                self.data = data
                self.left = self.right = None
'''

#Function to return a tree created from postorder and inoreder traversals.
# def build(In,post,start,end,ind):
#     if start>end:
#         return None
    
#     node=Node(post[ind])
#     if start==end:
#         return node
#     pos=In.index(post[ind])
#     ind-=1
#     node.right=build(In,post,pos+1,end,ind)
#     node.left=build(In,post,start,pos-1,ind)
#     return node
def buildTree(In, post, n):
    # your code here
    if not post:
        return None
    pos=In.index(post[-1])
    node=Node(post[-1])
    node.left=buildTree(In[:pos],post[:pos],len(In[:pos]))
    node.right=buildTree(In[pos+1:],post[pos:-1],len(In[:pos]))
    return node
    

#{ 
#  Driver Code Starts
#Initial Template for Python 3















# Helper function that allocates  
# a new node  
class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

# This funtcion is here just to test  
def preOrder(node):
    if node == None:
        return
    print(node.data, end=" ")
    preOrder(node.left)
    preOrder(node.right)
    
if __name__ == '__main__':
    
    
    n = int(input("n::"))  # number of nodes in tree
    in_order = list(map(int, input("inorder::").strip().split()))  # parent child info in list
    post_order = list(map(int, input("postordre::").strip().split()))  # parent child info in list
    preOrder(buildTree(in_order,post_order,n))
    print()


# } Driver Code Ends