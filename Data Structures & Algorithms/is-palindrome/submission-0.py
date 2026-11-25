# Jordan solution:

# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         result = ""
#         for ch in s:
#             if ch.isalnum():
#                 result += ch
#             continue
#         if result.lower() == result.lower()[::-1]:
#             return True
#         return False

class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = [ch.lower() for ch in s if ch.isalnum()]
        return cleaned == cleaned[::-1]
        

       
        