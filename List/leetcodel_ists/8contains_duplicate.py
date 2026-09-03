
8Contains Duplicate Easy https://leetcode.com/problems/contains-duplicate/

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # isduplicate = True
        # for num in nums:
        #     if nums.count(num)>1:
        #         return isduplicate
        # return False
        #or
        return len(nums) != len(set(nums))
            