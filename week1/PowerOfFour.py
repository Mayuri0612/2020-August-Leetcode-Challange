class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0:
            return False
        else:
            while(num != 1):
                if (num % 4 != 0):
                    return False
                else:
                    num = num // 4
            return True