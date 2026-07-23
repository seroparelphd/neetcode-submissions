# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        if pairs == []:
            return []
        sorted = []
        sorted.append(pairs[:])
        # Traverse through 1 to len(pairs)
        for i in range(1, len(pairs)):
            j = i - 1
            while j >= 0 and pairs[j + 1].key < pairs[j].key:
                # pairs[j] and pairs[j + 1] are out of order so swap them         
                tmp = pairs[j + 1]
                pairs[j + 1] = pairs[j]
                pairs[j] = tmp
                j -= 1
            sorted.append(pairs[:])
        return sorted