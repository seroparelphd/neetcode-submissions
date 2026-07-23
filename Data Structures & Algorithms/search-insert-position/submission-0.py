class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2      # mid = 3
            mid_num = nums[mid]     # mid_num = 4
            if target == mid_num:   
                return mid
            elif target > mid_num:
                l = mid + 1         # l = 4
            else: 
                r = mid - 1         # r = 4
        return l  # 4

# nums = [-1,0,2,4,6,8], target = 5
