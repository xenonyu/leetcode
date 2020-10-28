from typing import List


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        q1 = set(['0000'])
        q2 = set([target])
        visit = set()
        step = 0

        def updown(inStr, index, up=True):
            before = inStr[0:index]
            after = inStr[index + 1:]
            target = inStr[index]
            if target == '9' and up == True:
                target = '0'
            elif target == '0' and up == False:
                target = '9'
            else:
                change = 1 if up else -1
                target = chr(ord(target) + change)
            return before + target + after

        while len(q1) and len(q2):
            temp = set()
            for cur in q1:
                if cur in deadends: continue
                if cur in q2: return step
                visit.add(cur)
                for i in range(4):
                    up = updown(cur, i)
                    if up not in deadends:
                        visit.add(up)
                        temp.add(up)
                    down = updown(cur, i, False)
                    if down not in deadends:
                        visit.add(down)
                        temp.add(down)
            step += 1
            q1 = q2
            q2 = temp.copy()
        return -1


if __name__ == '__main__':
    deads = ["0201", "0101", "0102", "1212", "2002"]
    target = '0202'
    test = Solution()
    res = test.openLock(deads, target)
    print(res)
