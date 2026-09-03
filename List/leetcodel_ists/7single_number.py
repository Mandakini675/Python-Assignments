#7Single Number Easy https://leetcode.com/problems/single-number/
        
class Solution(object):
    def singleNumber( nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for num in nums:
           if nums.count(num)==1:
               return num
        #~~~~~~~~~~~o(n) tc cause of X-OR 
        # ans =0 
        # for num in nums:
        #     ans^= num
        # return ans
    print(singleNumber([1,2,2,4,1]))