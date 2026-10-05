class Solution(object):
    def permute(self, nums):
        n=len(nums)
        result=[]
        def backtrack(current):
            if (len(current)==n):
                result.append(current[:])
                return
            for i in nums:
                if(i not in current):
                    current.append(i)
                    backtrack(current)
                    current.pop()
        backtrack([])
        return result
        