/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public TreeNode replaceValueInTree(TreeNode root) {
        if (root == null) return null;

        // Queue for BFS traversal
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);

        // Set root's value to 0 because it has no cousins
        root.val = 0;

        while (!queue.isEmpty()) {
            int levelSize = queue.size();
            int levelSum = 0;
            List<TreeNode> currentLevelNodes = new ArrayList<>();

           
            for (int i = 0; i < levelSize; i++) {
                TreeNode node = queue.poll();
                currentLevelNodes.add(node);

                if (node.left != null) {
                    levelSum += node.left.val;
                    queue.offer(node.left);
                }
                if (node.right != null) {
                    levelSum += node.right.val;
                    queue.offer(node.right);
                }
            }

           
            for (TreeNode node : currentLevelNodes) {
                int siblingSum = 0;

                if (node.left != null) siblingSum += node.left.val;
                if (node.right != null) siblingSum += node.right.val;

                if (node.left != null) {
                    node.left.val = levelSum - siblingSum;
                }
                if (node.right != null) {
                    node.right.val = levelSum - siblingSum;
                }
            }
        }

        return root;
    }

    
}