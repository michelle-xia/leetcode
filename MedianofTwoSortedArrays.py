class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        nums = nums1 + nums2
        nums.sort()
        return nums[len(nums) // 2 ]  if len(nums) % 2 == 1 else (nums[len(nums) // 2] + nums[len(nums) // 2 - 1] ) / 2