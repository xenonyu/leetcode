# TSP 状压DP

n = int(input())
m = []
for i in range(n):
    m.append(list(map(int, input().split())))

V = 1 << (n - 1)  # 从左至右每一位二进制代表第i个城市是否被访问 如1000代表，第一个城市被访问，而其他城市没有
dp = [[float("inf")] * V for i in range(n)]  # dp[i][j]:从节点i只经过集合j所有点再回到0点所需要的最小开销

for i in range(n):
    dp[i][0] = m[i][0]

for j in range(1, V):
    for i in range(n):
        for k in range(1, n):  # 能不能先到k城市
            if (j >> (k - 1) & 1) == 1:  # 可以途径k
                dp[i][j] = min(dp[i][j], m[i][k] + dp[k][j ^ (1 << (k - 1))])

# 从0出发，经过所有点，再回到0的费用
print(dp[0][(1 << (n - 1)) - 1])
