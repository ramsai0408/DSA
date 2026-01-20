# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[str]
        """
        arr=[]
        final_arr=[]
        def dfs(root):
            if root is None :
                return None
            arr.append(root.val)
            if root.left is None and root.right is None:
                final_arr.append("->".join(map(str,arr)))
            dfs(root.left)
            dfs(root.right)
            arr.pop()
        dfs(root)
        return final_arr
            
        