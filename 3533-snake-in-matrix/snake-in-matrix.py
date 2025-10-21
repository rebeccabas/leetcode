class Solution(object):
    def finalPositionOfSnake(self, n, commands):
        """
        :type n: int
        :type commands: List[str]
        :rtype: int
        """
        val = 0
        for command in commands:
            if command == "UP":
                val = val -n
            elif command == "DOWN":
                val = val + n 
            elif command == "LEFT":
                val = val -1
            else:
                val = val +1
        return val
                

        