from typing import List
import itertools

# class Solution:
#     def letterCombinations(self, digits: str) -> List[str]:
#         if not digits:
#             return []
#         phoneMap = {'2': 'abc',
#                     '3': 'def',
#                     '4': 'ghi',
#                     '5': 'jkl',
#                     '6': 'mno',
#                     '7': 'pqrs',
#                     '8': 'tuv',
#                     '9': 'wxyz'}
#
#         def search(combination: str, resumeDigits: str) -> List[str]:
#             if not resumeDigits:
#                 res.append(combination)
#             else:
#                 print(combination)
#                 for char in phoneMap[resumeDigits[0]]:
#                     search(combination + char, resumeDigits[1:])
#             return combination
#         res = []
#         search('', digits)
#         return res

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits)==0:
            return []
        conversion={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        return [''.join(item) for item in itertools.product(*(conversion[char] for char in digits))]


if __name__ == '__main__':
    inputStr = "23"
    test = Solution()
    print(test.letterCombinations(inputStr))
    for item in itertools.product(*inputStr, *inputStr):
        print(item)
