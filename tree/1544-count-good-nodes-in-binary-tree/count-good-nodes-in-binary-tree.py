# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        count = 0
        stack =[(root, [root.val])]
        result =[]

        while stack:
            node, path = stack.pop()
            
             
            if node.right:
                stack.append((node.right, path+[node.right.val]))
                
            if node.left:
                stack.append((node.left, path+[node.left.val]))
            result.append(path)
        
        for ele in result:
            if ele[-1] == max(ele):
                count+=1

        return count