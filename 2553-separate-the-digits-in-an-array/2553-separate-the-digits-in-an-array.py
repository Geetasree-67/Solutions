class Solution(object):
    def separateDigits(self, nums):
        ans=[]
        for num in nums:
            for i in str(num):
                ans.append(int(i))
        return ans
        