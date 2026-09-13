class Solution:
    def isPalindrome(self, s: str) -> bool:
        string=''
        for i in s:
            if i.isalnum():
                string+=i.lower()

        for i in range(len(string)//2):
            if string[i]!=string[-i-1]:
                return False
        return True