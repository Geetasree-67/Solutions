class Solution(object):
    def recoverOrder(self, order, friends):
        s=set(friends)
        return [player for player in order if player in s]
        