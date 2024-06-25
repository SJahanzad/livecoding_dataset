/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public List<Integer> largestValues(TreeNode root) {
        List<Integer> largest_vals = new ArrayList<>();
        helper_method(root, largest_vals, 0);
        return largest_vals;
    }
    
    public void helper_method(TreeNode root, List<Integer> largest_vals, int level) {
        if (root == null) return;
        
        if (level == largest_vals.size()) {
            largest_vals.add(root.val);
        } else {
            largest_vals.set(level, Math.max(largest_vals.get(level), root.val));
        }
        
        helper_method(root.left, largest_vals, level + 1);
        helper_method(root.right, largest_vals, level + 1);
    }
}
