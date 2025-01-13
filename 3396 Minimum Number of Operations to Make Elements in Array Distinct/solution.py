class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        set_num = set()
        index = 0
        deletions = 0
        while True:
            if index >= len(nums):
                break
            if nums[index] in set_num:
                index = 0
                del nums[0:3]
                set_num = set()
                deletions += 1
            else:
                set_num.add(nums[index])
                index += 1
        return deletions
        