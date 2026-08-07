class Solution(object):
    def findErrorNums(self, nums):
        n=len(nums)
        c=Counter(nums)
        a=[]
        for i in range(0,n+1):
            if c[i]==2:
                a.append(i)
        for i in range(1,n+1):
            if c[i]==0:
                a.append(i)
        return a
        