from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = Counter(nums)

        if k > len(count):
            return []
        
        return [word for word,cnt in count.most_common(k)]

        # O(n log k)