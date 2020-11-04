class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def rob1(start, end):
            robbed = skipped = 0
            for m in nums[start:end + 1]:
                r = robbed
                robbed = skipped + m
                skipped = max(skipped, r)
            return max(robbed, skipped)
        return max(rob1(0, len(nums) - 2), rob1(1, len(nums) - 1))
                

