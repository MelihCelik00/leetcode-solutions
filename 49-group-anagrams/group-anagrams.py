class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        
        for s in strs:
            count = [0] * 26 # a...z

            for c in s:
                count[ord(c) - ord("a")] += 1

            result[tuple(count)].append(s)

        return result.values()

        # O(m*n), m for len of strs [], n for len of c