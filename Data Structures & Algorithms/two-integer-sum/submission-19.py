class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        print(nums)
        seen = {}
        for ix, val in enumerate(nums):
            diff = target - val
            if diff in seen:
                return [seen[diff], ix]
            seen[val] = ix
        return -1