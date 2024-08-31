class Solution {

    void swap(int l, int r, char[] arr){
        char temp = arr[l];
        arr[l] = arr[r];
        arr[r] = temp;
    }
    void reverse(int l, int r, char[] arr){
        if (l>r) return;
        swap(l, r, arr);
        reverse(l+1, r-1, arr);
    } 
    public void reverseString(char[] s) {
        reverse(0, s.length-1, s);
    }
}