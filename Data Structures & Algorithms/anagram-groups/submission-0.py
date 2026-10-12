class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        dct = {}

        for string in strs:
            cnt = [0] * 26
            for letter in string:
                cnt[ord(letter) - ord('a')] += 1
            cnt = tuple(cnt)
            if cnt in dct:
                dct[cnt].append(string)
            else:
                dct[cnt] = [string]
        return [
            dct[element] for element in dct       
        ]
