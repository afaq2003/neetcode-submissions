class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        for i in nums:
            count[i] = count.get(i,0)+1
        n = len(nums)//2
        for i in count:
            if count[i]>n:
                return i
