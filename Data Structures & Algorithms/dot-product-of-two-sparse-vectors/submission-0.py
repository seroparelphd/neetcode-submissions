class SparseVector:
    def __init__(self, nums: List[int]):
        self.pairs = []
        for index, value in enumerate(nums):
            if value != 0:
                self.pairs.append([index, value])

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        # print(self.pairs)
        v1i, v2i, product = 0, 0, 0
        # print(f"len(vec.pairs) = {len(vec.pairs)}")
        while v1i < len(self.pairs) and v2i < len(vec.pairs):
            if self.pairs[v1i][0] == vec.pairs[v2i][0]:
                product += self.pairs[v1i][1] * vec.pairs[v2i][1]
                v1i += 1
                v2i += 1
            elif self.pairs[v1i][0] < vec.pairs[v2i][0]:
                v1i += 1
            else:
                v2i += 1
        return product

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)

# v1 = [[0, 1], [3, 2], [4, 3]]
# v2 = [[1, 3], [3, 4]]