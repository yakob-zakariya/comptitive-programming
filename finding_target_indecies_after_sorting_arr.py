class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = []
        for i in range(len(nums)-1,0,-1):
            for j in range(i):
                if nums[j] > nums[j+1]:
                    temp= nums[j]
                    nums[j] = nums[j+1]
                    nums[j+1] = temp
        for c in range(len(nums)):
            if nums[c] == target:
                result.append(c)
        return result