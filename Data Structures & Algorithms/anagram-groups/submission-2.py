from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_table = defaultdict(list)
        for s in strs:
            key = tuple(sorted(s))
            # print(f"key = {key}")
            hash_table[key].append(s)
            # print(f"  hash_table = {hash_table}")
        return list(hash_table.values())