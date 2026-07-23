class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        list_of_nums = []
        # print(len(nums), len(nums) -2)
        for i in range(len(nums)-k+1):
            # print(nums[i:i+k])
            list_of_nums.append(nums[i:i+k])
            # print(f"list_of_nums = {list_of_nums}")
        
        maxes = []
        for l in list_of_nums:
            # print(max(l))
            maxes.append(max(l))
            # print(maxes)
        return maxes
