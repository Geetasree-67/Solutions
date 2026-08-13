class Solution(object):
    def countSymmetricIntegers(self, low, high):
        count=0
        for x in range(low,high+1):
            s = str(x)
            if len(s) % 2 != 0:
                continue
            n = len(s) // 2
            left_sum = sum(map(int, s[:n]))
            right_sum = sum(map(int, s[n:]))
            if left_sum==right_sum:
                count+=1
        return count
        