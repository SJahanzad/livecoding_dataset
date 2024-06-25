class Solution {
    public String reverseOnlyLetters(String S) {
        StringBuilder reversed_string = new StringBuilder();
        int j = S.length() - 1;

        for (int i = 0; i < S.length(); i++) {
            if (Character.isLetter(S.charAt(i))) {
                while (!Character.isLetter(S.charAt(j))) {
                    j--;
                }
                reversed_string.append(S.charAt(j));
                j--;
            } else {
                reversed_string.append(S.charAt(i));
            }
        }

        return reversed_string.toString();
    }
}
