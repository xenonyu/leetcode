from handleInput import List


def singleNumber(nums: List[int]):
    res = 0
    for n in nums:
        res ^= n
    return res


inputList = [3, 3, 5, 5, 1]


def reversea(arr):
    arr.reverse()
    return arr


inputList[:3] = reversea(inputList[:3])
print(inputList)
print(inputList)
print(inputList.index(max(inputList)))
