class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = dict()
        
        for s in strs:
            ascii = [0]*26
            for j in s:
                index = ord(j) - ord('a')
                ascii[index]+=1
            print(s, ascii)
            
            if count.get(tuple(ascii)):
                count[tuple(ascii)].append(s)
            else:
                count[tuple(ascii)] = []
                count[tuple(ascii)].append(s)
        return list(count.values())



        