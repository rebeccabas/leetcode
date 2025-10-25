class Solution(object):
    def minElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mini=float('inf')
        for num in nums:
            r=0
            while num>0:
                r+= num%10
                num//=10
            mini= min(mini, r)
        return mini
        