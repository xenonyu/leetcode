from typing import List
class Solution:

    def calculateDrink(self, n: int) -> int:
        output = 0
        if n == 2:
            return 1
        elif n == 1 or n == 0:
            return 0
        else:
            output = output + n // 3
            res = n // 3 + n % 3
            output = output + self.calculateDrink(res)
        return output


test = Solution()
print(test.calculateDrink(10))
