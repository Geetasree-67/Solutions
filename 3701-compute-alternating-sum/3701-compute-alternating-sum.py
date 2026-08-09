class Solution(object):
    def alternatingSum(self, nums):
        n=len(nums)
        c=0
        for i in range (0,n):
            if i%2==0:
                c+=nums[i]
            else:
                c-=nums[i]
        return c