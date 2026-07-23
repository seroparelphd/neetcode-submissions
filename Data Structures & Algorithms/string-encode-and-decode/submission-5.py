class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "__EMPTY__"
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
        if s == "__EMPTY__":
            return []
        if s == "":
            return [""]
        return s.split("\t")