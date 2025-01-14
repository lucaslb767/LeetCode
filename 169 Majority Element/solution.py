class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        dict_nums = {}

        for n in nums:
            if not n in dict_nums:
                dict_nums[n] = 1
            else:
                dict_nums[n] += 1
        
        answer = None

        for key,value in dict_nums.items():
            if value > len(nums)/2:
                answer = key
                break
        return answer