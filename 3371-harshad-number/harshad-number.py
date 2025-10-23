class Solution(object):
    def sumOfTheDigitsOfHarshadNumber(self, x):
        """
        :type x: int
        :rtype: int
        """
        val = list(str(x))
        sum = 0
        for num in val:
            sum+=int(num)
        if x%sum == 0:
            return sum
        else:
            return -1

        