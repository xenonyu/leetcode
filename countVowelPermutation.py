class Solution:
    def countVowelPermutation(self, n: int) -> int:
        import numpy as np
        c = np.mat([(0, 1, 0, 0, 0), (1, 0, 1, 0, 0), (1, 1, 0, 1, 1), (0, 0, 1, 0, 1), (1, 0, 0, 0, 0)], np.dtype('O'))#这里np.object也可以
        return (c ** (n - 1)).sum() % 1000000007


def main():
    test = Solution()
    print(test.countVowelPermutation(2))


if __name__ == '__main__':
    main()