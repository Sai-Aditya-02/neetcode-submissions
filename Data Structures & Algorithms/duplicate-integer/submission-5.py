class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup_set = set(nums)
        return len(dup_set) != len(nums)
        
        
        