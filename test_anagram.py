from unittest import TestCase
from anagram import Solution


class Test(TestCase):
    def test_solution(self):
        solution = Solution()
        value = ["tea", "ate", "ant", "eat", "bat"]
        expected = [['tea', 'ate', 'eat'], ['ant'], ['bat']]
        self.assertEqual(solution.group_anagrams(value),expected)
