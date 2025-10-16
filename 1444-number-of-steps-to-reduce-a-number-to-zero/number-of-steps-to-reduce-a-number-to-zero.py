class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        steps = 0
        for i in range(num):
            if(num==0):
                break
            elif(num%2==0):
                num=num//2
                steps=steps+1
            elif(num%2!=0):
                num=num-1
                steps+=1
        return steps
        