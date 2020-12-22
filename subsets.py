from handleInput import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            for r in res[:]:
                if r:
                    res.append(r + [num])
                else:
                    res.append([num])
        return res


if __name__ == '__main__':
    inputList = [1, 2, 3]
    test: Solution = Solution()
    res = test.subsets(inputList)
    print(res)
