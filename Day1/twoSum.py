# https://leetcode.com/problems/two-sum

class Solution(object):
    def twoSum(self, nums, target):
        res={}
        for i in range(len(nums)):
            diff= target - nums[i]
            if res.get(diff,False):
                return [res[diff],i]
            res[nums[i]]=str(i)
        return res
