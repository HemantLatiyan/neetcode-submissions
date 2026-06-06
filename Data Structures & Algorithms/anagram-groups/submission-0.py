class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = {}
        for i in strs:
            abc = [0]*26
            for j in i:
                abc[97-ord(j)] += 1
             
            if tuple(abc) not in groups:
                groups[tuple(abc)] = [i]
            else:
                groups[tuple(abc)].append(i)

        return [v for k, v in groups.items()]