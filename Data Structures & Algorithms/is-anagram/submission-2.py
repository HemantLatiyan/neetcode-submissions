class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t) or set(s) != set(t):
            return False
            
        freq1 = {}
        freq2 = {}
        for i in s:
            if i not in freq1:
                freq1[i] = 1
            else:
                freq1[i] += 1
        for i in t:
            if i not in freq2:
                freq2[i] = 1
            else:
                freq2[i] += 1
        
        for i in freq1:
            if i not in freq2 or freq1[i] != freq2[i]:
                return False
        
        for i in freq2:
            if i not in freq1 or freq1[i] != freq2[i]:
                return False

        return True
