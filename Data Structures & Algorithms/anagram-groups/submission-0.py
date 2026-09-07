class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # anagram -> hashmap[count] = list of anagrams with same structure

        result = defaultdict(list)

        for string in strs:
            count = [0]*26 # Array of 26 characters
            for char in string:
                count[ord(char)-ord("a")] += 1
            result[tuple(count)].append(string)
        return list(result.values())