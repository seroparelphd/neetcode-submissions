class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        array = []
        for i in range(len(nums)):
            sub_array = []
            product = 1
            for j, num in enumerate(nums):
                if j != i:
                    # sub_array.append(num)
                    product *= num
            array.append(product)
            # print(f"sub_array = {sub_array}")
            # print(f"  array = {array}")
        return array
        # for a in array:

# Time O(n^2)
# Space O(n)