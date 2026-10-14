class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        smallest = None
        for i in strs:
            if(smallest == None or len(i) < len(smallest)): smallest = i
        print(smallest)
        for word in strs:
            j=0
            if(not word or word == smallest): continue
            while j < len(smallest) and word[j] == smallest[j]:
                j+=1
            smallest = smallest[:j]
        print(smallest)
        return smallest