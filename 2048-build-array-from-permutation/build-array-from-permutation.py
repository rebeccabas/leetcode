class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr = []
        for num in range(len(nums)):
            arr.append(nums[nums[num]])
        return arr
        