
#10Move Zeroes Easy https://leetcode.com/problems/move-zeroes/
nums = [int(x) for x in input("Enter all zeroes and non zeroes.").split()]      
for i in range(len(nums)-1,-1,-1):
    if nums[i]==0:
            # if 0 in nums:
            nums.remove(nums[i])
            nums.append(0)
print(nums)

for i in range(len(nums)):
            if nums[i] != 0:
                nums[k] = nums[i]
                k += 1
#i is reading and k is writing 
        while k < len(nums):
            nums[k] = 0
            k += 1       