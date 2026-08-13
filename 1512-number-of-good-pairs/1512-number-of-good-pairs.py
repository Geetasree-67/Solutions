class Solution(object):
    def numIdenticalPairs(self, nums):
        count=0
        n=len(nums)
        for i in range(0,n):
            for j in range(i+1,n):
                if nums[j]==nums[i]:
                    count+=1
        return count
        