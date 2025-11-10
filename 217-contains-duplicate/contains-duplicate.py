class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count={}
        flag = False
        for num in nums:
            if num in count:
                count[num]= count[num]+1
            else:
                count[num]=1
        for value in count.values():
            if value >=2:
                flag=True
                break
        if flag:
            return True
        else:
            return False
            

        