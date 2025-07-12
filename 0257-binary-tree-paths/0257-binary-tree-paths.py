# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        
        queue = deque([(root, str(root.val))])  # Node and its path
        res = []  # To store all paths
        while queue:
            node, path = queue.popleft()
            if not node.left and not node.right:  # Leaf node
                res.append(path)
            if node.left:
                queue.append((node.left, path + "->" + str(node.left.val)))
            if node.right:
                queue.append((node.right, path + "->" + str(node.right.val)))
            
        return res

        