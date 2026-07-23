class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # seen = []

        # for num in nums:
        #     if num in seen:
        #         return True
        #     else:
        #         seen.append(num)
            
        # return False

        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
