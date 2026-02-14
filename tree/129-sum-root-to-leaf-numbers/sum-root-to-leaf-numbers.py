# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        stack = [(root,root.val)]
        result = []

        while stack:

            node, prev = stack.pop()

            if not node.left and not node.right:
                result.append(prev)
                continue
            
            if node.right:
                stack.append((node.right, prev*10+ node.right.val))
            if node.left:
                stack.append((node.left, prev*10+ node.left.val))
        
        return sum(result)
        
        