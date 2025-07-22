# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        res = []
        def inorder(node):
            if node:
                inorder(node.left)
                res.append(node.val)
                inorder(node.right)

        inorder(root)
        res.sort()

        index = 0
        def rewrite(node):
            nonlocal index
            if node:
                rewrite(node.left)
                node.val = res[index]
                index += 1
                rewrite(node.right)

        rewrite(root)
            
        