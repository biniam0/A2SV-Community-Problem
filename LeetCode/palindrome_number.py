class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x == int(str(x)[::-1]):
            return True
        else:
            return False
