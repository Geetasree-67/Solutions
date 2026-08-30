class Solution(object):
    def minimumDeletions(self, nums):
        n=len(nums)
        mini=nums.index(min(nums))
        maxi=nums.index(max(nums))
        a=min(mini,maxi)
        b=max(mini,maxi)
        return min(b+1,n-a,a+1+n-b)
        