class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic=defaultdict(list)
        for word in strs:
            key="".join(sorted(word))
            dic[key].append(word)
        return dic.values()