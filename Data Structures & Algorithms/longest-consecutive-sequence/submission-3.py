class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset=set(nums)
        maxl=0
        for i in numset:
            if i-1 not in numset:
                current=i
                streak=1
                while current+1 in numset:
                    current+=1
                    streak+=1
                maxl=max(maxl, streak)
        return maxl