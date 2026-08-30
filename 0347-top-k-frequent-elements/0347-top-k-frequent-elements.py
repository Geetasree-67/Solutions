class Solution(object):
    def topKFrequent(self, nums, k):
        count=Counter(nums)
        return heapq.nlargest(k,count,key=count.get)
        