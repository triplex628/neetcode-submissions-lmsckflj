import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = re.sub(r'[\W_]+', '', s)
        result = result.lower()
        return result == result[::-1]