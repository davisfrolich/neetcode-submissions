class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = defaultdict(int)
        for num in nums:
            seen[num]+=1
        sorted_items = sorted(seen.items(), key = lambda item: item[1], reverse = True)
        return [item[0] for item in sorted_items[:k]]