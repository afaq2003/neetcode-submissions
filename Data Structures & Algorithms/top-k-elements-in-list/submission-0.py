class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in nums:
            count[i]=count.get(i,0)+1
        buckets = [[] for _ in range(len(nums)+1)]
        for value,freq in count.items():
            buckets[freq].append(value)
        result = []
        for i in range(len(buckets)-1,0,-1):
            for num in buckets[i]:
                result.append(num)
            if len(result)==k:
                return result
