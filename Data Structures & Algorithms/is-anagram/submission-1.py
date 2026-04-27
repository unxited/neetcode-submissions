class Solution:
    def stTodict(self, s: str) -> dict:
        charcountdict = {}
        for char in s:
            charcount = charcountdict.get(char, 0)
            charcountdict[char] = charcount + 1
        return charcountdict    

    def isAnagram(self, s: str, t: str) -> bool:
        return self.stTodict(s) == self.stTodict(t)

        

