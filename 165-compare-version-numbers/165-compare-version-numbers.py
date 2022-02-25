class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        nums1 = version1.split(".")
        nums2 = version2.split(".")
        n1 = len(nums1)
        n2 = len(nums2)
        
        for i in range(max(n1, n2)):
            if i < n1:
                i1 = int(nums1[i])
            else:
                i1 = 0
            if i < n2:
                i2 = int(nums2[i])
            else:
                i2 = 0
            if i1 != i2:
                if i1 > i2:
                    return 1
                else:
                    return -1
        return 0
    
    # time complexity = O(N + M + max(N, M))
    # space complexity = O(N + M)


        