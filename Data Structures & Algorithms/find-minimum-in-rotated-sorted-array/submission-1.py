class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n - 1

        while l < r:
            mid = (l + r) // 2    
            curr = nums[mid]
            if curr > nums[r]:
                l = mid + 1
            else: 
                r = mid
        return nums[l]
        #     if curr < nums[mid - 1] and curr < nums[mid + 1]:
        #         return curr
        #     elif curr < nums[mid + 1] and curr > nums[mid - 1]:
        #         l = mid + 1
        #     else:
        #         r = mid - 1
        # return -1


# nums = [4,5,6,7]
#         0 1 2 3
#         l m   r
# l = 0
# r = 1
# mid = 0
# curr = 4
# nums[r] = 5



# nums = [3,4,5,6,1,2]
#         0 1 2 3 4 5
#               l m r
# l = 3
# r = 5
# mid = 4
# curr = 5


# nums = [4,5,6,7]
#         0 1 2 3
#         l     r
# l = 0
# r = 3


# nums = [3,4,5,6,1,2]
#         0 1 2 3 4 5
#               l m r
# l = 3
# r = 5
# mid = 4
# curr = 5