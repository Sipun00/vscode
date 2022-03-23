#Given a binary tree, find if it is height balanced or not. 
#A tree is height balanced if difference between heights of left and right subtrees is not more than one for all nodes of tree. 
# A height balanced tree
        # 1
    #  /     \
#    10      39
#   /
# 5
# 
# An unbalanced tree
        # 1
    #  /    
#    10   
#   /
# 5
class Node:                 #creation of tree
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
    def insert(self,data):
        if self.data:
            if data<self.data:
                if self.left is None:
                    self.left=Node(data)
                else:
                    self.left.insert(data)
            if data>self.data:
                if self.right is None:
                    self.right=Node(data)
                else:
                    self.right.insert(data)         
        else:
            self.data=data



class Solution:

    def isBalanced1(self,root):
        if root is None:
            return 0,True
        lh,rh=0,0
        lb,rb=True,True
        if root.left !=None:
            lh,lb=self.isBalanced1(root.left)
            if not lb:
                return lh,False
        if root.right!=None:
            rh,rb=self.isBalanced1(root.right)
            if not rb:
                return rh,False
        diff,height=abs(lh-rh),max(lh,rh)+1
        return height,-1<diff<2
    def isBalanced(self,root):
        return self.isBalanced1(root)[1]






s=input("put value for tree")#its a 
ip=list(map(str,s.split()))
root=Node(int(ip[0]))
i=1

while( i<len(ip)):
    
    root.insert(int(ip[i]))
    i+=1
    


print(Solution().isBalanced(root))
