class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [0] * len(nums)
        for i in range(len(nums)):
            counter = 0
            for j in range(len(nums)):
                if nums[i] > nums[j]:
                    counter += 1
            result[i] = result[i] + counter
        return result