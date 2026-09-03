#4Search Insert Position Easy https://leetcode.com/problems/search-insert-position/
nums = [int(x) for x in input("enter the list of numbers ").split()]
target = int(input("target val:"))
for i in range(len(nums)):
            if nums[i]==target:
                print(i)
                break
            elif target<nums[i]:
                print(i)
                break
else:
    print(len(nums))