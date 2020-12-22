from handleInput import List


class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        if len(arr) == 1: return []

        def findMax(arr: List[int]) -> int:
            return arr.index(max(arr))

        def rotate(arr, k):
            return arr[:k][::-1] + arr[k:]

        maxIndex = findMax(arr)
        if maxIndex == len(arr) - 1:
            return self.pancakeSort(arr[:-1])
        elif maxIndex == 0:
            arr.reverse()
            return [len(arr)] + self.pancakeSort(arr[:-1])
        else:
            arr = rotate(arr, maxIndex + 1)
            return [maxIndex + 1] + self.pancakeSort(arr)

    def pancakeSortII(self, A):
        res = []
        N = len(A)
        while N:
            idx = A.index(N)
            res.append(idx + 1)
            A = A[:idx + 1][::-1] + A[idx + 1:]
            res.append(N)
            A = A[:N][::-1] + A[N:]
            N -= 1
        # print(A)
        return res


if __name__ == '__main__':
    inputList = [3, 2, 4, 1]
    test = Solution()
    print(test.pancakeSortII(inputList))
