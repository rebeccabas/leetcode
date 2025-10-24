class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        splitwords = s.split()
        length = len(splitwords)
        ls = [0] * length
        for i in range(length):
            splits = splitwords[i]
            ls[i] = splits[::-1]
        return " ".join(ls)