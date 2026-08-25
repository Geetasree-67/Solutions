class Solution(object):
    def missingMultiple(self, nums, k):
        i = 1
        while k * i in nums:
            i += 1   
        return k * i
        