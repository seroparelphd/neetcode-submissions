class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0,len(nums)):
            diff = target - nums[i]
            if diff in nums and i != nums.index(diff):
                return sorted([i,nums.index(diff)]) 
        return -1

        # for i, num in enumerate(nums):
        #     diff = target - num
        #     if target in nums and i !=0:
        #         return [i, nums]