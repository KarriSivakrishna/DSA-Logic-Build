# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.postOrder(root, p, q)

    def postOrder(self, node, p, q):
        if not node:
            return None

        if node==p or node==q:
            return node

        left = self.postOrder(node.left, p, q)
        right = self.postOrder(node.right, p, q)

        if left and right:
            return node
        if left:
            return left
        if right:
            return right

        return None
        