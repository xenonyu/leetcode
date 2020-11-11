from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = 0
        profits = []
        states = True
        for i, p in enumerate(prices):
            if i < 1: continue
            if p > prices[i - 1] and states == False:
                low = i - 1
            elif p < prices[i - 1] and states == True:
                profits.append(prices[i - 1] - prices[low])
                low = i
            if p >= prices[i - 1]:
                states = True
            else:
                states = False
        profits.sort(reverse=True)
        print(profits)
        return profits[0] + profits[1]


if __name__ == '__main__':
    test = Solution()
    inputList = [3, 3, 5, 0, 0, 3, 1, 4]
    print(test.maxProfit(inputList))
