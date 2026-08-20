class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        l = []
        for i in strs:
            if str(sorted(i)) in d:
                d[str(sorted(i))].append(i)
            else:
                d[str(sorted(i))] = [i]
        for v in list(d.values()):
            l.append(v)
        return l

        