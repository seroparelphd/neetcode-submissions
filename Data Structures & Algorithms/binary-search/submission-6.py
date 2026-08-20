class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n - 1    # 5
        while l <= r:
            mid = (l + r) // 2      # 5 // 2 = 2
            curr = nums[mid]
            if curr < target:
                l = mid + 1   # 2 + 1 = 3
            elif curr > target:
                r = mid - 1  
            else:
                return mid
        return -1

# Time O(log n)
# Space O(1)

# target = 3
# nums = [-1,0,2,4,6,8]
#              l     r    
# n = 6
# mid = 3