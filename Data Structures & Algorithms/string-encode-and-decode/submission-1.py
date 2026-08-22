class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "None"
        k = []
        for i in strs:
            k.append(i[::-1])
        g = "@d!ty@".join(k)
        return g

    def decode(self, s: str) -> List[str]:
        if s == "None":
            return []
        k = []
        if not s:
            return [""]
        for i in s.split("@d!ty@"):
            if not i:
                k.append("")
                continue
            s1 = i[::-1]
            k.append(s1)
        return k
            
