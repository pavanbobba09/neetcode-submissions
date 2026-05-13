class Solution:
    def isPalindrome(self, s: str) -> bool:

        l, r = 0, len(s) - 1

        while l < r:

            # skip non-alphanumeric from left
            while l < r and not self.isalphaNum(s[l]):
                l += 1

            # skip non-alphanumeric from right
            while l < r and not self.isalphaNum(s[r]):
                r -= 1

            # compare characters
            if s[l].lower() != s[r].lower():
                return False

            # move inward
            l += 1
            r -= 1

        return True

    def isalphaNum(self, c):
        return (
            ord('a') <= ord(c) <= ord('z') or
            ord('A') <= ord(c) <= ord('Z') or
            ord('0') <= ord(c) <= ord('9')
        )
