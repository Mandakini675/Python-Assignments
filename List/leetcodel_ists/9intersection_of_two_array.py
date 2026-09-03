
9 Intersection of Two Arrays II Easy https://leetcode.com/problems/intersection-of-two-arrays-ii/
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res=[]
        if len(nums1)>len(nums2):
            for i in range(len(nums1)):
                if nums1[i] in nums2:
                    res.append(nums1[i])
                    nums2.remove(nums1[i])
            return res
        else:
            for i in range(len(nums2)):
                if nums2[i] in nums1:
                    res.append(nums2[i])
                    nums1.remove(nums2[i])
            return res
           