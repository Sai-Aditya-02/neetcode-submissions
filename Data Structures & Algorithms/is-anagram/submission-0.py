class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_s = "".join(sorted(s))
        t_s = "".join(sorted(t))
        return s_s == t_s