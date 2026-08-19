class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = []
        for i in nums:
            if i not in s:
                s.append(i)
        if len(nums) == len(s):
            return False
        return True
