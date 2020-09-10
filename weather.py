class Solution:
    def __int__(self):
        self.stack = []

    def weather(self, t):
        weight = 1
        stack = []
        while stack and stack[-1][0] <= t:
            weight += self.stack.pop()[1]
        self.stack.append((t, weight))
        return weight
