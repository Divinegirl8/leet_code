from unittest import TestCase

from twoSumClass import Solution


class TestSolution(TestCase):
    def test_two_sum(self):
        solution = Solution()
        nums = [2, 7, 11, 15]
        target = 9
        expected = [0,1]
        self.assertEqual(solution.twoSum(nums,target),expected)

    def test_two_sum2(self):
        solution = Solution()
        nums = [3,2,4]
        target = 6
        expected = [1,2]
        self.assertEqual(solution.twoSum(nums, target), expected)
