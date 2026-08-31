class Solution {
public:
    string toHex(int num) {
        unsigned int n=num;
        string hex="0123456789abcdef";
        string ans="";
        if(n==0){
            return "0";
        }
        while(n>0){
            int digit=n&15;
            ans+=hex[digit];
            n=n>>4;
        }
        reverse(ans.begin(),ans.end());
        return ans;
    }
};