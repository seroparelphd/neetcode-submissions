class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cur_sum = 0
        prefix_sums = {0: 1}
        count = 0
        for num in nums:
            cur_sum += num
            diff = cur_sum - k
            count += prefix_sums.get(diff, 0)
            prefix_sums[cur_sum] = 1 + prefix_sums.get(cur_sum, 0)
        return count

# nums = [2,-1,1,2], k = 2
# cur_sum = 4
# prefix_sums = {
#     0: 1,
#     1: 1
#     2: 2
#     }
# count = 3
# num = 2
# diff = 2