class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        countR = 0
        countL = 0
        count = 0
        for string in s:
            if (string=='R'):
                countR+=1
            else:
                countL+=1
            if (countR==countL):
                count+=1
            
        return count
        