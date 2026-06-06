class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = {}
        for i in strs:
            count = [0]*26
            for j in i:
                count[97 - ord(j)] += 1
            if tuple(count) not in freq:
                freq[tuple(count)] = [i]
            else:
                freq[tuple(count)].append(i)
        # print(freq)
        return list(freq.values())
