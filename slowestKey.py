from typing import List


class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        minTime, minKey = releaseTimes[0], keysPressed[0]
        lastVal = releaseTimes[0]
        for i, val in enumerate(releaseTimes[1:]):
            if val - lastVal >= minTime: minTime, minKey = val - lastVal, keysPressed[i + 1]
            # print (val-lastVal, minTime, keysPressed[i+1])
            lastVal = val
        return minKey
