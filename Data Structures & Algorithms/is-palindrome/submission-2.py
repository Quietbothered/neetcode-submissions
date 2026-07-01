class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = True 
        b = ""
        for i in s:
            if i.isalnum():
                b+=i
            else:
                continue
        b = b.lower()
        for i in range(len(b)//2):
            if len(b) == 1 :
                break
            elif b[i]== b[len(b)-i-1]:
                continue
            else:
                a = False
        print(b)
        return a
