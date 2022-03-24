# Example 2:
# 
# Input:
    #  1          1
#    /   \      /   \
#   2     3    2     3
# Output: Yes
# Explanation: There are two trees both
# having 3 nodes and 2 edges, both trees
# are identical having the root as 1,
# left child of 1 is 2 and right child
# of 1 is 3.
# Example 2:
# 
# Input:
    # 1       1
#   /  \     /  \
#  2    3   3    2
# Output: No
# Explanation: There are two trees both
# having 3 nodes and 2 edges, but both
# trees are not identical.


class Solution:
    #Function to check if two trees are identical.
    def isIdentical(self,root1, root2):
        # Code here
        if root1==None and root2==None:
            return True
        if root1==None and root2!=None:
            return False
        if root1!=None and root2==None:
            return False
        else:
            l=self.isIdentical(root1.left,root2.left)
            r=self.isIdentical(root1.right,root2.right)
            val=(root1.data==root2.data)
            if l and r and val:
                return True
            else:
                return False

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
        


s=input("put value for tree")#its a 
s2=input("put value for tree")
ip=list(map(str,s.split()))
ip2=list(map(str,s2.split()))
root=Node(int(ip[0]))
root2=Node(int(ip2[0]))
i=1
if len(ip)!=len(ip2):
    print (False) 
else:

    while( i<len(ip)):
        root.insert(int(ip[i]))
        root2.insert(int(ip2[i]))
        i+=1
    print(Solution().isIdentical(root,root2))



      
    



