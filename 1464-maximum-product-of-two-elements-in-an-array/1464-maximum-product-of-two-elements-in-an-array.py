class Solution(object):
    def maxProduct(self, nums):
        nums.sort()
        a=nums[-2:]
        return (a[0]-1)*(a[1]-1)        