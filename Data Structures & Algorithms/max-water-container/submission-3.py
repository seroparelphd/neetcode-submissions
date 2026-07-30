class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_amt = 0
        while l < r:
            width = r - l
            amt = min(heights[l], heights[r]) * width
            max_amt = max(amt, max_amt)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return max_amt

# height = [1,7,2,5,4,7,3,6]
#           0 1 2 3 4 5 6 7 
#           l             r 
# r - l = 7-0 