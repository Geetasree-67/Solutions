class Solution(object):
    def mySqrt(self, x):
        n = x
        l, r = 0, n
        while l <= r:
            mid = (l + r) // 2
            if mid * mid <= n:
                l = mid + 1
            else:
                r = mid - 1
        return r