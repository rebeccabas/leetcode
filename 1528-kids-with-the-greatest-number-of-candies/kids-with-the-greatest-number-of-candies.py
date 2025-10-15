class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        arr= []
        maxCandies = max(candies)
        for i in candies:
                arr.append(i+extraCandies>=maxCandies)
        return arr
        