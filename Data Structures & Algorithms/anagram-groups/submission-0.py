class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a=defaultdict(list)
        for s in strs:
            sorted_str="".join(sorted(s))
            a[sorted_str].append(s)
        return list(a.values())