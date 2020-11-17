from handleInput import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def findKth(index1, index2, k):
            if index1 == self.len1:
                return nums2[index2 + k - 1]
            if index2 == self.len2:
                return nums1[index1 + k - 1]
            if k == 1:
                return min(nums1[index1], nums2[index2])
            target = k // 2 - 1
            newIndex1 = min(index1 + target, self.len1 - 1)
            newIndex2 = min(index2 + target, self.len2 - 1)
            if nums1[newIndex1] <= nums2[newIndex2]:
                k = k - (newIndex1 + 1 - index1)
                index1 = newIndex1 + 1
            else:
                k = k - (newIndex2 + 1 - index2)
                index2 = newIndex2 + 1
            return findKth(index1, index2, k)

        self.len1, self.len2 = len(nums1), len(nums2)
        if (self.len1 + self.len2) % 2:
            k = (self.len1 + self.len2) // 2 + 1
            return findKth(0, 0, k)
        else:
            k1 = (self.len1 + self.len2) // 2
            k2 = k1 + 1
            l = findKth(0, 0, k1)
            r = findKth(0, 0, k2)
            return (l + r) / 2

    def findMedianSortedArraysII(self, nums1: List[int], nums2: List[int]) -> float:
        len1, len2 = len(nums1), len(nums2)

        def getKth(k):
            p1, p2 = 0, 0
            while p1 < len1 and p2 < len2:
                if not k: return min(nums1[p1], nums2[p2])
                if nums1[p1] < nums2[p2]:
                    p1 += 1
                    k -= 1
                else:
                    p2 += 1
                    k -= 1
            if p1 == len1:
                return nums2[p2 + k]
            else:
                return nums1[p1 + k]

        if (len1 + len2) % 2:
            double = False
        else:
            double = True
        if not double:
            k = (len1 + len2) // 2
            return getKth(k)
        else:
            k1 = (len1 + len2) // 2 - 1
            k2 = k1 + 1
            return (getKth(k1) + getKth(k2)) / 2


if __name__ == '__main__':
    nums1 = [2]
    nums2 = [1, 3, 4]
    test = Solution()
    res = test.findMedianSortedArraysII(nums1, nums2)
    print(res)
