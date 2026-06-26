class Solution:
    def dailyTemperatures(self, nums: List[int]) -> List[int]:
        s=[]
        res=[0]*(len(nums))
        for i, e in enumerate(nums):
            while s and nums[s[-1]]<e:
                b=s.pop()
                res[b]=i-b
            s.append(i)
        return res
