class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # list_of_nums = []
        # # print(len(nums), len(nums) -2)
        # for i in range(len(nums)-k+1):
        #     # print(nums[i:i+k])
        #     list_of_nums.append(nums[i:i+k])
        #     # print(f"list_of_nums = {list_of_nums}")
        
        # maxes = []
        # for l in list_of_nums:
        #     # print(max(l))
        #     maxes.append(max(l))
        #     # print(maxes)
        # return maxes

        # maxes = []
        # for i in range(len(nums)-k+1):
        #     maxes.append(max(nums[i:i+k]))        
        # return maxes

        output = []
        q = deque()  # index
        l = r = 0

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()

            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1

        return output

        
