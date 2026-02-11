# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if root is None:
            return []
        
        q = deque([root])

        rightPeek = []

        while q:
            last_val = None
            for _ in range(len(q)):
                
                #left_node = q.popleft()
                #right_node = q.popright()
                node = q.popleft()
                last_val = node.val
                print(node.val)

                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)

            print('**')
            rightPeek.append(last_val)
        
        return rightPeek