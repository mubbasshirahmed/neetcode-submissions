class Solution:

    def encode(self, strs: List[str]) -> str:

        res = ""

        for word in strs:
            length = str(len(word))
            res += length + '#'
            res += word
        print(res) 
        return res 

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        length = 0

        while i < len(s):
            start = i

            while s[i] != '#':
                i += 1
            
            length = int(s[start: i])
            print(length)
            i += 1
            print(i)

            word = s[i: i + length]
            res.append(word)

            i += length 

        return res 

