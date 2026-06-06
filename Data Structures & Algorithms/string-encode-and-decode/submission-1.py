class Solution:

    def encode(self, strs: List[str]) -> str:
        self.encoded_string = ""
        for i in strs:
            len_str = len(i)
            self.encoded_string += str(len_str) + "#" + i
        return self.encoded_string

    def decode(self, s: str) -> List[str]:
        self.decoded_strs = []
        i = 0
        while i < len(s):
            j = s.find("#", i)
            length = int(s[i:j])
            self.decoded_strs.append(s[j+1 : j+1+length])
            i = j + 1 + length
        return self.decoded_strs