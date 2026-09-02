class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        s = set(nums)
        k = []
        for i in nums:
            if i - 1 not in s:
                k.append(i)
        
        counts = [0]
        for i in k:
            count = 1
            while i+1 in s:
                count += 1
                i += 1
            counts.append(count)
        return max(counts)
            


                
            
            
        
 

            
        