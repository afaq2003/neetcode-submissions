class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i,cur in enumerate(nums):
            x = target - cur
            if x in seen:
                return [seen[x],i]
            seen[cur]=i
            
