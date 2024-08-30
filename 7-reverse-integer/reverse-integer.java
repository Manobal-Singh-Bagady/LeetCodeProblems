class Solution {
    public int reverse(int x) {
        int num = x;
        boolean negative = x<0?true:false;
        if (negative) num*=-1;
        long ans = 0;

        while (num>0){
            ans*=10;
            ans+=(num%10);
            num/=10;
            if (ans>=Integer.MAX_VALUE) return 0;
        }
        return (int)(negative?-1*ans:ans);
    }
}