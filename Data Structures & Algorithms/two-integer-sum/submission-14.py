class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 1. Create an empty dictionary
        seen = {}

        # 2. Iterate through the list *once*.
        for i, num in enumerate(nums):
            # 3. Calculate `diff = target - n`.
            diff = target - num
            # 4. Check if `diff` is already in `prevMap`.
            if diff in seen:
                # * **Yes?** Return current index and the index of `diff`.
                return [seen[diff], i]
            # * **No?** Add current number to `prevMap`.
            seen[num] = i
        return -1




