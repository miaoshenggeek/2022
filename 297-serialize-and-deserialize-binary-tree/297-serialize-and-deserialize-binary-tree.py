# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        rt=[]
        def helper(root):
            if not root:
                rt.append("#,")
                return
            rt.append(str(root.val)+",")
            helper(root.left)
            helper(root.right)
        helper(root)
        return "".join(rt)
            
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        arr=data.split(",")
        def helper(arr):
            if arr[-1]=="#":
                arr.pop()
                return None
            root=TreeNode(arr[-1])
            arr.pop()
            root.left=helper(arr)
            root.right=helper(arr)
            return root
        arr.reverse()
        return helper(arr)
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))