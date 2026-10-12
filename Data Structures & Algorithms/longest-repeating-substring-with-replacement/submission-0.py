from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # start at index 0
        # check if its valid, len(substring) - most freq char

        # how do i keep track of the msot freq char

        # if <= k -> valid
        # else -> invalid

        freqMap = defaultdict(int)

        leftP = 0
        rightP = 0
        rsf = 0

        while rightP < len(s):
            rightVal = s[rightP]
            freqMap[rightVal] += 1
            mostFreq = max(freqMap.values())
            replacementCount = (rightP - leftP + 1) - mostFreq

            if replacementCount <= k:
                rsf = max(rsf, rightP - leftP + 1)

            else:
                freqMap[s[leftP]] -= 1
                leftP += 1

                
            rightP += 1
        
        return rsf

