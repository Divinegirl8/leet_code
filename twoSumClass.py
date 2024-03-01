class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = []

        for index in range(len(nums)):
            for index2 in range(index):
                sum = nums[index] + nums[index2]

                if sum == target:
                    result.append(index2)
                    result.append(index)
        return result

