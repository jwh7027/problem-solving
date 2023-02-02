class Solution:
    def twoSum(self,nums,target):
        nums = [[n,i] for i, n in enumerate(nums)]
        nums.sort(key = lambda x: x[0])
        l,r =0, len(nums) -1
        while l <= r:
            nums_sum = nums[l][0] + nums[r][0]
            if nums_sum == target:
                return (nums[l][1], nums[r][1])
            elif nums_sum > target:
                r -= 1
            else:
                l += 1