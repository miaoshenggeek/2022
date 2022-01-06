# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        
        def find(root,v):
            if not root:return 
            if root.val==v:
                path.append("".join(res))
                #print(path)
                return
            res.append("L")
            find(root.left,v)
            res.pop()
            res.append("R")
            find(root.right,v)
            res.pop()
        res=[]  
        path=[]
        find(root,startValue)
        find(root,destValue)
        pathS=path[0]
        pathD=path[1]
        #print(pathS,pathD)
        prefix=0
        for i in range(len(pathS)):
            if i<len(pathD) and pathS[i]==pathD[i]:
                #print("same")
                prefix+=1
                continue
            prefix=i
            break
        #print(prefix)
        pathS=pathS[prefix:]
        pathD=pathD[prefix:]
        
        return "U"*len(pathS)+pathD
"""
[5,1,2,3,null,6,4]
3
6
[2,1]
2
1
[1,2]
2
1
[1,3,8,7,null,4,5,6,null,null,null,null,null,null,2]
2
1"""
            
            