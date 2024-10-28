class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Method 1: Sort and Compare
        return sorted(s) == sorted(t)

        # Method 2: Use Counter
        # return Counter(s) == Counter(t)

        # Method 3: Count characters manually
        if len(s) != len(t):
            return False
        countS, countT = {}, {}
        
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        
        return True
