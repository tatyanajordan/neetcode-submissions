class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            delim_idx = s.find('#', i)
            length = int(s[i:delim_idx])
            start = delim_idx + 1
            res.append(s[start:start + length])
            i = start + length
        return res