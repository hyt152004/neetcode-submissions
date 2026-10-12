class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False

        s1Freq = [0] * 26
        subStringFreq = [0] * 26

        for i in range(len(s1)):
            s1Freq[ord(s1[i]) - ord("a")] += 1
            subStringFreq[ord(s2[i]) - ord("a")] += 1

        if s1Freq == subStringFreq:
            return True

        
        for i in range(len(s2) - len(s1)):
            charEnter = ord(s2[i+len(s1)]) - ord("a")
            charLeave = ord(s2[i]) - ord("a")
            subStringFreq[charEnter] += 1
            subStringFreq[charLeave] -= 1

            print(s2[i+len(s1)-1])
            print(s2[i])

            if s1Freq == subStringFreq:
                return True



        return False





