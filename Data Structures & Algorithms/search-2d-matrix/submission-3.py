class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        firsts = [x[0] for x in matrix]
        # print(f"firsts = {firsts}")

        l, r = 0, len(firsts) - 1
        while l <= r:
            mid = (l + r) // 2
            curr = firsts[mid]
            if curr < target:
                l = mid + 1
            elif curr > target:
                r = mid - 1
            else:
                return True
        # print(f"l, r = {l, r}")  # r has target

        l2, r2 = 0, len(matrix[mid]) - 1
        while l2 <= r2:
            mid2 = (l2 + r2) // 2
            curr2 = matrix[r][mid2]
            if curr2 < target:
                l2 = mid2 + 1
            elif curr2 > target:
                r2 = mid2 - 1
            else:
                return True

        return False
            
                
