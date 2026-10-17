class Solution:
    def romanToInt(self, s: str) -> int:
        symbolToVal = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        res = 0
        i = 0
        end = False
        while(i < len(s)-1):
            #subtraction cases
            char = s[i]
            nextChar = s[i+1]
            if((char == "I" and (nextChar == "V" or nextChar == "X"))
            or (char =="X" and (nextChar == "L" or nextChar == "C"))
            or (char == "C" and (nextChar == "D" or nextChar == "M"))):
                res += symbolToVal[nextChar] - symbolToVal[char]
                i+=2
                if(i >= len(s)-1): end = True
            else:
                res += symbolToVal[char]
                i+=1 

        if not end: res += symbolToVal[s[-1]]

        return res
            #othewrise
