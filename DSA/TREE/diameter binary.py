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
    diameter_=0
     # main function starts here   
    def heightTree(self,root):
        if not root:
            return 0
        l=self.heightTree(root.left)
        r=self.heightTree(root.right)
        self.diameter_=max(self.diameter_,1+l+r)#to store the max value to find diameter//
                                                #some time max diameter exist only in left or right side
        return 1+max(l,r)
    #Function to return the diameter of a Binary Tree.
    def diameter(self,root):
        # Code here
        if root==None:
            return 0
        self.diameter_=0
        self.heightTree(root)
        return self.diameter_



        
b=int(input(" Root node::"))
root=Node(b)
c=True
while(True):
    a=int(input("if you want to stop enter -1/////else enter  leaf node::"))
    if a==-1:
        break
    else:
        root.insert(a)
print(Solution().diameter(root))

        