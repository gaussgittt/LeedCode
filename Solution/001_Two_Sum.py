class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash = {}
        for i in range(len(nums)):
            if target - nums[i] in hash:
                return [hash[target - nums[i]], i]
            hash[nums[i]] = i

        return [-1, -1]

#debug
nums = [2, 7, 11, 15]

s = Solution()
print s.twoSum(nums, 9)





'''
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''