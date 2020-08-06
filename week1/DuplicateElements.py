class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dup = []
        unik = {}
        for x in nums:
            if x not in unik:
                unik[x] = 1
            else:
                    dup.append(x)
                    unik[x] += 1
        return dup
                