class Solution(object):
    def trafficSignal(self, timer):
        if timer==0:
            s="Green"
            return s
        elif timer==30:
            p="Orange"
            return p
        elif 30<timer<=90:
            q="Red"
            return q
        else:
            r="Invalid"
            return r
        