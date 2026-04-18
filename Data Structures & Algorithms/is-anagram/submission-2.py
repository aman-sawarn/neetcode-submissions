class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        ascii = [0]*26
        for i in range(len(s)):
            index = ord(s[i])-ord('a')
            ascii[index]+=1
            index = ord(t[i])-ord('a')
            ascii[index]-=1
            
        for i in range(len(ascii)):
            if ascii[i]!=0:
                return False
        return True

        