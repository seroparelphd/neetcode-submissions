class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = {}
        current_max = 0
        result = 0
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
            if counts[num] > current_max:
                result = num
            current_max = max(counts[num], current_max)
        return result
        