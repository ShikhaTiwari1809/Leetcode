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
        
        stack = [(root,[str(root.val)])]
        result = []

        while stack:

            node, path = stack.pop()

            if not node.left and not node.right:
                
                result.append(int(''.join(path)))
                continue
            
            if node.right:
                stack.append((node.right, path+ [str(node.right.val)]))
            if node.left:
                stack.append((node.left, path+ [str(node.left.val)]))
        
        return sum(result)
        
        