class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []
        n = len(nums)
        for i in range(n):
            j, k = i + 1, n - 1
            while j < k:
                triplet = [nums[i], nums[j], nums[k]]
                if nums[i] + nums[j] + nums[k] == 0 and triplet not in triplets:
                    # triplet = [nums[i], nums[j], nums[k]]
                    # print(f"found triplet = {triplet}")
                    triplets.append(triplet)
                    # print(triplets)
                    j += 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                else:
                    k -= 1
        return triplets

# nums = [-4,-1,-1,0,1,2]
#             i  j     k   = -2
# i = 0
# j = 3
# k = 5

# nums = [-4,-1,-1,0,1,2]
#          i  j        k    = -3

# nums = [-4,-1,-1,0,1,2]
#                  i j k   = 3

