class Solution(object):
    def reverseBits(self, n):
        binary=format(n,'032b')
        reverse_binary=binary[::-1]
        return int(reverse_binary,2)
        