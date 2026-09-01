class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums2 + nums1
        nums.sort()
        n = len(nums)
        # m = n % 2
        # print(m)
        if n % 2 == 1:
            mid = n // 2
            res = float(nums[mid])
            return res
        else:
            left = n // 2 - 1
            right = n // 2 
            res = float((nums[left] + nums[right]) / 2)
            return res
            