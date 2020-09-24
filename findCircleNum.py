from typing import List


class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        p = [i for i in range(len(M))]

        def find(x):
            if p[x] == x:
                return x
            p[x] = find(p[x])
            return p[x]

        for i in range(len(M)):
            for j in range(len(M)):
                if M[i][j] == 1:
                    a = find(i)
                    b = find(j)
                    p[a] = b
        for i in range(len(M)):
            p[i] = find(i)
        print(p)
        return len(set(p))
        # resume = [0 for _ in range(len(M))]
        # count = 0
        # def DFS(i):
        #     for j in range(len(resume)):
        #         if M[i][j] == 1 and resume[j] == 0:
        #             resume[j] = 1
        #             DFS(j)
        # res = []
        # for i in range(len(M)):
        #     if resume[i] == 0:
        #         resume[i] = 0
        #         before = resume.copy()
        #         DFS(i)
        #         res.append([before[i] ^ resume[i] for i in range(len(resume))])
        #         count += 1
        # return res


if __name__ == '__main__':
    test = Solution()
    result = test.findCircleNum([[1, 1, 0], [1, 1, 0], [0, 0, 1]])
    print(result)
