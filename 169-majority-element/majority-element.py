class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size= len(nums)//2
        count= Counter(nums)
        majority = 0
        for key,val in count.items():
            if val > size:
                if val> majority:
                    majority = val 
                    keym=key
                    
        return keym
                
        