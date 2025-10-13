class Solution(object):
    def clearDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        arr = []
        for char in s:
            if char.isdigit() and arr:
                arr.pop()
            else:
                arr.append(char)
        return ''.join(arr)