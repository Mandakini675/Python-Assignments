#2Remove Duplicates from Sorted Array https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# Example 1:

# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
# Explanation: Your function should return k = 2,
#  with the first two elements of nums being 
#  1 and 2 respectively.
# It does not matter what you leave beyond 
# the returned k (hence they are underscores).

numbers = [int(x) for x in input("enter the list of numbers ").split()]
ans = []
for num in numbers:
    if num not in ans:
        ans.append(num)
       

print(ans)
#~~~~~~~~~~~~~~~~~~~~~leetcode solution
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        write = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[write] = nums[i]
                write += 1

        return write