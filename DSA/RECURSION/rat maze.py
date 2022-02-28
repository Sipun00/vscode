def issafe(x,y,n,b,a):
    if (x>=0 and x<n)  and (y>=0 and y<n) and (b[x][y]==0) and (a[x][y]==1) :

        return True
    else:
        return False    





def solve(a,b,n,x,y,ans,path,s):
    if (x==n-1)and (y==n-1):
        #ans.append(path)
        ans.append(s)
        #print (ans, "\n")
        return ans
    b[x][y]=1
    
    #Down
    x1=x+1
    y1=y
    if(issafe(x1,y1,n,b,a)):
        path.append("D")
        s+="d"
        solve(a,b,n,x1,y1,ans,path,s)
        path.remove("D")
        s=s[:-1]
    #left
    x1=x
    y1=y-1
    if(issafe(x1,y1,n,b,a)):
        path.append("L")
        s+="l"
        solve(a,b,n,x1,y1,ans,path,s)
        path.remove("L") 
        s=s[:-1] 
    #Right
    x1=x
    y1=y+1      
    if(issafe(x1,y1,n,b,a)):
        path.append("R")
        s+="r"
        solve(a,b,n,x1,y1,ans,path,s)
        path.remove("R")  
        s=s[:-1]
    #up
    x1=x-1
    y1=y    
    if(issafe(x1,y1,n,b,a)):
        path.append("U")
        s+="u"
        solve(a,b,n,x1,y1,ans,path,s)
        path.remove("U") 
        s=s[:-1]
    b[x][y]=0         

n=3
a=[[1,0,1],
    [1,1,0],
    [1,1,1]]
b=[[0,0,0],
    [0,0,0],
    [0,0,0]] 
ans=[]   
x=0
y=0 
path=[] 
s=""
solve(a,b,n,x,y,ans,path,s) 
print(ans)

#33