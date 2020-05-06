class Solution(object):
    def removeElement(self, nums, val):
        idx = 0
        for k,l in enumerate(nums):
            if l != val:
                nums[idx] = nums[k]
                idx += 1
        return idx + 1
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
