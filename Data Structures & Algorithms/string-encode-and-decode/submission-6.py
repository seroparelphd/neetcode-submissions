class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "NONE"
        if strs == [""]:
            return ""
        encoded = ""
        for s in strs[:-1]:
            # print(f"s = {s}")
            encoded = encoded + s + "\t"
            # print(f"  encoded = {encoded}")
        encoded = encoded + strs[-1]
        # print(f"return encoded = {encoded}")
        return encoded

    def decode(self, s: str) -> List[str]:
        if s == "NONE":
            return []
        if s == "":
            return [""]
        return s.split("\t")