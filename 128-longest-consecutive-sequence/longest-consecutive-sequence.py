# class Solution(object):
#     def longestConsecutive(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         if len(nums) in [0,1]:
#             return len(nums)
#         value= min(nums)
#         print(value)
#         max_count=0
#         count=1
#         for i in range(len(nums)-1):
#             value=value+1
#             print(value)
#             if value in nums:
#                 count=count+1
#                 if count>max_count:
#                     max_count=count
#             else:
#                 if count>max_count:
#                     max_count=count
#                 count=1
#             print("count is "+ str(count))

#         return max_count

# class Solution(object):
#     def longestConsecutive(self, nums):
#         if len(nums) in [0,1]:
#             return len(nums)
#         value = min(nums)
#         max_count = 1
#         count = 1
#         for i in range(len(nums)-1):
#             value = value + 1
#             if value in nums:
#                 count = count + 1
#                 # always update max_count
#                 if count > max_count:
#                     max_count = count
#             else:
#                 count = 1
#         return max_count

class Solution(object):
    def longestConsecutive(self, nums):
        if not nums:
            return 0

        nums_set = set(nums)   # O(n) to build the set
        longest = 0

        for num in nums_set:
            # Only start counting if it's the beginning of a sequence
            if num - 1 not in nums_set:
                current = num
                count = 1

                while current + 1 in nums_set:
                    current += 1
                    count += 1

                longest = max(longest, count)

        return longest



        