class Node:
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
    def PrintTree(self,level=0):
        if self.left:
           self.left.PrintTree(level+1)
        print(self.data,end=' ')
    
        if self.right:
           self.right.PrintTree(level+1)  
              
    def PrintTreeinshape(self,level=0):
        if self.right:
            self.right.PrintTreeinshape(level+1)
        #print(self.data,sep="  ")
        
        print(' ' * 4 * level + '-> ' + str(self.data))
        if self.left:
            self.left.PrintTreeinshape(level+1)
    def inorderTraversal(self, root):
        res = []
        if root:
           res = self.inorderTraversal(root.left)
           res.append(root.data)
           res = res + self.inorderTraversal(root.right)
        return res 
    def PreorderTraversal(self,root):
        res=[]
        if root:
            res.append(root.data)
            res = res + self.PreorderTraversal(root.left)
            res = res + self.PreorderTraversal(root.right)
        return res
    def PostorderTraversal(self, root):#left>right>root
        res = []
        if root:
           res = self.PostorderTraversal(root.left)
           res = res + self.PostorderTraversal(root.right)
           res.append(root.data)
        return res
# root = Node(12)
# root.insert(13)
# root.insert(14)
# root.insert(3)
# root.PrintTree()
b=int(input(" Root node::"))
root=Node(b)
c=True
while(True):
    a=int(input("if you want to stop enter -1/////else enter  leaf node::"))
    if a==-1:
        break
    else:
        root.insert(a)
print("tree=",end=" ")
root.PrintTree()

print("\n")

print("tree in shape")

root.PrintTreeinshape() 

print("inorder=",end=" ")
print(root.inorderTraversal(root))

print("Preorder=",end=" ")
print(root.PreorderTraversal(root))

print("Postorder=",end=" ")
print(root.PostorderTraversal(root))


