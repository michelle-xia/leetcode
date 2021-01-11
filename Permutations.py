class Solution:
    def permute(self, nums):
        out = []
        
        if len(nums) == 1:
            return [nums[:]]
        
        for _ in range(len(nums)):
            val = nums.pop(0)
            permutations = self.permute(nums)

            for permutation in permutations:
                permutation.append(val)

            out.extend(permutations)
            nums.append(val)
        
        return out 