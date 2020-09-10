from typing import List

class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        i = 0
        result: List[List[int]] = []
        while i < 8:
            if [i, king[1]] in queens:
                result.append([i, king[1]])
                break
            i = i + 1
        i = 0
        while i < 8:
            if king + [0, i] in queens:
                result.append(king + [i, 0])
                break
            i = i + 1
        while i < 8:
            if king + [0, i] in queens:
                result.append(king + [i, 0])
                break
            i = i + 1