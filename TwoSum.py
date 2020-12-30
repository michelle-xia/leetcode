class Solution:
    def twoSum(self, nums, target):
        if nums is None or len(nums) == 0:
            return
        cache = set()
        for num in nums:
            if target - num in cache:
                ind1 = nums.index(target - num)
                nums[ind1] = '*'
                ind2 = nums.index(num)
                return [ind1, ind2]
            else:
                cache.add(num)