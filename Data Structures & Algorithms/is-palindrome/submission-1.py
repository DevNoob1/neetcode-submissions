class Solution:
    def isPalindrome(self, s: str) -> bool:
        if type(s)!=str:
            return False
        c="".join(c.lower() for c in s if c.isalnum())
        if c==c[::-1]:
            return True
        return False