from collections import defaultdict, Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # can either sort each string and group them using a hashmap

        # use hashmap as the key of a hashmap
        
        anagramMap = defaultdict(list)

        for s in strs:
            # create a hashmap
            sortedS = "".join(sorted(s))

            anagramMap[sortedS].append(s)

        return list(anagramMap.values())