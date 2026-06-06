class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = Counter(s)
        count_t = Counter(t)
        for i in s:
            if (i not in count_t) or count_s[i] != count_t[i]:
                return False

        for i in t:
            if (i not in count_s) or count_s[i] != count_t[i]:
                return False
        return True