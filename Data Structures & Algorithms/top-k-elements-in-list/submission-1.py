from collections import defaultdict
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for num in nums:
            # print(f"num = {num}")
            # print(f"  counts[num] = {counts[num]}")
            counts[num] += 1
        sorted_counts = sorted(counts.items(), key = lambda x: x[1], reverse = True)
        # print(f"sorted_counts = {sorted_counts}")
        res = []
        for num, count in sorted_counts[:k]:
            res.append(num)
        return res