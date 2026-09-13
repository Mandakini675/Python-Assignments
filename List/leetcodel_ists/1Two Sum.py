# 1Two Sum Easy https://leetcode.com/problems/two-sum/

nums = [int(x) for x in input("enter array:").split()]
target = int(input("enter the target sum :"))
for i in range(len(nums)):
        curr = nums[i]
        for j in range(i+1,len(nums)):
            if curr+nums[j]==target:
                print( "[",i,",",j,"]")