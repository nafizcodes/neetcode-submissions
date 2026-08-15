class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#"+ s
        return res


    def decode(self, s: str) -> List[str]:
        res = []
        i = 0 
        # ["Hello","World"]
        # "5#Hello5#World"
        while i < len(s):
            j = i

            # j=0
            while s[j] != '#':
                j += 1
            
            length = int(s[i:j])
            res.append(s[j + 1: j + 1 + length])

            i = j + 1 + length

        return res
