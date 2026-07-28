class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:  # and r < len(numbers):
            if numbers[l] + numbers[r] == target:
                return [l + 1, r + 1]
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                r -= 1
                # l += 1
                # r = l + 1
        return []

# Time: O(n)
# Space: O(1)

# [1,2,3,4]
#  l r
# target = 3
# diff = 