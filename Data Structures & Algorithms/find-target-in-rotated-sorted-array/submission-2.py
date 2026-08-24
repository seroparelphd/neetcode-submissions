class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n - 1

        while l < r:
            mid = (l + r) // 2    
            curr = nums[mid]
            if curr > nums[r]:
                l = mid + 1
            else: 
                r = mid # - 1
        # return nums[l]
        if nums[l] <= target and target <= nums[-1]:
            l2, r2 = l, n - 1
        else:
            l2, r2 = 0, l

        # l2, r2 = 0, n - 1    # 5
        while l2 <= r2:
            mid2 = (l2 + r2) // 2      # 5 // 2 = 2
            curr2 = nums[mid2]
            if curr2 < target:
                l2 = mid2 + 1   # 2 + 1 = 3
            elif curr2 > target:
                r2 = mid2 - 1  
            else:
                return mid2
        return -1


        # findMin_ix = l

        # if target > nums[0]:
        #     l2, r2 = 0, r
        #     while l2 <= r2:
        #         mid2 = (l2 + r2) // 2
        #         curr2 = nums[mid2]
        #         if curr2 > nums[r2]:
        #             l = mid2 + 1
        #         elif:
        #             r = mid2 - 1
        #     return 



# nums = [3,5,6,0,1,2], target = 4
#               m