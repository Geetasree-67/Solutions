class Solution(object):
    def countBits(self, n):
        ans=[]
        for i in range (n+1):
            count=0
            x=i
            while(x!=0):
                x=x&(x-1)
                count+=1
            ans.append(count)
        return ans
        