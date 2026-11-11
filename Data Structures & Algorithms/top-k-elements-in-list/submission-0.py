class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        res = []
        for i in range(len(nums)):
            n = nums[i]
            count = 0
            for j in range (len(nums)):
                if   nums[j] == n:
                    count += 1 
                    hashmap[nums[j]] =  count

        sorted_by_frequency = sorted(hashmap.items(), key=lambda x: x[1], reverse=True)
        
        for index in range(k):
            res.append(sorted_by_frequency[index][0])
            
        return res

            
