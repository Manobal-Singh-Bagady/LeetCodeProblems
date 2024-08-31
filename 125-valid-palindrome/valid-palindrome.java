class Solution {
    boolean checkPalindrome(int l, int r, String s) {
        if (l > r)
            return true;

        if (s.charAt(l) != s.charAt(r))
            return false;

        return checkPalindrome(l + 1, r - 1, s);
    }

    public boolean isPalindrome(String s) {
        s = s.toLowerCase();
        s = s.replaceAll("[^a-zA-Z0-9]", "");
        return checkPalindrome(0, s.length() - 1, s);
    }
}