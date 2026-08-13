class Solution(object):
    def concatWithReverse(self, nums):
        ans=[]
        n=len(nums)
        for i in range(0,n):
            ans.append(nums[i])
        for i in range(n-1,-1,-1):
            ans.append(nums[i])
        return ans
        