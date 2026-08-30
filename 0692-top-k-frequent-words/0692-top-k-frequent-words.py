class Solution(object):
    def topKFrequent(self, words, k):
       count=Counter(words)
       return heapq.nsmallest(k, count, key=lambda x: (-count[x], x))
        