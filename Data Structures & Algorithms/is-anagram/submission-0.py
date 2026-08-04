class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        count = [0]*26
        for i, v in zip(list(s),list(t)):
            count[ord(i)-ord('a')]+=1
            count[ord(v)-ord('a')]-=1
        return all(c==0 for c in count)
