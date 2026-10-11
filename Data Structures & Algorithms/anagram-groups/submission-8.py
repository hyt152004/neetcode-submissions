from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # use the alphabet count as the key of a hashmap
        # we can do this because this question only uses alpabets.

        anagramMap = defaultdict(list)
        for s in strs:
            # there are 26 letters in the alphabet
            count = [0] * 26
            for c in s:
                # use ord ascii values 
                count[ord(c) - ord("a")] += 1
            anagramMap[tuple(count)].append(s)

        return list(anagramMap.values())
            


