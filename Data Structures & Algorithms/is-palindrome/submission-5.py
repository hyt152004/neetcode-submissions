class Solution:
    def isPalindrome(self, s: str) -> bool:
        leftp = 0
        rightp = len(s) - 1

        while leftp < rightp:
            left = s[leftp]
            right = s[rightp]
            
            if not left.isalnum():
                leftp += 1
                continue
            if not right.isalnum():
                rightp -= 1
                continue

            if left.lower() != right.lower():
                return False

            leftp += 1
            rightp -= 1

        return True 

            