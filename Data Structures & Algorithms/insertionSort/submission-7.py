# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:

        # Check if empty
        if pairs == []:
            return []

        # Initialize a list to add lists into
        sorted = []

        # Initial state of the array
        sorted.append(pairs[:])  # [:] to clone
        
        # Traverse through 1 to len(pairs)
        for i in range(1, len(pairs)):
            j = i - 1
            while j >= 0 and pairs[j + 1].key < pairs[j].key:
                # pairs[j].key and pairs[j + 1].key are out of order so swap them         
                tmp = pairs[j + 1]
                pairs[j + 1] = pairs[j]
                pairs[j] = tmp
                j -= 1

            # state of the array after each insertion
            sorted.append(pairs[:])  # [:] to clone
        return sorted