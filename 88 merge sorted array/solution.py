class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        first = nums1[:m]
        i = 0
        j = 0
        z = 0
        while i < len(first) and j < len(nums2):
            if first[i] <= nums2[j]:
                nums1[z] = first[i]
                i += 1
                z += 1
            else:
                nums1[z] = nums2[j]
                j += 1
                z += 1
        while i < len(first):
            nums1[z] = first[i]
            i += 1
            z += 1
        while j < len(nums2):
            nums1[z] = nums2[j]
            j += 1
            z += 1
        print(nums1)