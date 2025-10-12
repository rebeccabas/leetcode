class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        arr = []
        for i in range(left,right+1):
            flag = 0
            strval = list(str(i))
            for j in strval:
                if j=='0':
                    flag = 1
                    break
                if (i%int(j)!=0):
                    flag = 1
            if flag==0:
                arr.append(i)
        return arr
            


        