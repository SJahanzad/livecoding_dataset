class Solution {
    public TreeNode pruneTree(TreeNode root) {
        if (root == null) return null;
        containsOne(root);
        return root;
    }

    public boolean containsOne(TreeNode node) {
        if (node == null) return false;
        boolean left_contains = containsOne(node.left);
        boolean right_contains = containsOne(node.right);
        if (!left_contains) {
            node.left = null;
        }
        if (!right_contains) {
            node.right = null;
        }
        return node.val == 1 || left_contains || right_contains;
    }
}
