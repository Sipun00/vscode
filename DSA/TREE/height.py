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

def height(root):#this is the main function for height


    if root is None:
        return 0
    else:
        return max(height(root.left),height(root.right))+1
b=int(input(" Root node::"))
root=Node(b)
c=True
while(True):
    a=int(input("if you want to stop enter -1/////else enter  leaf node::"))
    if a==-1:
        break
    else:
        root.insert(a)
print(height(root))#

