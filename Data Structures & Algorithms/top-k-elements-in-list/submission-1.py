class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        count = []
        for n in nums:
            hashmap[n] = hashmap.get(n , 0) + 1

        sorted_keys = sorted(hashmap, key=lambda x: hashmap[x], reverse=True)

        return sorted_keys[:k]
