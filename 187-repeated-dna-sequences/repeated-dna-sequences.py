class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        final = []
        seen = []
        for i in range(len(s)-9):
            substring= s[i:i+10]
            seen.append(substring)
        count= Counter(seen)
        for key, value in count.items():
            if value>1:
                final.append(key)
        return final

        