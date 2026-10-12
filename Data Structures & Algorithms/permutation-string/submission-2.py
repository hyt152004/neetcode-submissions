from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        # make a freq count for s1

        # for every combination of s2 of len(s1), check if the two hashmaps equal

        s1Freq = Counter(s1)

        for i in range(len(s2) - len(s1) + 1):
            substring = s2[i:i+len(s1)]
            print(substring)

            substringFreq = Counter(substring)

            if s1Freq == substringFreq:
                return True

        return False
        
