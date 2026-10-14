class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for word in strs:
            output += str(len(word)) + "#" + word
        print(output)
        return output

    def decode(self, s: str) -> List[str]:
        output = []
        i = 0
        while(i < len(s)):
            end = s.find('#', i)
            lenstring = s[i:end]
            
            length = int(lenstring)
            output.append(s[end+1: i + len(lenstring) + length+1])
            i += len(lenstring) + length+1
        return output
