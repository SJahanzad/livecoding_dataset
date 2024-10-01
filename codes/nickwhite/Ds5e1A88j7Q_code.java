class Solution {
    public List<Integer> postorder(Node root) {
        LinkedList<Node> stack = new LinkedList<>();
        LinkedList<Integer> output_arr = new LinkedList<>();

        if (root == null) {
            return output_arr;
        }

        stack.add(root);
        while (!stack.isEmpty()) {
            Node node = stack.pollLast();
            output_arr.addFirst(node.val);
            for (Node child : node.children) {
                stack.add(child);
            }
        }

        return output_arr;
    }
}
