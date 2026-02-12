# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        
        if root is None:
            return 0
        
        
        q = deque([root])
        left_node = None

        while q:
            for _ in range(len(q)):
                
                node = q.popleft()
                left_node = node.val

                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)
        
        return left_node