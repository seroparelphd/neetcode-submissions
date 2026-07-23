from collections import defaultdict
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for num in nums:
            # print(f"num = {num}")
            # print(f"  counts[num] = {counts[num]}")
            counts[num] += 1

        # Sort by frequency
        # print(f"counts.items = {counts.items}")
        sorted_counts = sorted(counts.items(), key = lambda x: x[1], reverse = True)  # in tuple form
        # print(f"sorted_counts = {sorted_counts}")
        
        res = []
        # Get only top k items
        for num, count in sorted_counts[:k]:
            res.append(num)
        return res