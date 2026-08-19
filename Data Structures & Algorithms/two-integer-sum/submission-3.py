class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            t = nums[i+1:]
            k = target - nums[i]
            if k in t:
                nums.remove(nums[i])
                return [i, nums.index(k) + 1]

