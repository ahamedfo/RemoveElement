class Solution(object):
    def removeElement(self, nums, val):
        k = 0
        idx = 0
        for number in nums:
            if number != val:
                nums[idx] = number
                k+= 1
                idx += 1
        return k
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
