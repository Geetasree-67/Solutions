class Solution(object):
    def arraySign(self, nums):
        count=0
        n=len(nums)
        for i in nums:
            if i==0:
                return 0
            if i<0:
                count+=1
        return 1 if count%2==0 else -1     