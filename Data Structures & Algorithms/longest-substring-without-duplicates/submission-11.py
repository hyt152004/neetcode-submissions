class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        rsf = 0
        current = set()

        while right < len(s):
            rightVal = s[right]

            while rightVal in current:
                current.remove(s[left])
                left += 1

            rsf = max(rsf, right - left +1)
            current.add(rightVal)
            right += 1

        return rsf
            






