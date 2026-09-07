class Solution(object):
    def kWeakestRows(self, mat, k):
        m=len(mat)
        arr=[]
        for i in range(0,m):
            count=sum(mat[i])
            arr.append((count,i))
        arr.sort()
        return [arr[i][1] for i in range(k)]
        