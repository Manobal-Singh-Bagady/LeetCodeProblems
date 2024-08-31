class Solution {
    boolean checkPalindrome(int i, String s) {
        if (i >= s.length() / 2)
            return true;

        if (s.charAt(i) != s.charAt(s.length() - i - 1))
            return false;

        return checkPalindrome(i + 1, s);
    }

    public boolean isPalindrome(String s) {
        s = s.toLowerCase();
        s = s.replaceAll("[^a-zA-Z0-9]", "");
        return checkPalindrome(0, s);
    }
}