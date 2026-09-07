class Solution(object):
    def kthSmallest(self, matrix, k):
        a=[]
        m=len(matrix)
        for i in range(m):
            for j in range(len(matrix[0])):
                a.append(matrix[i][j])
        a.sort()
        return a[k-1]
        