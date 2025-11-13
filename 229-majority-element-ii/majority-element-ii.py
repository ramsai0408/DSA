from collections import Counter

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        repeat = len(nums) // 3
        freq = Counter(nums)
        result = [num for num, count in freq.items() if count > repeat]
        return result


        