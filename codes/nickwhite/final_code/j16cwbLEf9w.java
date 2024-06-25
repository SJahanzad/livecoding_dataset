class Solution {
    public boolean isCompleteTree(TreeNode root) {
        boolean end = false;
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);

        while (!queue.isEmpty()) {
            TreeNode current_node = queue.poll();
            if (current_node == null) {
                end = true;
            } else {
                if (end) return false;
                queue.offer(current_node.left);
                queue.offer(current_node.right);
            }
        }

        return true;
    }
}
