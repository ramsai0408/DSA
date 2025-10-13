class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        heapq.heapify(nums)
        list1=[]
        for i in range(len(nums)):
            list1.append(heapq.heappop(nums))
        return list1
        