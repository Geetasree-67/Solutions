class Solution(object):
    def kClosest(self, points, k):
        heap=[]
        for x,y in points:
            distance = x*x + y*y
            heapq.heappush(heap, (distance, x, y))
        ans=[]
        for i in range(k):
            distance, x, y = heapq.heappop(heap)
            ans.append([x, y])
        return ans
        