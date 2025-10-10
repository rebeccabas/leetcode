class Solution(object):
    def findClosest(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: int
        """
        for1 = abs(z-x)
        for2 = abs(z-y)
        if(for1<for2):
            return 1
        elif(for2<for1):
            return 2
        elif(for1==for2):
            return 0

        