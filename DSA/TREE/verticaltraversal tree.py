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