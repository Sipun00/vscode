"""Given 2 Arrays of Inorder and preorder traversal. Construct a tree and print the Postorder traversal. 

Example 1:

Input:
N = 4
inorder[] = {1 6 8 7}
preorder[] = {1 6 7 8}
Output: 8 7 6 1
Example 2:

Input:
N = 6
inorder[] = {3 1 4 0 5 2}
preorder[] = {0 1 3 4 2 5}
Output: 3 4 1 5 2 0
Explanation: The tree will look like
       0
    /     \
   1       2
 /   \    /
3    4   5"""

'''
# Node class

class Node:
    def __init__(self,val):
        self.data = val
        self.right = None
        self.left = None

'''

class Solution:
    def buildtree(self, inorder, preorder, n):
        
        # code here
        # build tree and return root node
        # self.preorderIter = 0
        # return self.buildtreeUtil(inorder, preorder, 0, n - 1)
        if not preorder:
        
            return None
        pos=inorder.index(preorder[0])
        node=Node(preorder[0])
        node.left=self.buildtree(inorder[:pos],preorder[1:pos+1],len(inorder[:pos]))
        node.right=self.buildtree(inorder[pos+1:],preorder[pos+1:],len(inorder[:pos]))
        return node
        
    # def buildtreeUtil(self, inorder, preorder, start, end):
    #     if start >  end:
    #         return None
    #     node = Node(preorder[self.preorderIter])
    #     inorderIndex = start+ inorder[start:end+1].index(preorder[self.preorderIter])
    #     self.preorderIter += 1
    #     node.left = self.buildtreeUtil(inorder, preorder, start, inorderIndex - 1)
    #     node.right = self.buildtreeUtil(inorder, preorder, inorderIndex + 1, end)
    #     return node


#{ 
#  Driver Code Starts
#Initial Template for Python 3

class Node:
    def __init__(self,val):
        self.data = val
        self.right = None
        self.left = None

def printPostorder(n):
    if n is None:
        return
    printPostorder(n.left)
    printPostorder(n.right)
    print(n.data, end=' ')

if __name__=="__main__":
    
    
    n = int(input("n"))
    inorder = [ int(x) for x in input().split("inorder::") ]
    preorder = [ int(x) for x in input().split("postoredr::") ]
    
    root = Solution().buildtree(inorder, preorder, n)
    printPostorder(root)
    print()

# } Driver Code Ends