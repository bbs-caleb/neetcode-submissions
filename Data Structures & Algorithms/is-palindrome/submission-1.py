class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(element for element in s.lower() if element.isdigit() or element.isalpha())
        return s == s[::-1]