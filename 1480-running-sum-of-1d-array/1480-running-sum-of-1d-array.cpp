class Solution {
public:
    vector<int> runningSum(vector<int>& nums) {
        vector<int>ans;
        int add=0;
        for(int i=0;i<nums.size();i++){
            add+=nums[i];
            ans.push_back(add);

        }
       return ans; 
    }
};